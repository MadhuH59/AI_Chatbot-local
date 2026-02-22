import streamlit as st
import ollama
from utils.memory import load_memory, save_message, clear_memory

st.set_page_config(page_title="AI Assistant", layout="wide")

st.title("🤖 AI Assistant Platform")

# Sidebar
if st.sidebar.button("Clear Memory"):
    clear_memory()
    st.rerun()

# Load chat history
messages = load_memory()

# Display history
for msg in messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
prompt = st.chat_input("Ask something...")

if prompt:
    # show user message
    with st.chat_message("user"):
        st.write(prompt)

    save_message("user", prompt)

    # AI response
    response = ollama.chat(
        model="llama3",
        messages=load_memory()
    )

    reply = response["message"]["content"]

    with st.chat_message("assistant"):
        st.write(reply)

    save_message("assistant", reply)