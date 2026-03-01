# 🤖 AI Assistant Platform

A full-stack **AI Assistant Platform** built using **Streamlit, Local LLMs, RAG architecture, and Voice Interaction**, capable of conversational AI, document question answering, persistent memory, and speech-based interaction.

---

## 🚀 Live Demo

🌐 **Live App:**
`https://your-cloudflare-link.trycloudflare.com`

💻 **GitHub Repository:**
[https://github.com/MadhuH59/AI_Chatbot-local](https://github.com/MadhuH59/AI_Chatbot-local)

---

## 📌 Project Overview

This project implements a **ChatGPT-like AI assistant** running locally using Ollama LLMs and enhanced with Retrieval-Augmented Generation (RAG) for document understanding.

The assistant supports:

* Natural conversation
* PDF-based question answering
* Persistent chat memory
* Voice interaction
* Multi-modal AI workflow

---

## ✨ Features

✅ ChatGPT-style conversational interface
✅ Local LLM integration (Ollama – Llama3)
✅ Retrieval-Augmented Generation (RAG)
✅ PDF Question Answering system
✅ Vector database semantic search (FAISS)
✅ Persistent memory storage
✅ Voice input (Speech-to-Text)
✅ AI voice responses (Text-to-Speech)
✅ Streamlit web interface
🌐 Public Web Access via Cloudflare Tunnel

---

## 🧠 Architecture

```
User Input (Text / Voice)
        ↓
Streamlit UI
        ↓
Memory System
        ↓
RAG Pipeline (LangChain)
        ↓
FAISS Vector Database
        ↓
Local LLM (Ollama)
        ↓
AI Response + Voice Output
```

---

## 🛠️ Tech Stack

| Category           | Technology                        |
| ------------------ | --------------------------------- |
| Language           | Python                            |
| UI Framework       | Streamlit                         |
| LLM Runtime        | Ollama                            |
| Model              | Llama3                            |
| RAG Framework      | LangChain                         |
| Vector Database    | FAISS                             |
| Embeddings         | HuggingFace Sentence Transformers |
| Speech Recognition | SpeechRecognition                 |
| Text-to-Speech     | pyttsx3                           |
| Deployment         | Cloudflare Tunnel                 |

---

## 📂 Project Structure

```
AI_Chatbot-local/
│
├── app.py
├── utils/
│   ├── memory.py
│   ├── pdf_qa.py
│   ├── voice.py
│   └── __init__.py
│
├── data/
│   ├── uploads/
│   └── vector_db/
│
├── memory/
│   └── chat_memory.json
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository


```bash
git clone https://github.com/MadhuH59/AI_Chatbot-local.git
cd AI_Chatbot-local
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Ollama Model

```bash
ollama run llama3
```

---

### 5️⃣ Start Application

```bash
streamlit run app.py
```

Open:

```
http://localhost:8501
```

## ✅ Small Summary of **Streamlit**

**Streamlit** is a Python framework used to build **interactive web applications** directly from Python code.
It allows developers to create dashboards, AI apps, and chat interfaces **without using HTML, CSS, or JavaScript**.

👉 You write Python → Streamlit automatically creates a website and runs it in your browser.

**Key idea:**

> Streamlit converts Python scripts into web apps quickly and easily.


### 🧠 One-Line Understanding

**Streamlit = fastest way to turn Python programs into web apps.**

---

## 🌐 Public Deployment (Cloudflare Tunnel)

You can make the AI Assistant accessible online using **Cloudflare Tunnel**.

### 1️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

App runs locally at:

```
http://localhost:8501
```

---

### ✅ Step 2 — Download Cloudflare Tunnel

Download **cloudflared** from:

https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads/

Place `cloudflared.exe` inside a known folder (example: `c:/user/project`).

---

### 2️⃣ Start Cloudflare Tunnel

Open a new terminal and run:

```bash
cloudflared tunnel --url http://localhost:8501
```

---

### 3️⃣ Access Live App

Cloudflare generates a public URL like:

```
https://xxxx.trycloudflare.com
```
```
https://publication-quoted-committed-synthesis.trycloudflare.com/
```

Share this link to access the AI Assistant from anywhere.

⚠️ The link works only while both terminals are running.

---


## 📄 How RAG Works

1. Upload PDF document
2. Text is split into chunks
3. Embeddings generated using HuggingFace models
4. Stored in FAISS vector database
5. User query performs semantic similarity search
6. Retrieved context injected into LLM prompt
7. AI generates context-aware response

---

## 🎙️ Voice Assistant Workflow

```
Speech → Text → AI Processing → Response → Speech Output
```

---

## 📸 Screenshots(TBU)

* Chat Interface: 

* PDF QA
* Voice Interaction

---

## 🔮 Future Improvements

* Multi-model selection
* Wake-word detection ("Hey Jarvis")
* User authentication
* Cloud deployment (AWS/GCP)
* Database-backed memory
* Agent-based automation

---

## 👨‍💻 Author

**Madhu H**

📧 [madhuh0059@gmail.com](mailto:madhuh0059@gmail.com)
🔗 GitHub: [https://github.com/MadhuH59](https://github.com/MadhuH59)
🔗 Cloudfare: [https://publication-quoted-committed-synthesis.trycloudflare.com/](https://publication-quoted-committed-synthesis.trycloudflare.com/)
---

## ⭐ Resume Description

Built a full-stack AI Assistant Platform featuring conversational AI, Retrieval-Augmented Generation (RAG), PDF question answering, persistent memory, and voice interaction using Streamlit, LangChain, FAISS, and local LLMs and Public Web Access via Cloudflare Tunnel.

---



