from socket import timeout
from turtle import width
import cv2
import threading
import speech_recognition as sr
import webbrowser
import pyttsx3
import music
import pywhatkit


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Set voice to female
    engine.say(text)
    engine.runAndWait()



def processCommand(c):
    c = c.lower()
    if "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://www.google.com/")
    elif "open facebook" in c:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com/")
    elif "open linkedin" in c:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com/feed/")
    elif "open instagram" in c:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com/")
    
    elif "about me" in c:
        speak("You are my master your name is mujtaba.... your expertise are in.... front end development and python programming...")
    elif "who" in c:
        speak("")

    elif "thank" in c:
        speak("no need...i'm ready at your command master")

    elif "open github" in c:
        speak("Opening GitHub")
        webbrowser.open("https://github.com/mujtabachandio")
    elif "play music" in c:
        # Extract song number if specified
        words = c.split()
        for word in words:
            if word.isdigit():  # Check if the word is a number
                song_index = int(word)
                if 1 <= song_index <= len(music.music):
                    song_name = list(music.music.keys())[song_index - 1]
                    speak(f"Playing {song_name}")
                    webbrowser.open(music.music[song_name])
                    return
                else:
                    speak("Invalid song number.")
                    return
        speak("Sorry, I didn't understand the song number. Please specify a number.")
    else:
        speak("Command not recognized.")









def listen_for_commands():
    activated = False
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = recognizer.listen(source,timeout=2, phrase_time_limit=3)  # Increased timeout
                word = recognizer.recognize_google(audio)
                print(f"Command received: {word}")

                if not activated:
                    if word.lower() == "jarvis":
                        speak("Yes sir!....")
                        activated = True
                        continue

                if activated:
                    processCommand(word)
                
        except sr.UnknownValueError:
            if activated:
                speak("Sorry sir, I didn't understand that....")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    speak("Initializing Jarvis.....")

    
    
    listen_for_commands()
