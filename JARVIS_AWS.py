import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit

# Initialize recognizer and speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def wishme():
    """Greet the user based on time of day"""
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good morning, sir")
    elif hour < 17:
        speak("Good afternoon, sir")
    elif hour < 20:
        speak("Good evening, sir")
    else:
        speak("Good night, sir")

    speak("Hello! Welcome back, sir. I am your personal assistant, Jarvis!")

def takecommand():
    """Listen for voice commands (with error handling)"""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Reduce noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand. Please repeat.")
        speak("Sorry, I could not understand. Please repeat.")
        return "None"
    except sr.RequestError:
        print("Network error. Please check your connection.")
        speak("Network error. Please check your connection.")
        return "None"

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand()

        # Logic for executing tasks based on query
        if "hello" in query:
            speak("Hello! How can I assist you?")

        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia...")
                print(results)
                speak(results)
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find any results on Wikipedia.")
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results. Please be more specific.")

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube.")

        elif "open google" in query:
            webbrowser.open("https://www.google.com")
            speak("Opening Google.")

        elif "open stackoverflow" in query:
            webbrowser.open("https://www.stackoverflow.com")
            speak("Opening Stack Overflow.")

        elif "play" in query:
            song = query.replace("play", "").strip()
            speak(f"Playing {song} on YouTube.")
            pywhatkit.playonyt(song)

        elif "exit" in query or "bye" in query:
            speak("Goodbye, Sir!")
            exit()

        else:
            speak("Sorry, I didn't understand that.")
