import pyaudio
import speech_recognition as sr
import pyttsx3
import datetime

# pyttsx3.get
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 180)
print(voices[2].id)
engine.setProperty('voice',voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    if 0<= hour <12:
        speak("Good Morning")
    elif 12<=hour<16:
        speak("Good Afternoon")
    elif 16<= hour < 20:
        speak("Good Evening ")
    else:
        speak('I hope my master had a great day')
    
    speak('Hey! i am Hazel . please tell me what can i do for you?')

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print('listening.......')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing.....')
        query = r.recognize_google(audio, language= 'en-in')
        print(f'User said:{query}\n')

    except Exception as e:
        #print(e)
        print("say that again please......")
        return "None"
    return query

wishme()
