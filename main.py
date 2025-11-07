from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from neo4j import GraphDatabase
import cohere
import json
import logging
import os

logging.getLogger("neo4j").setLevel(logging.ERROR)

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
COHERE_KEY = os.getenv("COHERE_KEY")

missing_vars = [k for k, v in {
    "NEO4J_URI": NEO4J_URI,
    "NEO4J_USER": NEO4J_USER,
    "NEO4J_PASSWORD": NEO4J_PASSWORD,
    "COHERE_KEY": COHERE_KEY
}.items() if not v]

if missing_vars:
    print(f"❌ Missing environment variables: {', '.join(missing_vars)}")
    sys.exit(1)
    
app = FastAPI(title="MRD-RAG Doctor Chatbot API", version="2.9")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Neo4jConnector:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        print(f"✓ Connected to Neo4j at {uri}")

    def search_entities(self, query_text):
        safe_props = ["name", "text", "description", "disease", "symptom", "title"]
        query_parts = [f"(n.{p} IS NOT NULL AND toLower(toString(n.{p})) CONTAINS toLower($query))" for p in safe_props]
        where_clause = " OR ".join(query_parts)
        cypher_query = f"""
            MATCH (n)
            WHERE {where_clause}
            RETURN n LIMIT 5
        """
        with self.driver.session() as session:
            result = session.run(cypher_query, {"query": query_text})
            records = result.values()
            context = "\n".join([
                json.dumps(r[0]._properties, indent=2)
                for r in records
            ])
            return context if context else "No relevant entities found."

class BiomedicalRAG:
    def __init__(self, api_key, model="command-a-03-2025"):
        self.cohere = cohere.Client(api_key)
        self.model = model
        try:
            _ = self.cohere.chat(model=self.model, message="Hello test")
            print(f"✓ Cohere Chat backend initialized with model '{self.model}'")
        except Exception:
            print(f"⚠️ Cohere model '{self.model}' failed. Trying fallback...")
            self.model = "command-r7b-12-2024"
            _ = self.cohere.chat(model=self.model, message="Hello test")
            print(f"✓ Using fallback model '{self.model}'")

    def _prompt(self, conversation, context):
        convo_text = "\n".join([
            f"Patient: {c['patient']}\nDoctor: {c.get('doctor', '')}" for c in conversation
        ])
        return f"""
You are a kind, logical, biomedical doctor chatbot.

PATIENT CONVERSATION HISTORY:
{convo_text}

KNOWLEDGE GRAPH CONTEXT:
{context}

TASK:

* Ask relevant follow-up questions.
* If enough info, give a diagnosis and short advice.
* Be concise, empathetic, and medically accurate.

YOUR RESPONSE:
"""

    def answer(self, conversation, context):
        try:
            response = self.cohere.chat(
                model=self.model,
                message=self._prompt(conversation, context),
                temperature=0.4
            )
            return response.text.strip()
        except Exception as e:
            return f"Error from Cohere API: {str(e)}"

class DoctorChatPipeline:
    def __init__(self, uri, user, password, api_key):
        self.neo4j = Neo4jConnector(uri, user, password)
        self.rag = BiomedicalRAG(api_key)
        print("✓ Doctor Chatbot Pipeline Ready")

pipeline_instance = DoctorChatPipeline(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD, COHERE_KEY)

@app.get("/")
def home():
    return {"message": "✅ MRD-RAG Doctor Chatbot Backend Running", "status": "ok"}

@app.post("/predict")
def predict(data: dict):
    user_message = data.get("message", "")
    conversation = data.get("conversation", [])
    if not user_message.strip():
        return {"error": "Please provide a valid message."}
    try:
        context = pipeline_instance.neo4j.search_entities(user_message)
        conversation.append({"patient": user_message})
        doctor_reply = pipeline_instance.rag.answer(conversation, context)
        conversation[-1]["doctor"] = doctor_reply
        return {
            "response": doctor_reply,
            "conversation": conversation,
            "context_preview": context[:400]
        }
    except Exception as e:
        return {"error": f"Internal server error: {str(e)}"}
