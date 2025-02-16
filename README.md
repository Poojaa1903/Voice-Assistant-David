# Voice Assistant - David 🤖

A simple voice assistant built using **Streamlit**, **pyttsx3**, **SpeechRecognition**, and **Wikipedia API** that can perform tasks such as fetching weather updates, opening websites, searching Wikipedia, and more!

## Features ✨
- 🎤 **Speech Recognition:** Listens to user commands.
- 🔊 **Text-to-Speech:** Provides voice responses using `pyttsx3`.
- 🔍 **Wikipedia Search:** Fetches short summaries from Wikipedia.
- 🌍 **Weather Updates:** Retrieves real-time weather using Open-Meteo API.
- 🎬 **YouTube Search:** Opens YouTube with a user-defined search query.
- 🕒 **Time Announcement:** Tells the current time.
- 🎵 **Music Playback:** Plays music from a specified folder.

### Commands You Can Use 🗣️
- **"Search Wikipedia for <topic>"** - Fetches a summary from Wikipedia.
- **"Open YouTube"** - Asks for a search term and opens YouTube.
- **"Open Google"** - Opens Google homepage.
- **"Play Music"** - Plays a song from a predefined folder.
- **"What is the time?"** - Tells the current time.
- **"What is the weather in <city>?"** - Fetches the weather report.
- **"Exit" / "Quit"** - Stops the assistant.

## Notes 📝
- Ensure your microphone is working for speech recognition.
- Modify `music_dir` in the code to point to your music folder.
- The weather feature supports predefined cities (Mumbai, New York, etc.).
- For better performance, adjust the timeout and phrase limit in `takeCommand()`.

## Author 🧑‍💻
Made with ❤️ by **Pooja Nayak** 🙋‍♀️

