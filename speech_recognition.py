"""This program is a person assistante that can recognize your voice
using the speech recognition algorithm of AI and answering spoken voice
who can convert the text into a speech."""

"""tool to use are: Python recognition module; google speech API and 
the google texter speech API(gtts)"""


#Build the person assistance

import speech_recognition as sr

from time import ctime

import time

import os

from gtts import gTTs

import pyglet #module for audio and video

import subprocess

#define the speak function. It contain the audio speech parameter

def speak(audioString):
    print(audioString)
    tts= gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")

#use a mediaplayer to get the audio
#set the path for the player and read the path
#get the audio after the text has been converted into a speech

rb = r"/usr/bin/rhythmbox"
media_file = os.path.abspath(os.path.realpath("/home/hilbert/Desktop/Speech_recognition_project/speech_recognition.py"))
call = subprocess.call([rb,media_file])

#define a function to record the audio

def recordAudio():
    rec = sr.recognizer()
    with sr.Microphone() as source:
        print("Speak up please")
    audio = rec.listen(source)

#store data

    data_stored = ""

#check error and exception

try:
    data_stored = rec.recognize_google(audio)#use googleAPI
    print("You said: " + data_stored)
except sr.UnknownValueError:
        print("Repeat please, I can not understand you")
except sr.RequestError as e:#In case a file is missing on demand
        print("Couldn't request results; {0}".format(e))
    return data_stored

#build the person assistante function
#the function will hold the name of the personal assistante

def yosh(data_stored):
    if "how are you" in data_stored:
        speak("I am fine")


#define a sleep time for missing respose
time.sleep(2)
speak("How can I help you?")
while 1:
    data_stored = recordAudio()
yosh(data_stored)