import os
import speech_recognition as sr
import pyttsx3
import pywhatkit 
import datetime
import wikipedia
import pyjokes
import webbrowser
import smtplib
import sys
from requests import get
listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate',120)
engine.setProperty('volume',7.0)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
 try:
    with sr.Microphone() as source:
        
        print("listening...")
        listener.adjust_for_ambient_noise(source,duration=1)
        audio2 = listener.listen(source)
        Mytext = listener.recognize_google(audio2)
        Mytext = Mytext.lower()

    #if 'alexa' in Mytext:
        #Mytext = Mytext.replace('alexa','')
        print(f'User said: {Mytext}')
 except Exception as e:
    return 'None'
 return Mytext


def wishMe():


   hour = int(datetime.datetime.now().hour)

   if hour>=0 and hour<12 :
     print('Good Morning Mam, How can I help you')
     talk('Good Morning Mam, How can I help you')
   
   elif hour>=12 and hour<18 :
     print('Good Afternoon Mam, How can I help you')
     talk('Good Afternoon Mam, How can I help you')

   else:
      print('Good Evening Mam, How can I help you')
      talk('Good Evening Mam, How can I help you')
'''
if 1:
    print('Hello Mam, How can I help you?')
    talk('Hello Mam, How can I help you?')
'''
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',465)
    server.ehlo()
    server.starttls()
    server.login('Your gmail id', 'Your Password')
    server.sendmail('Your gmail id', to, content)
    server.close()




#def run_alexa():
#Mytext = take_command()
       
if __name__ == "__main__":
      wishMe()
while True:
   
     Mytext = take_command()

     if 'play' in Mytext:
        # we use another variable use like..
        #song = Mytext.replace('play','')
        Mytext = Mytext.replace('play','')
        talk('playing'+ Mytext)
        pywhatkit.playonyt(Mytext)
    
     elif 'time' in Mytext:
        #time = datetime.datetime.now().strftime('%H:%M')
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is '+ time)
    
     elif 'open notepad' in Mytext:
        rpath = "C:/Users/dell/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Accessories/Notepad"
        os.startfile(rpath)
    
     elif 'close notepad' in Mytext:
        print('Closing Notepad')
        talk('Closing Notepad...')
        os.system('taskkill /f /im %windir%\system32\notepad.exe')

     elif 'open command prompt' in Mytext:
        cpath = 'C:/Users/dell/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Accessories/Command Prompt'
        os.startfile(cpath)

     elif 'music' in Mytext:
        
        mpath = 'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Windows Media Player'
        os.startfile(mpath)
        
        #music_dir = 'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Windows Media Player'
        #songs = os.listdir(music_dir)
        #rd = random.choice(song)
        #os.startfile(os.path.join(mpath,song))
        
     elif 'wikipedia' in Mytext:
        print('searching wikipedia...')
        talk('searching wikipedia...')
        person = Mytext.replace('wikipedia','')
        info = wikipedia.summary(person,'2')
        print('according to wikipedia')
        talk('according to wikipedia')
        print(info)
        talk(info)
     
     elif 'ip address' in Mytext:
        ip = get('https://api.ipify.org').text
        print(f'Your IP adress is {ip}')
        talk(f'Your IP adress is {ip}')
    
     elif 'joke' in Mytext:
        talk(pyjokes.get_joke())
    
     elif 'who are you' in Mytext:
        print('I am alexa.I am created by Sakshi Kumari.')
        talk('I am alexa.I am created by Sakshi Kumari')
    
     elif 'who created you' in Mytext:
        print('I am created by Sakshi Kumari.')
        talk('I am created by Sakshi Kumari')
    
     elif 'how are you' in Mytext:
        print('I am fine thank you for asking.')
        talk('I am fine.Thank you for asking.')
    
     elif 'open youtube' in Mytext:
        webbrowser.open('www.youtube.com')
    
     elif 'open facebook' in Mytext:
        webbrowser.open('www.facebook.com')
    
     elif 'open w3school' in Mytext:
        webbrowser.open('www.w3schools.com')
        
     elif 'open instagram' in Mytext:
        webbrowser.open('www.instagram.com')
    
     elif 'open github' in Mytext:
        webbrowser.open('www.github.com')
    
     elif 'open google' in Mytext:
        print('Mam, What should I search on google')
        talk('Mam, What should I search on google')
        cm = take_command().lower()
        webbrowser.open(f'{cm}')
    
     elif 'open ignou' in Mytext:
        webbrowser.open('ignou.ac.in') 
    
     elif 'send message' in Mytext:
        pywhatkit.sendwhatmsg('Enter your number','This is testing program',12,30)
    
     elif 'email to sakshi' in Mytext:
        try:
            print('What should I say')
            talk('What should I say')
            content = take_command().lower()
            to = 'Enter gmail id'
            sendEmail(to,content)
            talk('Email has been sent to Sakshi')
            talk('Email has been sent to Sakshi')
        except Exception as ae:
            print(ae)
            print('Sorry Mam, I am not able to sent this mail to Sakshi')
            talk('Sorry Mam, I am not able to sent this mail to Sakshi')

     elif 'exit' in Mytext:
        print('Thanks for using me Mam, have a good day')
        talk('Thanks for using me Mam, have a good day') 
        sys.exit()
    
     else:
      print('Mam, please say again')
      talk('Mam, please say again')


    
    
