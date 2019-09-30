# Todd

## Table of Contents
* [General info](#general-info)
* [Setup](#setup)
* [Wishlist](#wishlist)

## General Info
This project is a voice-controlled personal assistant that is intended to be run at startup. This is written in Python 2.7 due to compatibility issues with 3.7, but I would like to bring it up to 3.7 if possible in the future just to keep everything relevant. While it is very much a work in progress, this is a project I can see getting very big and very complicated as time goes on and I continue to improve the overall functionality of Todd.

## Setup
To run this project, you'll need to install (use pip install):
* SpeechRecognition version 3.8.1
* pyttsx version 1.1 
<br />

Navigate into the directory containing Main.py and run `$ python Main.py`. That will run the file and you can press the back-tick key (same key as '~') to alert Todd to listen for a request, which it will then confirm with an audio cue. If you would like to set it to run automatically: <br />
<br />
**Windows:**
1. Create a .bat file somewhere (I would recommend the home directory of your user folder (ex. C:/Users/Hunter))
2. Inside it, type
```
ECHO OFF
cd "Insert path to directory containing Main.py here"
python Main.py
PAUSE
```
3. Open Task Scheduler and create a new Task
4. Name it Todd, set to "Run only when user is logged on"
5. Set the trigger to begin "At log on" and set the task to delay for 1 minute
6. Set the Action to "Start a program" and enter the path to your .bat file that you created at the beginning
7. **Set "Start in" to the directory containing your .bat file**

## Wishlist
* Global key-press recognition, currently limited to recognition when window is in focus
* Ability to read from and write to several files that can save information about the local user (phone number, email, preferred name, etc.) for personalization
* Ability to keep track of the To-Do list and push that list to a mobile number in the form of an SMS message
* Integration into a Discord server for added functionality like fetching the status of members and giving an audio notification of a specific user/role coming online
* Add reading of a new email as an option, given a user's login credentials in a separate file
