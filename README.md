# 🩺 MRD-RAG Doctor Chatbot

*AI-Powered Medical Diagnosis Assistant using Neo4j + Cohere + FastAPI*

![MRD-RAG Banner](https://img.shields.io/badge/AI%20Healthcare-MRD-RAG-dc2626?style=for-the-badge\&logo=python\&logoColor=white)

---

## 🚀 Overview

**MRD-RAG Smart Diagnosis** is an intelligent healthcare chatbot that uses **Retrieval-Augmented Generation (RAG)** to assist users in understanding potential medical conditions based on their symptoms.

It combines:

* 🧠 **Cohere LLMs** — for biomedical natural language understanding
* 🧬 **Neo4j Graph Database** — for retrieving verified medical knowledge
* ⚡ **FastAPI** — for a lightweight, fast backend service

---

## 🧩 Features

✅ Conversational medical diagnosis assistant
✅ Follow-up questioning for better accuracy
✅ Real-time inference via Cohere
✅ Secure connection to Neo4j medical graph
✅ Deployed using **Render** for 24×7 access

---

## 🗂️ Tech Stack

| Layer          | Technology                           |
| -------------- | ------------------------------------ |
| **Frontend**   | HTML, CSS, JavaScript                |
| **Backend**    | FastAPI (Python)                     |
| **LLM API**    | Cohere (Command-R / Command-A)       |
| **Database**   | Neo4j AuraDB                         |
| **Deployment** | Render (Backend), Netlify (Frontend) |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/mrd_rag_backend.git
cd mrd_rag_backend
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add environment variables

Create a `.env` file or use Render’s dashboard:

```
COHERE_KEY=your_cohere_api_key
NEO4J_URI=neo4j+s://your_database_uri
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_neo4j_password
```

---

## 🧠 Run Locally

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Open your browser → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
You’ll see an interactive Swagger UI where you can test your chatbot.

---

## 🌐 Deploy on Render

1. Push your backend to GitHub
2. Create a **new Web Service** on [Render](https://render.com)
3. Connect the repo and use these settings:

   * **Build Command:** `pip install -r requirements.txt`
   * **Start Command:** `uvicorn main:app --host 0.0.0.0 --port 10000`
4. Add environment variables in Render’s dashboard
5. After a few minutes, your API will be live 🎉

Example URL:

```
https://mrd-rag.onrender.com
```

---

## 🔗 Frontend Integration

In your `script.js`, update the backend endpoint:

```js
const BACKEND_URL = "https://mrd-rag.onrender.com";
```

Now your website can interact directly with the deployed FastAPI backend.

---

## 📬 API Endpoints

| Method   | Endpoint   | Description                                                  |
| -------- | ---------- | ------------------------------------------------------------ |
| **GET**  | `/`        | Returns backend status                                       |
| **POST** | `/predict` | Accepts user message and conversation, returns chatbot reply |

### Example Request:

```json
{
  "message": "I have a headache and nausea",
  "conversation": []
}
```

### Example Response:

```json
{
  "response": "Do you also have sensitivity to light or vomiting?",
  "conversation": [...],
  "context_preview": "..."
}
```

---

## 🛡️ Notes

* MRD-RAG is designed for **educational and research use** only.
* It should **not** replace professional medical consultation.
* Cohere and Neo4j credentials must remain **private**.

---

## 👩‍💻 Contributors

**Sai Deepak** – Project Lead & Developer

---

## 📄 License

MIT License © 2025 MRD-RAG Team
Feel free to modify and build upon this project for learning or research.

---
