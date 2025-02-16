import streamlit as st
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import requests

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        greeting = "Good Morning 🌞!!"
    elif hour >= 12 and hour < 16:
        greeting = "Good Afternoon ☀️!!"
    else:
        greeting = "Good Evening 🌙!!"
    speak(greeting)
    speak("I am David 🤖. Please tell me how may I help you?")
    return greeting

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("🎧 Listening... 👂")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            query = r.recognize_google(audio, language='en-in')
            st.write(f"💬 User Said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            st.write("❌ Sorry, I did not catch that. Please repeat.")
            speak("Sorry, I did not catch that. Please repeat.")
            return ""
        except sr.RequestError:
            st.write("❌ Speech recognition service is unavailable.")
            speak("Speech recognition service is unavailable.")
            return ""

def get_weather(city):
    city_coordinates = {
        "new york": (40.7128, -74.0060),
        "mumbai": (19.0760, 72.8777),
        "london": (51.5074, -0.1278),
        "paris": (48.8566, 2.3522),
        "tokyo": (35.6895, 139.6917)
    }
    if city in city_coordinates:
        latitude, longitude = city_coordinates[city]
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
        response = requests.get(url)
        data = response.json()
        if "current_weather" in data:
            temperature = data["current_weather"]["temperature"]
            windspeed = data["current_weather"]["windspeed"]
            report = f"The current temperature in {city} is {temperature}°C 🌡️ with a wind speed of {windspeed} km/h 🌬️."
            speak(report)
            return report
    return "I couldn't retrieve weather data. ❌"

st.title("Voice Assistant - David 🤖")

# Personalized greeting
st.markdown("Made with ❤️ by **Pooja Nayak** 🙋‍♀️")

# Run the assistant if the button is clicked
if st.button("Start Voice Assistant 🎙️"):
    wishMe()

    # Loop for continuous interaction
    while True:
        query = takeCommand()

        if 'wikipedia' in query:
            speak("🔍 Searching Wikipedia... 📚")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak(results)
            st.write(f"📝 {results}")
        elif 'open youtube' in query:
            speak("🎬 What would you like to search on YouTube?")
            search_query = takeCommand()
            if search_query:
                webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
        elif 'play music' in query:
            music_dir = "C:\\Music"
            songs = os.listdir(music_dir)
            if songs:
                os.startfile(os.path.join(music_dir, songs[0]))
            else:
                speak("❌ No songs found in the directory.")
        elif 'the time' in query:
            time_now = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time_now} ⏰")
            st.write(f"🕒 {time_now}")
        elif 'weather' in query:
            speak("🌍 Please tell me the city name for weather details.")
            city = takeCommand()
            weather_report = get_weather(city)
            st.write(f"☁️ {weather_report}")
        elif 'exit' in query or 'quit' in query:
            speak("👋 Goodbye! Have a nice day! 🌟")
            st.stop()
            break
