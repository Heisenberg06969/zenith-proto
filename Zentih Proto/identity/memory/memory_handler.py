import json
import os
from utils.speak import speak

MEMORY_FILE = "memory/memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)


def handle_memory(text):
    memory = load_memory()

    # SAVE
    if "my " in text and " is " in text:
        try:
            parts = text.split(" is ", 1)

            key_part = parts[0]
            value = parts[1].strip()

            key = key_part.split("my ", 1)[1].strip()

            memory[key] = value
            save_memory(memory)

            speak(f"I have updated your {key}.")
            return True
        except:
            pass

    # RECALL
    if "what is my " in text:
        key = text.split("what is my ", 1)[1].strip()

        if key in memory:
            speak(f"Your {key} is {memory[key]}.")
        else:
            speak(f"I do not have information about your {key}.")

        return True

    return False

