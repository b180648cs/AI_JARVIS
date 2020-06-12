import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import pyjokes
import psutil
engine=pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Time():
    time=datetime.datetime.now().strftime("%I:%M:%S")
    speak(time)
def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    dates=int(datetime.datetime.now().day)
    speak(dates)
    speak(month)
    speak(year)

def cpu():
    usage=str(psutil.cpu_percent())
    speak("Cpu is at"+usage)
    battery=psutil.sensors_battery()
    speak("battery is at")
    speak(str(battery.percent))
       

def wishme():
    speak("welcome back sir ")
    speak("the current time is")
    Time()
    speak("the current date is")
    date()
    hour=datetime.datetime.now().hour
    if hour>6 and hour<=12:
        speak("Good morning sir")
    
    elif hour>12 and hour<=18:
        speak("Good evening sir")
    
    else:
        speak("Good night sir")
    speak("jarvis is at your service sir how can i help you ")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning..")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query =r.recognize_google(audio,language ='en-in')
        print(query)
    except Exception as e:
        speak("say again please")
        print(e)
        return None
    
    return query
def jokes():
    speak(pyjokes.get_joke())

if __name__=="__main__":
    wishme()
    while True:
        query=takeCommand().lower()
        if 'time' in query:
            Time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching ...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        elif 'search in chrome' in query:
            speak("what to search")
            chromepath='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search=takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
        

        elif 'hello jarvis' in query:
            speak("hi sir how are you hope everything is fine")
        
        elif 'logout' in query:
            os.system("shutdown -1")
        
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        
        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'play songs' in query:
            songs_dir="D:\Arjit singh"
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))

        elif 'remember that' in query:
            speak("What should i remeber")
            data=takeCommand()
            speak("You said me to remember that"+data)
            remember=open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'do you know anything ' in query:
            remember=open('data.txt','r')
            speak("you said me to remember that"+remember.read())
        elif 'joke' in query:
            jokes()
        elif 'cpu usage' in query:
            cpu()
        elif 'offline' in query:
            quit()