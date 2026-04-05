from utils.speak import speak
import webbrowser

def google_search(query):
    query = query.strip().replace(" ", "+")
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def youtube_search(query):
    query = query.strip().replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

def handle_search(text):

    if "search" not in text:
        return False

    # YouTube search
    if "on youtube" in text or "on you tube" in text:
        query = text.split("search", 1)[1]
        query = query.replace("on youtube", "").replace("on you tube", "").strip()

        if query:
            speak(f"Searching YouTube for {query}")
            youtube_search(query)
        else:
            speak("What should I search on YouTube?")

        return True

    # Default Google search
    query = text.split("search", 1)[1].strip()

    if query:
        speak(f"Searching Google for {query}")
        google_search(query)
    else:
        speak("What should I search?")

    return True
