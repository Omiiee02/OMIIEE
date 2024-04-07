from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pywhatkit


class JARVIS(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"

        self.label = Label(text="Hello! I am your personal assistant,JARVIS")
        self.add_widget(self.label)

        self.button = Button(text="Start Listening", size_hint=(None, None), size=(150, 50))
        self.button.bind(on_press=self.listen_command)
        self.add_widget(self.button)

        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def wish_me(self):
        hour = datetime.datetime.now().hour

        if hour < 12:
            self.speak("Good morning, sir. How can i help you")

        elif 12 <= hour < 17:
            self.speak("Good afternoon, sir. How can i help you")

        elif 17 <= hour < 20:
            self.speak("Good evening, sir. How can i help you")

        else:
            self.speak("Good night, sir. How can i help you")
           

    def listen_command(self):
        speak("Hello! Welcome back, sir. I am your personal assistant, Jarvis!")

    def take_command(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.pause_threshold = 1
            audio = self.recognizer.listen(source)

        try:
            print("Recognizing...")
            query = self.recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            self.process_command(query.lower())

        except Exception as e:
            print("Please, sir, can you repeat that again...")
            self.speak("Please, sir, can you repeat that again...")

    def process_command(self, query):
        if "hello" in query:
            self.speak("Hello! How can I help you?")

        elif "wikipedia" in query:
            self.speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            self.speak("According to Wikipedia...")
            print(results)
            self.speak(results)
            page = wikipedia.page(query)
            webbrowser.open(page.url)

        elif "open youtube" in query:
            self.speak("Opening YouTube...")
            webbrowser.open("www.youtube.com")

        elif "open google" in query:
            webbrowser.open("https://www.google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("https://www.stackoverflow.com")

        elif "play" in query:
            song = query.replace("play", "")
            self.speak(f"Playing {song.strip()} on YouTube.")
            pywhatkit.playonyt(song.strip())

        elif "exit" in query or "bye" in query:
            self.speak("Goodbye, Sir!")
            exit()

        else:
            self.speak("Sorry, Sir. I didn't understand that.")

    def listen_command(self, instance):
        self.wish_me()
        while True:
            self.take_command()


class JARVIS_AI(App):
    def build(self):
        return JARVIS()


if __name__ == "__main__":
    JARVIS_AI().run()
