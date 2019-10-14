import speech_recognition as sr
import webbrowser
from time import ctime
import pyttsx
import keyboard
import yaml
from yaml import Loader, Dumper
import smtplib


def speak(audio_string):
    engine = pyttsx.init()
    sound = engine.getProperty('voices')
    engine.setProperty('voice', sound[0].id)
    engine.say(audio_string)
    engine.runAndWait()


def send_email(from_addr, to_addr, cc_addr_list, subject, message, login,
               password, smtpserver='smtp.gmail.com:587'):
    header = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    issues = server.sendmail(from_addr, to_addr, message)
    server.quit()
    return issues


def todd(info):
    try:
        data = r.recognize_google(audio)
        if "how are you" in data:
            speak("I am fine, thanks for asking")
        if "what time is it" in data:
            speak("It's currently " + ctime())
        if "shut down" in data:
            speak("Shutting down now")
            exit(0)
        if "change my name to" in data:
            new_name = data[18:]
            info.update({"name": new_name})
            yaml.dump(info, open("config.yaml", "w"), Dumper=Dumper)
            speak("Sounds good, your name is now" + new_name)
        if "I'd like to change my email" in data:
            speak("Alright, type your new email in the terminal")
            new_email = raw_input('New Email:')
            info.update({"email": new_email})
            yaml.dump(info, open("config.yaml", "w"), Dumper=Dumper)
            speak("Your new email is " + new_email)
        if "where is" in data:
            data = data.split(" ")
            location = ""
            for item in data:
                if item != "where" and item != "is":
                    location = location + item + " "
            speak("Hold on " + info.get("name") + ", I will show you where " + location.rstrip() + " is.")
            webbrowser.register('firefox', None,
                                webbrowser.BackgroundBrowser("C:/Program Files/Mozilla Firefox/firefox.exe"))
            webbrowser.get('firefox').open_new_tab('https://www.google.com/maps/place/' + location + "/&amp;")
        if "send me an audio text" in data:
            speak("Alright, what would you like me to send?")
            new_audio = r.listen(source)
            text = r.recognize_google(new_audio)
            send_email('Todd@yourpc.net', info.get("phone") + "@vtext.com", "", "", text,
                       info.get("email"), info.get("email app password"))
            speak("Text sent")
        if "send me a text" in data:
            speak("Alright, what would you like me to send?")
            text = raw_input('Text:')
            send_email('Todd@yourpc.net', info.get("phone") + "@vtext.com", "", "", text,
                       info.get("email"), info.get("email app password"))
            speak("Text sent")
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print("Todd error; {0}".format(e))


r = sr.Recognizer()
file = yaml.load(open("config.yaml", "r"), Loader=Loader)
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=5)
    print("Todd is up and running")
    speak("Todd is up and running")
    while 1:
        if keyboard.is_pressed('`'):
            speak("How may I assist you?")
            audio = r.listen(source)
            todd(file)
