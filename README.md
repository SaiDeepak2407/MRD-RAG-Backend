# 🧠 RAGnosis – AI Doctor Chatbot  

*AI-Powered Medical Diagnosis Assistant built with FastAPI, Neo4j, and Cohere*  

![RAGnosis Banner](https://img.shields.io/badge/AI%20Healthcare-RAGnosis-dc2626?style=for-the-badge&logo=python&logoColor=white)

---

## 🚀 Overview  

**RAGnosis** (Retrieval-Augmented Diagnosis) is an intelligent medical chatbot that helps users understand possible conditions based on symptoms.  
It combines **LLM reasoning** with **graph-based medical knowledge retrieval** for safe and context-aware responses.  

### 🔍 Powered by
- 🧠 **Cohere Command Models** — for biomedical natural-language understanding  
- 🧬 **Neo4j AuraDB** — for verified medical graph retrieval  
- ⚡ **FastAPI** — for lightweight, production-grade API hosting  

---

## ✨ Features  

✅ Conversational symptom-based diagnosis assistant  
✅ Context-aware follow-up questioning for higher accuracy  
✅ RAG pipeline: Neo4j + Cohere integration  
✅ Secure, scalable FastAPI backend  
✅ Deployed seamlessly on **Vercel** for global access  

---

## 🧩 Tech Stack  

| Layer          | Technology                              |
|----------------|------------------------------------------|
| **Frontend**   | HTML, CSS, JavaScript (Vanilla or React) |
| **Backend**    | FastAPI (Python)                         |
| **LLM API**    | Cohere (Command-R / Command-A)           |
| **Database**   | Neo4j AuraDB                             |
| **Deployment** | Vercel (Backend)                         |

---

## ⚙️ Setup Instructions  

###1️⃣ Clone the Repository  
bash
git clone https://github.com/yourusername/ragnosis-backend.git
cd ragnosis-backend

###2️⃣ Create and Activate a Virtual Environment
python -m venv venv
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate

###3️⃣ Install Dependencies
pip install -r requirements.txt

###4️⃣ Add Environment Variables
Create a .env file in the project root:

COHERE_KEY=your_cohere_api_key
NEO4J_URI=neo4j+s://your_database_uri
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_neo4j_password

🧠 Run Locally
uvicorn main:app --host 0.0.0.0 --port 8000
Then open your browser → http://127.0.0.1:8000/docs

You’ll see the interactive Swagger UI where you can test your chatbot.

🌐 Deployment on Vercel

1.Push your backend code to GitHub.

2.On Vercel, create a New Project and import your repo.

3.In the setup:

  Framework Preset: “Other”

  Build Command: pip install -r requirements.txt

  Output Directory: .

  Start Command: uvicorn main:app --host 0.0.0.0 --port 8000

4.Add environment variables under Settings → Environment Variables.

5.Deploy — your API will go live at:
  https://ragnosis.vercel.app

🔗 Frontend Integration

In your frontend script.js or .env file, update the backend endpoint:

const BACKEND_URL = "https://ragnosis.vercel.app";


Then call the API:

const response = await fetch(`${BACKEND_URL}/predict`, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    message: "I have a headache and nausea",
    conversation: []
  })
});

📬 API Endpoints
Method	Endpoint	Description
GET	/	Returns API status
POST	/predict	Accepts user message & conversation; returns chatbot reply
Example Request
{
  "message": "I have a headache and nausea",
  "conversation": []
}

Example Response
{
  "response": "Do you also have sensitivity to light or vomiting?",
  "conversation": [...],
  "context_preview": "..."
}

⚠️ Notes

RAGnosis is intended for educational and research purposes only.

It must not replace professional medical consultation.

Cohere and Neo4j credentials should always remain private.

👩‍💻 Contributor

Sai Deepak

📄 License

MIT License © 2025 RAGnosis Team
Feel free to use, modify, and extend for research or learning purposes.
