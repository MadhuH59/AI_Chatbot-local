# 🤖 AI Chatbot (Local ChatGPT Clone)

A ChatGPT-style AI chatbot running locally using **Ollama + Streamlit**.

---

## 🚀 Features

* Local AI model (No API key required)
* ChatGPT-like interface
* Runs completely on your computer
* Private & offline capable

---

## 🧰 Technologies Used

* Python 3.12
* Streamlit
* Ollama
* Llama3 / Mistral LLM

---

## 📦 Project Setup (SOP)

Follow these steps to run the project locally.

### 1️⃣ Clone Repository

```bash
git clone https://github.com/MadhuH59/AI_Chatbot-local.git
cd AI_Chatbot-local
```

---

### 2️⃣ Create Virtual Environment

```bash
py -3.12 -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Install Ollama

Download from:

https://ollama.com/download

Verify installation:

```bash
ollama --version
```

---

### 5️⃣ Download AI Model

```bash
ollama pull llama3
```

(or)

```bash
ollama pull mistral
```

---

### 6️⃣ Run Application

```bash
streamlit run app.py
```

Open browser:

```
http://localhost:8501
```

---

## 📁 Project Structure

```
AI_Chatbot-local/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 👨‍💻 Author

Madhu H
GitHub: https://github.com/MadhuH59

---

## ⭐ Future Improvements

* Chat memory storage
* Voice assistant
* PDF question answering
* Online deployment
