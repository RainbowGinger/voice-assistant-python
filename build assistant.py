import speech_recognition as sr
from gtts import  gTTS
import wikipedia
import os
import random
import datetime

def recordAudio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Rainbow, what do you want to know today?')
        audio=r.listen(source)
    try:
        data=r.recognize_google(audio)
        print('Yes, I said: ' + data)

    except:
        return recordAudio()

    return data

def assistantResponse(text):
  print(text)
  myobj=gTTS(text=text,lang='en',slow=False)
  myobj.save('assistant.mp3')
  os.system('start assistant.mp3')

def wakeword(text):
    wakewords=['hi computer','ok computer']
    text=text.lower()
    for phrase in wakewords:
      if phrase in text:
        return True
    return False

def datecal():
    weekday2=datetime.datetime.now().strftime("%A")
    month=datetime.datetime.now().strftime("%B")
    return 'today is'+weekday2+' '+month

def greeting(text):
    greeting_words=['hey','hi','hello']
    response_word=['hey there  ', 'hi,how are you  ','howdy  ']
    for y in greeting_words:
        if y in text.lower():
            return random.choice(response_word)
    return ''

def getPerson(text):
    word=text.split()
    for i in range(0,len(word)):
        if i-3<len(word) and word[i].lower()=='who' and word[i+1].lower()=='is':
            return word[i+2]+" "+word[i+3]

def getdetail(text):
    word=text.split()
    for i in range(0,len(word)):
        if i-2<len(word) and word[i].lower()=='what' and word[i+1].lower()=='is':
            return word[i+2:]

def howto(text):
    word=text.split()
    for i in range(0,len(word)):
        if i-2<len(word) and word[i].lower()=='how' and word[i+1].lower()=='to':
            return word[i+2:]

while True:
    text=recordAudio()
    response=''
    if (wakeword(text)==True):

        response=response+greeting(text)
        if ('date' in text):
            response=response+datecal()
        if('who' in text):
            response=response+wikipedia.summary(getPerson(text),sentences=1)
        if ('what is' in text):
            response = response + wikipedia.summary(getdetail(text), sentences=1)
        if ('how to' in text):
            response = response + wikipedia.summary(howto(text), sentences=2)
        if ('time' in text):
            time=datetime.datetime.now().time()
            response=response+"it is"+str(time)

        assistantResponse(response)






