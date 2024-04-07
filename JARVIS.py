import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishme():
    hour = datetime.datetime.now().hour

    if hour >= 0 and hour < 12:
        speak("Good morning, sir")

    elif hour >= 12 and hour < 17:
        speak("Good afternoon, sir")

    elif hour >= 17 and hour < 20:
        speak("Good evening, sir")

    else:
        speak("Good night, sir")

    speak("Hello! Welcome back, sir. I am your personal assistant, Jarvis!")


def takecommand():
    # It takes microphone as input and returns string output

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()

    except Exception as e:
        print("Please, sir, can you repeat that again...")
        speak("Please, sir, can you repeat that again...")
        return "None"


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand()

        # Logic for executing tasks based on query
        if "hello" in query:
            speak("Hello! How can I help you?")

        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia...")
            print(results)
            speak(results)
            page = wikipedia.page(query)
            webbrowser.open(page.url)

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")

        elif "open google" in query:
            webbrowser.open("https://www.google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("https://www.stackoverflow.com")

        elif "play" in query:
            song = query.replace("play", "")
            speak(f"Playing {song.strip()} on YouTube.")
            pywhatkit.playonyt(song.strip())

        elif "exit" in query or "bye" in query:
            speak("Goodbye, Sir!")
            exit()

        else:
            speak("Sorry, Sir. I didn't understand that.")
