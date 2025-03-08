import boto3
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit

# AWS Polly (Text-to-Speech)
polly = boto3.client("polly", region_name="us-east-1")
translate = boto3.client("translate", region_name="us-east-1")

def speak(text):
    """Convert text to speech using AWS Polly"""
    response = polly.synthesize_speech(Text=text, OutputFormat="mp3", VoiceId="Joanna")
    with open("output.mp3", "wb") as file:
        file.write(response["AudioStream"].read())
    os.system("mpg321 output.mp3")  # Play the speech

def wishme():
    """Personalized greeting based on time of day"""
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        speak("Good morning, sir")
    elif 12 <= hour < 17:
        speak("Good afternoon, sir")
    elif 17 <= hour < 20:
        speak("Good evening, sir")
    else:
        speak("Good night, sir")

    speak("Hello! Welcome back, sir. I am your personal assistant, Jarvis!")

def takecommand():
    """Get user input via Amazon Connect Chat"""
    print("Listening for input from Amazon Connect...")
    
    # Simulating input (Replace with actual chat retrieval from Amazon Connect)
    query = input("You: ").lower()

    if not query:
        speak("Please, sir, can you repeat that again...")
        return "None"

    return query

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
            song = query.replace("play", "").strip()
            speak(f"Playing {song} on YouTube.")
            pywhatkit.playonyt(song)

        elif "exit" in query or "bye" in query:
            speak("Goodbye, Sir!")
            exit()

        else:
            speak("Sorry, Sir. I didn't understand that.")
