import speech_recognition as sr
import webbrowser
from time import ctime
import pyttsx
import keyboard


def speak(audio_string):
    engine = pyttsx.init()
    sound = engine.getProperty('voices')
    engine.setProperty('voice', sound[0].id)
    engine.say(audio_string)
    engine.runAndWait()


def todd():
    try:
        data = r.recognize_google(audio)
        if "how are you" in data:
            speak("I am fine, thanks for asking")
        if "what time is it" in data:
            speak("It's currently " + ctime())
        if "shut down" in data:
            speak("Shutting down now")
            exit(0)
        if "where is" in data:
            data = data.split(" ")
            location = ""
            for item in data:
                if item != "where" and item != "is":
                    location = location + item + ""
            speak("Hold on Hunter, I will show you where " + location.rstrip() + " is.")
            webbrowser.register('firefox', None, webbrowser.BackgroundBrowser("C:/Program Files/Mozilla Firefox/firefox.exe"))
            webbrowser.get('firefox').open_new_tab('https://www.google.com/maps/place/' + location + "/&amp;")
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print("Todd error; {0}".format(e))


r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=5)
    print("Todd is up and running")
    speak("Todd is up and running")
    while 1:
        # key = ord(getch())
        if keyboard.is_pressed('`'):
            speak("How may I assist you?")
            audio = r.listen(source)
            todd()





