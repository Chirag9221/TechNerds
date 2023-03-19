import sqlite3
import pyttsx3
import cv2
import os
import playsound
import datetime
import hazel1
import speech_recognition as sr
import datetime,subprocess,pyautogui
class camera:
    def takePhoto(self):
        self.videoCaptureObject = cv2.VideoCapture(0)
        self.result = True
        a=os.getcwd()
        if not os.path.exists("Camera"):
            os.mkdir("Camera")
        os.chdir(a+'\Camera')
        self.ImageName="Image-"+str(datetime.datetime.now()).replace(':','-')+".jpg"
        while(self.result):
            self.ret,self.frame = self.videoCaptureObject.read()
            cv2.imwrite(self.ImageName,self.frame)
            self.result = False
        self.videoCaptureObject.release()
        cv2.destroyAllWindows()
        os.chdir(a)
        playsound.playsound("camera-shutter-click.mp3")
        # reqd_img_path = 'C:\\Users\\Sneha\\Hazel\\Camera\\'
        # os.open(reqd_img_path+self.ImageName)
        return "Camera\\"+self.ImageName
    
class note:
    def Note(self,data):
        date=datetime.datetime.now()
        filename=str(date).replace(':','-')+'-note.txt'
        a=os.getcwd()
        if not os.path.exists('Notes'):
            os.mkdir('Notes')
        os.chdir(a+r'\Notes')
        with open(filename,'w') as f:
            f.write(data)
        subprocess.Popen(['notepad.exe',filename])
        os.chdir(a)

class screenshot:
    def takeSS(self):
        img_captured=pyautogui.screenshot()
        a=os.getcwd()
        if not os.path.exists("Screenshots"):
            os.mkdir("Screenshots")
        os.chdir(a+'\Screenshots')
        ImageName='screenshot-'+str(datetime.datetime.now()).replace(':','-')+'.png'
        img_captured.save(ImageName)
        os.startfile(ImageName)
        os.chdir(a)

class SpeakRecog:
    def __init__(self,scrollable_text):
        self.scrollable_text=scrollable_text

    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    # print(voices[].id)
    # print(voices)

    """ VOICE RATE"""
    rate = engine.getProperty('rate')               # getting details of current speaking rate
    # print(rate)
    # engine.setProperty('rate',mycursor.execute('select rate from speech_rate').fetchone()[0])                 # setting up new voice rate in words per minute

    """VOLUME"""  
    volume = engine.getProperty('volume')           #getting to know current volume level (min=0 and max=1)
    # print(volume)                                 #printing current volume level
    scrollable_text=None
    def STS(self,scrollable_text):
        '''This is scrollable text setter '''
        self.scrollable_text=scrollable_text
    def updating_ST(self,data):
        self.scrollable_text.configure(state='normal')
        self.scrollable_text.insert('end',data+'\n')
        self.scrollable_text.configure(state='disabled')
        self.scrollable_text.see('end')
        self.scrollable_text.update()
    def updating_ST_No_newline(self,data):
        self.scrollable_text.configure(state='normal')
        self.scrollable_text.insert('end',data)
        self.scrollable_text.configure(state='disabled')
        self.scrollable_text.see('end')
        self.scrollable_text.update()
    def scrollable_text_clearing(self):
        self.scrollable_text.configure(state='normal')
        self.scrollable_text.delete(1.0,'end')
        self.scrollable_text.configure(state='disabled')
        self.scrollable_text.update()
    def speak(self,audio):
        """It speaks the audio"""
        self.updating_ST(audio)
        self.engine.say(audio)
        # engine.save_to_file('Hello World', 'test.mp3')
        self.engine.runAndWait()
        # engine.stop()
       
    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            # print('listening.......')
            self.updating_ST('\nListening.......')
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            # print('Recognizing.....')
            self.updating_ST("Recognizing........")
            query = r.recognize_google(audio, language= 'en-in')
            self.updating_ST(f'User said:{query}\n')

        except Exception as e:
            #print(e)
            self.updating_ST("Say that again please......")
            return "None"
        return query

    def nonPrintSpeak(self,audio):
        self.engine.say(audio)
        self.engine.runAndWait()

