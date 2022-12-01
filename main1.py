import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os
import smtplib

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'guide' in command:
        talk('Your guide is Professor Sachin Deshpande')
    elif 'goodbye' in command:
        talk('GoodBye and Have a nice day')
    elif 'thank you' in command:
        talk('At your service')
    elif 'open google' in command:
        talk('Opening Google')
        webbrowser.open("google.com")
    elif 'open youtube' in command:
        talk('Opening Youtube')
        webbrowser.open("youtube.com")
    elif 'your name' in command:
        talk('My name is Alexa, thanks for asking')
    elif 'name of project' in command:
        talk('Voice assistant using python')
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
