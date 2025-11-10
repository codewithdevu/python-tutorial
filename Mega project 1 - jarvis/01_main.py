import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
# engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male

newsapi = "7b1ebff42edb444daee2d2855de0675f"

def speak(text):
    engine.say(text)
    engine.runAndWait() 

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():  
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ", 1)[1]  # Use split with limit to avoid errors
        link = musicLibrary.music.get(song, None)
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find that song.")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles[:5]:  # Limit output to 5 articles
                speak(article['title'])
        else:
            speak("No articles found.")

if __name__ == "__main__":
    speak("Activating Jarvis....")
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for name...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
                
            word = recognizer.recognize_google(audio)
            if "jarvis" in word.lower():
                speak("Yes Divyansh")
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = recognizer.listen(source, phrase_time_limit=6)
                    command = recognizer.recognize_google(audio)
                    recognizer.adjust_for_ambient_noise(source, duration=1) 
                    processcommand(command)
        
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Could not request results. Check internet connection.")
        except Exception as e:
            print(f"Error: {e}")