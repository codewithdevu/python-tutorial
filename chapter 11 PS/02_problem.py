import pyttsx3

class Animals:
    pass

class pets(Animals):
    pass

class dog(pets):
    def bark(engine):
        engine = pyttsx3.init()
        engine.say("bhoooww bhoowww")
        engine.runAndWait()

d = dog()
d.bark()