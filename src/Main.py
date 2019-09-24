import speech_recognition as sr
import webbrowser
from time import ctime
import time
import os
from playsound import playsound
from gtts import gTTS
import pyttsx


def speak(audioString):
    # tts = gTTS(text=audioString, lang='en')
    # tts.save("D:/vcs/GitHub/Todd/src/audio.mp3")
    # playsound("D:/vcs/GitHub/Todd/src/audio.mp3")
    # os.remove("D:/vcs/GitHub/Todd/src/audio.mp3")
    engine = pyttsx.init()
    sound = engine.getProperty('voices')
    engine.setProperty('voice', sound[0].id)
    engine.say(audioString)
    engine.runAndWait()


# def recordAudio():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Say something!")
#         audio = r.listen(source)
#
#         data = ""
#         try:
#             data = r.recognize_google(audio)
#             print("You said: " + data)
#         except sr.UnknownValueError:
#             print("Google Speech Recognition could not understand audio")
#         except sr.RequestError as e:
#             print("Could not request results from Google Speech Recognition service; {0}".format(e))
#         return data


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
    print("Todd is up and running ")
    speak("Todd is up and running")
    while 1:
        audio = r.listen(source)
        todd()



