import requests
from functions.online_ops import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message, get_city_from_ip
import pyttsx3
import speech_recognition as sr
from decouple import config
from datetime import datetime
from functions.os_ops import open_calculator, open_camera, open_cmd, open_notepad, open_discord, open_vscode
from random import choice
from utils import opening_text
from pprint import pprint

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Text to Speech Conversion
def speak(text):
    """Used to speak whatever text is passed to it"""
    engine.say(text)
    engine.runAndWait()

# Greet the user
def greet_user():
    """Greets the user according to the time"""
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")

# Takes Input from User
def take_user_input(ignore_error=False):
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')

        # If task is not in progress, ask again
        if not ignore_error and (query == 'None' or 'exit' in query or 'stop' in query):
            speak('Sorry, I could not understand. Could you please say that again?')
        else:
            if not ('exit' in query or 'stop' in query):
                speak(choice(opening_text))
            else:
                hour = datetime.now().hour
                if hour >= 21 or hour < 6:
                    speak("Good night sir, take care!")
                else:
                    speak('Have a good day sir!')
                exit()
    except Exception:
        if not ignore_error:
            speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query

# Main function where the listening loop continues
if __name__ == '__main__':
    greet_user()
    while True:
        # Listen for commands indefinitely
        query = take_user_input(ignore_error=True).lower()

        if 'open notepad' in query:
            open_notepad()

        elif 'open discord' in query:
            open_discord()

        elif 'open command prompt' in query or 'open cmd' in query:
            open_cmd()

        elif 'open camera' in query:
            open_camera()

        elif 'open vscode' in query:
            open_vscode()

        elif 'open calculator' in query:
            open_calculator()

        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, sir?')
            search_query = take_user_input(ignore_error=True).lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)

        elif 'youtube' in query:
            speak('What do you want to play on Youtube, sir?')
            video = take_user_input(ignore_error=True).lower()
            play_on_youtube(video)

        elif 'search on google' in query:
            speak('What do you want to search on Google, sir?')
            query = take_user_input(ignore_error=True).lower()
            search_on_google(query)

        elif "send whatsapp message" in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = take_user_input(ignore_error=True).lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")

        elif "send an email" in query:
            speak("On what email address do I send sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject sir?")
            subject = take_user_input(ignore_error=True).capitalize()
            speak("What is the message sir?")
            message = take_user_input(ignore_error=True).capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email sir.")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs sir.")

        elif 'joke' in query:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(joke)

        elif "advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)

        elif 'news' in query:
            speak("What category of news would you like to hear about? For example, sports, technology, health, etc.")
            category = take_user_input().lower()
            if category in ["sports", "technology", "health", "entertainment", "business", "science"]:
                speak(f"Fetching the latest {category} news for you.")
                get_latest_news(category)
            else:
                speak(f"Sorry, I don't have news for the category {category}. Please try a different one.")

        if 'weather' in query:
            city = get_city_from_ip()
            if city:
                speak(f"Getting the weather report for {city}.")
                weather, temperature, feels_like = get_weather_report(city)
                if weather and temperature and feels_like:
                    speak(f"The current weather in {city} is {weather}.")
                    speak(f"The temperature is {temperature}, but it feels like {feels_like}.")
                    print(f"Weather: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
                else:
                    speak(f"Sorry, I couldn't fetch the weather data for {city}.")
            else:
                speak(
                    "Sorry, I couldn't determine your location. Please check your network connection or try again later.")

