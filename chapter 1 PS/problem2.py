import pyttsx3

engine = pyttsx3.init()
engine.say(input("what do you want to speak : "))
engine.runAndWait()