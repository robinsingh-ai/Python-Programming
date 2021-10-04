import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12 :
        speak("Good Morning Robin, How Are You!")
    elif hour >=12 and hour <18:
        speak("Good Afternoon Robin , How Are You ")
    else:
        speak("Good Evening Robin , How Are You")
    speak("I am jarvis, Please Tell Me How Can I Help You")

def send_email(to,message):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('email','your-password')
    server.sendmail('rsinghpooj@gmail.com',to,message)
    server.close()

def take_command():
    """
    It takes speech input from the user and returns string o/p
    """
    s = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        s.pause_threshold =1 # seconds of non-speaking audio before a phrase is considered complete
        aud = s.listen(source)

    try :
        print("Recognizing.....!")
        info = s.recognize_google(aud,language='en-in')
        print("Robin Said : ",info)


    except Exception as e:
        # print(e)
        print("Not Recognizing..... Please  Say that Again...")
        return 'None'

    return info

if __name__ == '__main__':
    # speak("hey, i am zara guys, how are you robin, what can i do for you")
    # while True:?
    print("Initializing Jarvis....")
    speak("Initializing Jarvis....")
    chrome_path = 'C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s'
    mozila_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"

    wish_me()
    while True:
        query = take_command()
        query = query.lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia....Please Wait')
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=5)
            speak("According To wikipedia :")
            print(result)
            speak(result)

        elif "open youtube " in query:
            # webbrowser.open("youtube.com") for default browser
            webbrowser.get(chrome_path).open_new_tab(url="youtube.com")

        elif "open google " in query:
            # webbrowser.open("google.com")
            webbrowser.get(chrome_path).open_new_tab(url="google.com")

        elif "open github " in query:
            # webbrowser.open("github.com")
            webbrowser.get(chrome_path).open_new_tab(url="github.com")
        elif " music" in query:
            music = "E:\\Robin\\Songs\\Main"
            songs = os.listdir(music)
            print(songs)
            n = random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music,songs[n]))

        elif " time " in query:
            time1 = datetime.datetime.now().strftime("%H:%M:%S")
            print(time1)
            speak(f"Hello Robin, Now Time is {time1}")

        elif "visual studio" in query:
            visualCOde = "C:\\Users\\Robin Singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(visualCOde)

        elif "open git" in query:
            git_path = "C:\\Program Files\\Git\\git-bash.exe"
            os.startfile(git_path)

        elif "pycharm" in query:
            pycharm = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.3.2\\bin\\pycharm64.exe"
            os.startfile(pycharm)

        elif "email " in query:
            try:
                speak("Say message")
                message = take_command()
                to = "rsinghpooj@gmail.com"
                send_email(to,message)
                speak("Email has been send")

            except Exception as e:
                speak("Sorry , i m not able to send your email ")

        elif "jarvis quit" in query:
            quit()












