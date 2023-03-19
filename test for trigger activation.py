import speech_recognition as sr
import os
        
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print('listening.......')
        print('\nListening.......')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        # print('Recognizing.....')
        print("Recognizing........")
        query = r.recognize_google(audio, language= 'en-in')
        print(f'User said:{query}\n')

    except Exception as e:
        #print(e)
        print("Say that again please......")
        return "None"
    return query

def there_exist(terms,query):
    for i in terms:
        if i in query:
            return i



# Call listen_for_trigger function to wait for trigger phrase
while True:
    query = takeCommand()
    if there_exist(['hazelnut','hozelnut','nut','hejalnut','hejal','he is a nut'],query):
        os.system('python hazel1.py')

