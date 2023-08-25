from calendar import mon
from email.mime import audio
from mmap import PAGESIZE
from sqlite3 import Time
from unittest import result
from jmespath import search
import pyttsx3
import datetime
import speech_recognition as sr
import smtplib
from secrets import senderemail,epwd,to
import pyautogui
import webbrowser as web
# from time import sleep
import pywhatkit
import wikipedia
import requests,json
from newsapi import NewsApiClient
import clipboard
import os
import pyjokes
import time as tt
import string
import random
# from nltk.tokenize import word_tokenize
# import psutil

engine=pyttsx3.init()

def getvoices(voice):
    voices = engine.getProperty('voices') 
    if voice==1:     
        engine.setProperty('voice', voices[0].id)
        # speak("hello this is jarvis")

    if voice==2:
        engine.setProperty('voice', voices[1].id)
        # speak("hello this is friday")
    

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def time():
    Time= datetime.datetime.now().strftime("%I:%M:%S")
    speak("The Current time is")
    speak(Time)

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak('todays date is')
    speak(date)
    speak(month)
    speak(year)

def greeting():
    hour=datetime.datetime.now().hour
    if 6<=hour<12:
        speak("good morning!")
    elif 12<=hour<18:
        speak("good afternoon!")
    elif 18<=hour<24:
        speak("good evening!")
    else:
        speak("good night!")
# while True:
#     voice=int(input('Enter voice:'))
#     getvoices(voice)
    # audio=input("Enter the text:")
    # speak(audio)

def wishme():
    speak("Welcome back sir!")
    time()
    date()
    greeting()
    speak("jarvis at your service, what can i do for you ?")

# wishme()

def searchgoogle():
    speak('what should i search for you ?')
    search=takeCommandMic()
    web.open('https://www.google.com/search?q='+search)

def news():
    speak('what news you want to hear ?')
    topic=takeCommandMic()
    newsapi=NewsApiClient(api_key='885fc1fdabd34dd992b808dd9f72b00d')
    data=newsapi.get_top_headlines(q=topic,language='en',page_size=5)
    
    newsdata=data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak(f'{x}{y["description"]}')

def text2speech():
    text=clipboard.paste()
    print(text)
    speak(text)

def screenshot():
    name_img=tt.time()
    name_img='C:\\Users\\Rapid\\Desktop\\Jarvis\\screenshots\\{}.png'.format(name_img)
    img=pyautogui.screenshot(name_img)
    img.show()

def passwordgen():
    s1=string.ascii_uppercase
    s2=string.ascii_lowercase
    s3=string.digits
    s4=string.punctuation

    passlen=8
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    newpass=("".join(s[0:passlen]))
    print(newpass)
    speak(newpass)

def flip():
    speak("okay sir ,flipping a coin")
    coin=['heads','tails']
    toss=[]
    toss.extend(coin)
    random.shuffle(toss)
    toss=(''.join(toss[0]))
    speak('i flipped the coin and you get'+toss)

def roll():
    speak("okay sir ,rolling a die")
    die=['1','2','3','4','5','6']
    roll=[]
    roll.extend(die)
    random.shuffle(roll)
    roll=(''.join(roll[0]))
    speak('i rolled the dice and you get'+roll)
    

def takeCommandCMD():
    query=input("what can i do for you ?")
    return query

def takeCommandMic():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio ,language="en-IN")
        print(query)
        return query
    except Exception as e:
        print(e)
        speak('say that Again please...')
        return "None"



# def sendEmail():
#     server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
#     server.login(senderemail,epwd)
        
#     print("successful")
#     server.sendmail(senderemail,to,"Your order is placed succesfully")
#     server.quit()

# sendEmail()

#https://home.openweathermap.org/data/2.5/weather?q={City Name}&units=imperial&appid={API keys}

if __name__=="__main__":
    getvoices(2)
    url1 = "https://mp4-b.udemycdn.com/2021-02-04_14-18-50-1a16dd897b07f1a69ab396939c74b2f9/1/WebHD_720p.mp4?secure=pYlqdVDUZk1rnE-zT73Rbg%3D%3D%2C1657197454"
    web.open(url1)
    tt.sleep(13)

    os.system("taskkill /im firefox.exe /f")
    os.system("taskkill /im chrome.exe /f")
    
    url2="https://mp4-b.udemycdn.com/2021-02-04_14-18-48-3c195dbf5ee1fadbb1c9b9254fee744a/1/WebHD_720p.mp4?secure=O0rlFFmDP7qe4gv3YkAIsQ%3D%3D%2C1657196847"
    web.open(url2)
    tt.sleep(33)

    os.system("taskkill /im firefox.exe /f")
    os.system("taskkill /im chrome.exe /f")
    speak('what can i do for you sir')
    # wishme()
    wakeword='Jarvis'
    wakeword2='jarvis'
    while True:
        quer= takeCommandMic()
        # quer=word_tokenize(quer)
        
        getvoices(2)
        
        if 'time' in quer:
            time()
        elif 'date' in quer:
            date()
        elif 'message' in quer:
            user_name={
                    'mummy':'+91 99999 00000',
                    'dad':'+91 22222 33333'
                }

            try:
                speak("to whom do you want to send the whats app message?")
                name=takeCommandMic()
                hour=datetime.datetime.now().hour
                minute=datetime.datetime.now().minute
                phone_no=user_name[name]
                speak("what is the message?")
                message=takeCommandMic()
                pywhatkit.sendwhatmsg(phone_no,message,hour,minute+1)
                speak("message has been sent")
            except Exception as e:
                print(e)
                speak('unable to send the message')
        elif 'Wikipedia' in quer:
            speak('searching on wikipedia...')
            query=quer.replace('Wikipedia','')
            result=wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'search' in quer:
            searchgoogle()

        elif 'YouTube' in quer:
            speak('what should i search for you on youtube')
            topic=takeCommandMic()
            pywhatkit.playonyt(topic)

        elif 'weather' in quer:
                
                # base URL
                BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
                # City Name CITY = "Hyderabad"
                # API key API_KEY = "Your API Key"
                # upadting the URL
                URL = BASE_URL + "q={API_key}"
                # HTTP request
                response = requests.get(URL)
                # checking the status code of the request
                if response.status_code == 200:
                    # getting data in the json format
                    data = response.json()
                    # getting the main dict block
                    main = data['main']
                    # getting temperature
                    temperature = main['temp']
                    # getting the humidity
                    humidity = main['humidity']
                    # getting the pressure
                    pressure = main['pressure']
                    # weather report
                    report = data['weather']
                    #    print(f"{CITY:-^30}")
                    # temp=round((temperature-32)*5/9)
                    speak('the temperature today is')
                    speak(temperature)
                    # speak('degree celsius')
                    speak('the humidity today is')
                    speak(humidity)
                    speak('the pressure today is')
                    speak(pressure)
                    speak('today there will be')
                    speak({report[0]['description']})
                else:
                    # showing the error message
                    print("Error in the HTTP request")


        elif 'news' in quer:
                news()
            
        elif 'read' in quer:
                text2speech()
            
        elif 'open code' in quer:
                codepath="C:\\Users\\Rapid\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepath)

        elif 'open' in quer:
                os.system('explorer C://{}'.format(quer.replace('open','')))

        elif 'joke' in quer:
                speak(pyjokes.get_joke())
            
        elif 'screenshot' in quer:
                screenshot()
                speak('screenshot taken')
            
        elif 'remember that' in quer:
                speak('what should i remember')
                data=takeCommandMic()
                speak('you said me to remember that'+data)
                remember=open('data.txt','a')
                remember.write('\n'+data)
                remember.close()

        elif 'do you know anything' in quer:
                remember=open('data.txt','r')
                speak("you told me to remember that"+remember.read())

        elif 'password' in quer:
                passwordgen()

        elif 'flip' in quer:
                flip()

        elif 'roll' in quer:
                roll()

        elif 'offline' in quer:
                speak('nice to spend time with you sir')
                speak('see ya')
                quit()
        
