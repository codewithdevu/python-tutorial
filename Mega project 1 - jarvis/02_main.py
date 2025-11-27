import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Male voice
engine.setProperty('rate', 175)  # Faster speaking rate (default ~200)

newsapi = "7b1ebff42edb444daee2d2855de0675f"

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in c:
        webbrowser.open("https://instagram.com")
    elif c.startswith("play"):
        parts = c.split(" ", 1)
        if len(parts) > 1:
            song = parts[1]
            link = musicLibrary.music.get(song, None)
            if link:
                webbrowser.open(link)
            else:
                speak("Sorry, I couldn't find that song.")
        else:
            speak("Please tell me which song to play.")
    elif "news" in c:
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}", timeout=3)
            if r.status_code == 200:
                data = r.json()
                articles = data.get('articles', [])
                if articles:
                    for article in articles[:5]:
                        speak(article.get('title', 'No title'))
                else:
                    speak("No news articles found.")
            else:
                speak("News API returned an error.")
        except:
            speak("Failed to fetch news. Check internet.")
    elif "exit" in c or "stop" in c:
        speak("Goodbye, Divyansh.")
        exit()
    else:
        speak("Sorry, I don't understand that command.")

if __name__ == "__main__":
    speak("Activating Jarvis...")

    # Adjust ambient noise once
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

    while True:
        try:
            print("Listening for name ...")
            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
            word = recognizer.recognize_google(audio)
           
            if "jarvis" in word.lower():
                speak("Yes Divyansh")
                print("Listening for command...")
                with sr.Microphone() as source:
                    audio = recognizer.listen(source, timeout=1, phrase_time_limit=5)
                command = recognizer.recognize_google(audio)
                print("Command:", command)
                processcommand(command)

        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
        except sr.RequestError:
            speak("Could not request results. Check internet connection.")
        except Exception as e:
            print(f"Error: {e}")
