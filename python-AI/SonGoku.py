import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia
import pyaudio
import wave
import sys
import webbrowser
import time
import tkinter as Tkinter  

name='Nikhil Rawal'

warnings.filterwarnings('ignore')

def age():
    y=datetime.datetime.today().year
    m=datetime.datetime.today().month
    d=datetime.datetime.today().day
    year=2000
    day=14
    month=5
    return y-year-((m,d)<(month,day))

def recordAudio():
    r=sr.Recognizer()#created a object
    with sr.Microphone() as source:#os take audio input
        print('Hey I am riya how can i help you master!')
        audio=r.listen(source)
    data=''
    try:
        data=r.recognize_google(audio)
        print('you said: '+data)
    except sr.unknownValueError:
        print(' unknown error')
    except sr.RequestError as e:
        print('Request error'+e)
    return data

#function for audio
def asr(text):
    print(text)
    myobj=gTTS(text=text,lang='en',slow=False)
    myobj.save('assistant_response.mp3')
    os.system('Start assistant_response.mp3')
      
#a function wake word
def wakeWord(text):
    WAKE_WORDS=['hey','ok','hello']
    text=text.lower()
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True

    return False

def getDate():
    now=datetime.datetime.now()
    my_date=datetime.datetime.today()
    weekday=calendar.day_name[my_date.weekday()]
    monthNum=now.month
    dayNum=now.day
    month_names=['January','February','March','April','May','June','July','August','September','October','November','December']
    ordinalNumbers=['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th','16th','17th','18th','19th','20th','21th','22th','23th','24th','25th','26th','27th','28th','29th','30th','31th']
    return 'Today is '+weekday+' '+month_names[monthNum-1]+' the '+ordinalNumbers[dayNum-1]+' sir. '

def greeting(text):
    GREETING_INPUTS=['hi','hey','hola','greetings','wassup','hello']
    GREETING_OUTPUT=['welcome sir i am arificial intelligence created by nikhil rawal','hello sir i am riya how can i help you','hey there sir i am Artificial intelligence created by Nikhil Rawal']
    for word in text.split():
        if word in GREETING_INPUTS:
            return random.choice(GREETING_OUTPUT)+'. '
    return ''

def getPerson(text):
    wordList=text.split()
    for i in range(0,len(wordList)):
        if i+3<= len(wordList)-1 and wordList[i].lower()=='who' and wordList[i+1].lower()=='is':
            return wordList[i+2]+' '+wordList[i+3]

def contain(otext,text):
    otext=otext.lower()
    text=text.lower()
    for i in otext.split():
        if(i==text):
            return True
    return False

def google(text):
    webbrowser.open('https://google.com/?#q='+text)

def youtube(text):
    webbrowser.open("https://www.youtube.com/results?search_query="+text)

def goodmorning():
    morno=['good morning sir','good morning and have a nice day','good morning sir i am elsa an artificial intelligence']
    return random.choice(morno)

def goodafternoon():
    morno=['good afternoon sir','good afternoon and have a nice day','good afternoon sir i am elsa an artificial intelligence']
    return random.choice(morno)

def goodevening():
    morno=['good evening sir','good evening and have a nice day','good evening sir i am elsa an artificial intelligence']
    return random.choice(morno)

def goodnight():
    morno=['good night sir take a good sleep']
    return random.choice(morno)



    
while True:
    text=recordAudio()
    res=''
    if(wakeWord(text)==True):
        res=greeting(text)
        asr(res)
    elif(contain(text,'riya')):
        asr('She is your younger sister and a certified idiot sir')
    elif(contain(text,'nisha')):
        asr('She is your eldest sister and she is a bad person dont dare to mess with her sir')
    elif(text.lower()=='what is my phone number'):
        asr('9 8 8 8 0 8 4 1 1 7 is your phone number sir')
    elif(contain(text,'date')):
        asr(getDate())
    elif(contain(text,'who')):
        print('working')
        person=text[6:]
        wiki=wikipedia.summary(person,sentences=1)
        asr(wiki)
    elif(contain(text,'youtube')):
        text=text[15:]
        youtube(text)
    elif(contain(text,'search')):
        text=text[13:]
        google(text)
    elif(contain(text,'features')):
        print("My features are as following:\n0. random geetings just say hello riya\n1. basic info about you master(riya,nisha,phone no. ex:tell me about riya, what is my phone number)\n2. tell me date\n3. google search what_you_want_to_search\n4. open youtube\n5.who is person_name and person_surname i will do wikipidia search\n6. what is my age\n7. feel boring\n8. good morning, good afternoon,good night,good evening\n")
    elif(contain(text,'age')):
        Age=age()
        Agestr=str(Age)
        asr('Congratulations sir you are '+Agestr+' years old')
    elif(contain(text,'bored')or contain(text,'boring')or contain(text,'bore')):
        asr('sorry sir i am not good enough to entertain you know please upgrade me master Nikhil rawal')
    elif(contain(text,'morning') or contain(text,'goodmorning')):
        a=goodmorning()
        asr(a)
    elif(contain(text,'night') or contain(text,'goodnight')):
        a=goodnight()
        asr(a)
    elif(contain(text,'evening') or contain(text,'goodevening')):
        a=goodevening()
        asr(a)
    elif(contain(text,'afternoon') or contain(text,'goodafternoon')):
        a=goodafternoon()
        asr(a)


