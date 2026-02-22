import json
import os

MEMORY_FILE = "memory/chat_memory.json"


# create file if not exists
def init_memory():
    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            json.dump([], f)


# load chat history
def load_memory():
    init_memory()
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


# save message
def save_message(role, content):
    history = load_memory()

    history.append({
        "role": role,
        "content": content
    })

    with open(MEMORY_FILE, "w") as f:
        json.dump(history, f, indent=4)


# clear memory
def clear_memory():
    with open(MEMORY_FILE, "w") as f:
        json.dump([], f)