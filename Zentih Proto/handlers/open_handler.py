from utils.speak import speak
import webbrowser
import os
from config.websites import WEBSITES
from config.apps import APPS

def handle_open(text):

    # Website
    for name, url in WEBSITES.items():
        if f"open {name}" in text:
            speak(f"Opening {name}")
            webbrowser.open(url)
            return True

    # App
    for name, path in APPS.items():
        if f"open {name}" in text:
            speak(f"Opening {name}")
            os.startfile(path)
            return True

    return False
