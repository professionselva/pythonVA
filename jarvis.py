import win32com.client as wincl
import wikipedia
import mp3play
import speech_recognition as sr
import time
import os
import webbrowser
new=2

def wiki(data3):
    data = wikipedia.summary(data2,sentences=2)
    print data
    voice = wincl.Dispatch("SAPI.SpVoice")
    voice.Speak(data)

def playsong(data2):
    location = "e:"
    mp= ".mp3"
    mfile = data1
    pfile=location+data1+mp
    clip = mp3play.load(location+pfile)
    clip.play()
    time.sleep(min(10, clip.seconds()))
    clip.stop()

def search(data2):
    taburl="http://google.com/?#q="
    webbrowser.open(taburl+data2,new=new)
    


def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data


while 1:
    data1 = recordAudio()

    if data1==("search" or "Search"):
        data2=recordAudio()
        
        search(data2)

    if data1==("wiki" or "Wiki"):
        data3=recordAudio()
        wiki(data3)
        break

    if data1=="playsong":
        playsong()

    else:
        print("not audible ...Please try again")
