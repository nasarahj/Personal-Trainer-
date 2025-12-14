import json
from pathlib import Path as path

MEMORY_FILE = path(__file__).resolve().parents[1]/"users.json"

def load_memory(user_id: str) ->dict:
    if not MEMORY_FILE.exists():
        return {}
    with open(MEMORY_FILE, "r") as f:
        data = json.load(f)
    return data.get(user_id, {})

def save_memory(user_id: str, memory: dict):
    if MEMORY_FILE.exists():
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)
    else:
        data = {}
    data[user_id] = memory
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

