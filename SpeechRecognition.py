import speech_recognition as sr
import pyttsx3 as sx
import pywhatkit as wt
import datetime as dt
import wikipedia as wk
import pyjokes as jk

listener = sr.Recognizer()
engine = sx.init()
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
    except sr.UnknownValueError:
        talk("Sorry, I didn't catch that. Can you repeat?")
        command = take_command()
    except sr.RequestError:
        talk("Sorry, I'm having trouble accessing my speech recognition service. Please check your internet connection.")
        command = take_command()
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        wt.playonyt(song)

    elif 'time' in command:
        time = dt.datetime.now().strftime('%I:%M %p')
        talk('Current Time ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wk.summary(person, 1)
        print(info)
        talk(info)

    elif 'joke' in command:
        talk(jk.get_joke())
    
    elif 'stop' in command:
        exit(0)

    else:
        talk('I am not programmed to respond to that command.')


while True:
    run_alexa()