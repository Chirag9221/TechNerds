from ctypes import POINTER, cast
import datetime
from email import message
from sqlite3 import Time
from time import time
from unittest import removeHandler
import pywhatkit
from http import server
from tkinter.messagebox import YES
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from email.message import EmailMessage
import screen_brightness_control as brightness
# from plyer import notification
import pyjokes
import camerafile
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import threading
import tkinter as tk
from tkinter import scrolledtext
from PIL import ImageTk, Image
from ttkthemes import themed_tk
import camerafile
import random


# devices = AudioUtilities.GetSR.speakers()
# interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL,None)
# volume = cast(interface,POINTER(IAudioEndpointVolume))

import cv2


# from asyncio.timeouts import timeout

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if 0<= hour <12:
        gm = ["Good morning Wishing you a day full of positivity and happiness",
            "Rise and shine May your day be filled with success and accomplishment",
            "Good morning my love I hope you have a wonderful day ahead",
            "Wake up, sleepyhead It's a new day full of opportunities and adventures",
            "Good morning Don't forget to smile and spread some happiness wherever you go today",
            "Rise and shine my friend! Let's conquer this day together",
            "Good morning May your coffee be hot and your day be productive",
            "Wake up and chase your dreams You've got this",
            "Good morning Remember to take a moment to appreciate the beauty around you today",
            "Rise and shine sunshine It's a brand new day full of possibilities"]
        SR.speak(random.choice(gm))
       
    elif 12<=hour<16:
        ga = [  "Good afternoon my friend I hope you're taking some time to relax and recharge",
                "Just a quick message to let you know that I'm thinking of you. Have a great afternoon",
                "It's the perfect time for a mid-day pick-me-up Enjoy your afternoon and have a great one",
                "Good afternoon and remember to take a deep breath and enjoy the moment",
                "Hey there! Hope your afternoon is going as smoothly as possible"]
        SR.speak(random.choice(ga))
       
    elif 16<= hour < 20:
        ge = ["Good evening Wishing you a relaxing and peaceful evening after a busy day",
                "Hope your day was productive and fulfilling Have a wonderful evening ahead",
                "As the sun sets may all your worries and stress fade away Have a good evening",
                "Sending positive vibes your way for a great evening Take some time to unwind and enjoy",
                "May your evening be as beautiful as you are Good evening",
                "Evenings are a reminder that you survived another day Cheers to that Have a good evening"]
        SR.speak(random.choice(ge))
    else:
        SR.speak('I hope my master had a great day')
   
    SR.speak('Hey! i am Hazel . please tell me what can i do for you?')


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('emailbot74@gmail.com', 'jyfxghehyvkgcfky')
    email = EmailMessage()
    email['From'] = 'emailbot74@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

email_list = {
    'hello':'chiragg9221@gmail.com',
    'world' : 'baitalsneha@gmail.com',
    'tree' : 'taruniyer08@gmail.com',
    'none' : 'salonikharat1234@gmail.com'
}

whatsapp_list={
    'hello':'+919967208612'
}

# def reminder(title1,mssge1):
#     time1 = 5 * 60
#     if __name__ == "__main__":
#         notification.notify(
#             title = title1,
#             message = mssge1,
#             app_icon = "hazellogo.ico",
#             app_name = "Hazel",
#             timeout = 500
#         )
#         SR.speak(mssge1)
        



def get_email_info():
    SR.speak('To Whom you want to send email')
    name = SR.takeCommand()
    receiver = email_list[name]
    SR.updating_ST(receiver)
    SR.speak('What is the subject of your email?')
    subject = SR.takeCommand()
    SR.speak('Tell me the text in your email')
    message = SR.takeCommand()
    send_email(receiver, subject, message)
    # SR.speak('Hey lazy ass. Your email is sent')
    SR.speak('Do you want to send more email?')
    send_more = SR.takeCommand()
    if 'yes' in send_more:
        get_email_info()

def get_whatsapp_info():
    SR.speak("TO whom to do you want to whatsapp")
    wname = SR.takeCommand()
    wreceiver = whatsapp_list[wname] 
    SR.speak("What is the message")
    wmssge = SR.takeCommand()
    htime = datetime.datetime.now().hour
    mtime = datetime.datetime.now().minute
    pywhatkit.sendwhatmsg(wreceiver,wmssge,htime,mtime+1)
    SR.speak("Do you want to send more messages")
    ans = SR.takeCommand()
    if 'yes' in ans:
        get_whatsapp_info()

def query_exist(terms,query):
    for term in terms:
        if term in query:
            return True


def mainframe():
    SR.scrollable_text_clearing()

    WishMe()
    while True:
            query = SR.takeCommand().lower()

            #logic to perform various task
            if query_exist(['search wikipedia for','from wikipedia'],query):
                SR.speak("Searching wikipedia...")
                if 'search wikipedia for' in query:
                    query=query.replace('search wikipedia for','')
                    results=wikipedia.summary(query,sentences=2)
                    SR.speak("According to wikipedia:\n")
                    SR.speak(results)
                elif 'from wikipedia' in query:
                    query=query.replace('from wikipedia','')
                    results=wikipedia.summary(query,sentences=2)
                    SR.speak("According to wikipedia:\n")
                    SR.speak(results)
            elif query_exist(['wikipedia'],query):
                SR.speak("Searching wikipedia....")
                query=query.replace("wikipedia","")
                results=wikipedia.summary(query,sentences=2)
                SR.speak("According to wikipedia:\n")
                SR.speak(results)

        
            elif query_exist(['hey','hello','hola','namaste','whatsup','hii'],query) :
                SR.speak("Hey I am Hazel A virtual Assistant ")  
                SR.speak('How are you')
        
            elif query_exist(['i am fine','i am well','i am good','i am alright','how are you','what about you'],query):
                SR.speak("Thats Great")
                SR.speak('you know i was developed by my masters')
                SR.speak('and they keep me fine')
            
            elif query_exist(['who developed you','who developed','who made you','when were u developed','who are your developers','who are your parents','who is your developer','who is your father','how many people have developed you'],query):
                SR.speak("I was developed by a group of 3 people")
                SR.speak("Taarun")
                SR.speak('SNEHA')
                SR.speak('and My favourite Chirag')
            
            # elif query_exist(['change volume','decrease the volume','iincrease the volume','volume','pc volume','lower volume','lower the volume','higher the volume','high volume','low volume'],query):
            #     volume.SetMasterVolumeLevel(-45,None)
            
            elif query_exist(['crack a joke','joke','make me laugh','tell me joke','tell me a joke','make me happy','make my day'],query):
                SR.speak(pyjokes.get_joke(language='en',category='all'))
                future_query = SR.takeCommand()
                if query_exist(['crack another joke','one more','one more please','tell me more','i would like to hear more of them','more','once more','once again','again'],future_query) and (future_query is not None):
                    SR.speak(pyjokes.get_joke(language='en',category='all'))
                
            elif query_exist(['send mail','mail','write a mail','email','draft a mail','draft mail'],query):
                get_email_info()
            
            elif query_exist(['whatsapp','send messages','send messages by whatsapp'],query):
                get_whatsapp_info()
            
            elif query_exist(['change the brightness',"change brightness",'manipulate brightness','brightness of the pc','increase brightness','decrease the brightness'],query):
                SR.speak("what should be the value for brightness")
                SR.speak("Select in the range of 1 to 5")
                value = SR.takeCommand().lower()
                if 'one' in value:
                    brightness.set_brightness(20)
                    SR.speak("Brightness set to 20")
                elif 'two ' in value :
                    brightness.set_brightness(40)
                    SR.speak("Brightness set to 40")
                elif 'tu' in value:
                    SR.speak("Brightness set to 40")
                    brightness.set_brightness(40)

                elif 'three' in value :
                    brightness.set_brightness(60)
                    SR.speak("Brightness set to 60")
                elif 'tree' in value :
                    brightness.set_brightness(60)
                    SR.speak("Brightness set to 60")
                elif 'free' in value:
                    brightness.set_brightness(60)
                    SR.speak("Brightness set to 60")
            
                elif 'four' in value:
                    brightness.set_brightness(80)
                    SR.speak("Brightness set to 80")
                elif 'ford' in value:
                    brightness.set_brightness(80)
                    SR.speak("Brightness set to 80")
                elif 'fi' in value:
                    brightness.set_brightness(100)
                    SR.speak('brightness set to 100')
                
                elif 'five' in value:
                    brightness.set_brightness(100)
                    SR.speak('brightness set to 100')
                else:
                    brightness.set_brightness(100)
                    SR.speak('brightness set to 100')

            elif query_exist(['make a note','take note','take a note','note it down','make note','remember this as note','open notepad and write'],query):
                SR.speak("What would you like to write down?")
                data=SR.takeCommand()
                n=camerafile.note()
                n.Note(data)
                SR.speak("I have a made a note of that.")
                

            elif query_exist(['search','i want to search','can you search','open search'],query):
                SR.speak("What do you want search??")
                search = SR.takeCommand()
                url = 'https://google.com/search?q=' + search
                webbrowser.get().open_new_tab(url)
                SR.speak('Here is what i found' + search)
            
            elif query_exist(['open chrome','chrome'],query):
                webbrowser.open_new_tab('chrome.com')
            
            elif query_exist(["what is your name","what's your name","tell me your name",'who are you'],query):
                SR.speak("My name is Hazel and I'm here to serve you.")
        
            elif query_exist(['open youtube','yt','open yt','search youtube',"youtube"],query):
                webbrowser.open_new_tab('www.youtube.com')    
    
            elif query_exist(['play music','hazel play music','open music','play songs','song','open songs'],query):
                SR.speak("Which should i play for you master")
                search = SR.takeCommand()
                pywhatkit.playonyt(search)

            elif query_exist(['take screenshot','take a screenshot','screenshot please','capture my screen'],query):
                SR.speak("Taking screenshot")
                SS=camerafile.screenshot()
                SS.takeSS()
                SR.speak('Captured screenshot is saved in Screenshots folder.')
                del SS

            # elif 'open youtube' in query:
            #     webbrowser.open("youtube.com")
            
            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open facebook' in query:
                webbrowser.open("facebook.com")

            elif 'open instagram' in query:
                webbrowser.open("instagram.com")

            elif query_exist(['what is the time','what is time','time','time in date hour second format','what is the hour now','what is the time in the clock','clock'],query):
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                SR.speak(f"sir, the time is {strTime}")
            
            elif query_exist(["what is my exact location","What is my location","location",'my location',"my current location","exact current location"],query):
                    url = "https://www.google.com/maps/search/Where+am+I+?/"
                    webbrowser.get().open_new_tab(url)
                    SR.speak("Showing your current location on google maps...")
        
            elif query_exist(['take a photo','take a selfie','take my photo','take photo','take selfie','one photo please','click a photo'],query):
                    takephoto = camerafile.camera()
                    Location= takephoto.takePhoto()
                    os.startfile(Location)
                    del takephoto
                    SR.speak("Captured picture is stored in Camera folder.")
            
            elif query_exist(['open cmd','cmd','open command prompt','open command','command prompt'],query):
                os.startfile("C:\\Users\\nares\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk")

            elif query_exist(['open vs code','code','ide','open visual code','open editor','open programming editor','vs code'],query):
                visualstudio_path = "C:\\Users\\nares\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
                os.startfile(visualstudio_path)
            
            elif query_exist(['open file manager','open files','open mypc','mypc','files'],query):
                os.startfile('C:\\')

            elif query_exist(['calculator','open calculator','calci','open calci'],query):
                webbrowser.open_new_tab('https://www.google.com/search?q=calculator&rlz=1C1CHBF_enIN976IN976&oq=calcul&aqs=chrome.1.69i57j0i271l3.2996j0j7&sourceid=chrome&ie=UTF-8')

            elif query_exist(['open news','i want to read news','news','todays headline','whats todays world update','world update','any new news','headlines of the day','headlines'],query):
                webbrowser.open_new_tab('https://timesofindia.indiatimes.com/')

            elif 'open news ' in query:
                webbrowser.open('https://timesofindia.indiatimes.com/')

            elif 'open amazon' in query:
                webbrowser.open('amazon.com')
    
            elif 'open flipkart' in query:
                webbrowser.open('flipkart.com')

            elif query_exist(['thank you',"thankyou",'shutup','exit','bye','bubye','see you','leave','you work is done','time to leave','fuckoff'],query):
                SR.speak("I hope you enjoyed my service You can call me whenever you need me")
                exit()
            


def CommandsList():
    os.startfile('Commands List.txt')

def clearScreen():
    SR.scrollable_text_clearing()


def gen(n):
    for i in range(n):
        yield i

class MainframeThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        mainframe()
       
def Launching_thread():
    Thread_ID=gen(1000)
    global MainframeThread_object
    MainframeThread_object=MainframeThread(Thread_ID.__next__(),"Mainframe")
    MainframeThread_object.start()
   
if __name__=="__main__":
        #tkinter code
        root=themed_tk.ThemedTk()
        root.set_theme("winnative")
        root.geometry("{}x{}+{}+{}".format(913,460,int(root.winfo_screenwidth()/2 - 913/2),int(root.winfo_screenheight()/2 - 460/2)))
        root.resizable(0,0)
        root.title("Hazel")
        root.iconbitmap('hazellogo2.ico')
        root.configure(bg='#14B0BF')
        scrollable_text=scrolledtext.ScrolledText(root,state='disabled',height=15,width=87,relief='sunken',bd=9,wrap=tk.WORD,bg='#FDC00F',fg='#000000')
        scrollable_text.place(x=0,y=0)
        mic_img=Image.open("mic4.png")
        mic_img=mic_img.resize((90,90),Image.ANTIALIAS)
        mic_img=ImageTk.PhotoImage(mic_img)
        SR = camerafile.SpeakRecog(scrollable_text)    #Speak and Recognition class instance
        Listen_Button=tk.Button(root,image=mic_img,borderwidth=0,activebackground='#14B0BF',bg='#14B0BF',command=Launching_thread)
        Listen_Button.place(x=410,y=330)
        myMenu=tk.Menu(root)
        m1=tk.Menu(myMenu,tearoff=0) #tearoff=0 means the submenu can't be teared of from the window
        m1.add_command(label='Commands List',command=CommandsList)
        myMenu.add_cascade(label="Help",menu=m1)
        myMenu.add_cascade(label="Clear Screen",command=clearScreen)
        root.config(menu=myMenu)
        root.mainloop()




    

    
        
            
            
            




