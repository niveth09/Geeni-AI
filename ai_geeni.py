import pyttsx3
import datetime
import calendar
import speech_recognition as sr
import wikipedia
import webbrowser as wb 
import os


engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time = datetime.datetime.now().strftime('%H:%M:%S')
    speak('The current time is')
    speak(time)

def date():
    year = int(datetime.datetime.now().year)
    month_name = calendar.month_name[int(datetime.datetime.now().month)]
    date = int(datetime.datetime.now().day)
    speak('The current date is')
    speak(date)
    speak(month_name)
    speak(year)

def wish():
    hour = datetime.datetime.now().hour 

    if hour>=6 and hour<12:
        speak('Good morning Nivetha')
    elif hour>=12 and hour<18:
        speak('Good afternoon Nivetha')
    elif hour>=18 and hour<24:
        speak('Good evening Nivetha')

    speak('Geeni at your service Please tell me how can i help you?')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("Say something please!")
        return "None"
    
    return query


if __name__ == "__main__":
    wish()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        elif 'search in google' in query:
            speak('What should I search?')
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search =  takeCommand().lower()
           
            wb.get(chromepath).open_new_tab(search+'.com')
       
        elif 'logout' in query or 'log out' in query:
            os.system("shutdown -l")
        elif 'shutdown' in query:
            os.system("shutdown /s /t l")
        elif 'restart' in query:
            os.system("shutdown /r /t l")

        elif 'play songs' in query:
            songs_dir = "C:\\Users\\nivet\\Music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))

        elif "offline" in query:
            quit()





