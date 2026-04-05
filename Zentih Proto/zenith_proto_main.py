# zenith proto 1.5
from identity.memory.memory_handler import handle_memory
from identity.general_info.general_info import handle_identity
import speech_recognition as sr
from utils.speak import speak
from handlers.search_handler import handle_search
from handlers.open_handler import handle_open

activated = False

recognizer = sr.Recognizer()
recognizer.pause_threshold = 1

while True:
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio).lower()
        print("You said:", text)

        # Activation
        if not activated:
            if "ok zenith" in text:
                activated = True
                speak("Activated")
            continue
            # Memory Layer
        if handle_memory(text):
            continue

        # Identity Layer
        if handle_identity(text):
            continue

        # Search Layer
        if handle_search(text):
            continue

        # Open Layer
        if handle_open(text):
            continue

        # Other Commands
        if "sleep" in text:
            speak("Deactivating")
            activated = False

        elif "stop" in text:
            speak("Goodbye sir")
            break

        else:
            speak("Command not recognized")

    except Exception as e:
        print("Error:", e)