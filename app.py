import streamlit as st
import ollama
import os

from utils.memory import load_memory, save_message, clear_memory
from utils.pdf_qa import process_pdf, search_pdf
from utils.voice import listen, speak


# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Assistant Platform", layout="wide")

st.title("🤖 AI Assistant Platform")


# ---------------- SIDEBAR ----------------
st.sidebar.header("Controls")

# Clear memory
if st.sidebar.button("Clear Chat Memory"):
    clear_memory()
    st.rerun()


# -------- PDF Upload (RAG) --------
st.sidebar.subheader("📄 PDF Question Answering")

uploaded_file = st.sidebar.file_uploader(
    "Upload PDF",
    type="pdf"
)

if uploaded_file:
    os.makedirs("data/uploads", exist_ok=True)

    save_path = f"data/uploads/{uploaded_file.name}"

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("Processing PDF..."):
        process_pdf(save_path)

    st.sidebar.success("✅ PDF Ready for Questions")


# -------- Voice Assistant --------
st.sidebar.subheader("🎙️ Voice Assistant")

voice_prompt = None

if st.sidebar.button("Speak to AI"):
    voice_prompt = listen()
    st.sidebar.write(f"You said: {voice_prompt}")


# ---------------- LOAD CHAT HISTORY ----------------
messages = load_memory()

for msg in messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


# ---------------- USER INPUT ----------------
text_prompt = st.chat_input("Ask something...")

# choose voice OR typed input
prompt = voice_prompt if voice_prompt else text_prompt


# ---------------- AI RESPONSE ----------------
if prompt:

    # show user message
    with st.chat_message("user"):
        st.write(prompt)

    save_message("user", prompt)

    # 🔎 RAG: search PDF context
    pdf_context = search_pdf(prompt)

    system_prompt = f"""
You are a helpful AI assistant.

Use the provided context if relevant to answer the question.

Context:
{pdf_context}
"""

    # combine system prompt + memory
    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": system_prompt},
            *load_memory()
        ]
    )

    reply = response["message"]["content"]

    # show assistant message
    with st.chat_message("assistant"):
        st.write(reply)

    save_message("assistant", reply)

    # 🔊 Speak response
    speak(reply)