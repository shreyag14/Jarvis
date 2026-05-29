import speech_recognition as sr
import webbrowser
# import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
# from gtts import gTTS
# import pygame
from dotenv import load_dotenv
import os
import time
# import threading
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

load_dotenv()


# pip install pocketsphinx

recognizer = sr.Recognizer()

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# print(voices)
# engine.setProperty('voice', voices[0].id)
# engine.setProperty('rate', 170)
# engine.setProperty('volume', 1.0)

newsapi = os.getenv("NEWS_API_KEY")

def speak_old(text):

    print(f"Speaking: {text}")

    speaker.Speak(text)



# def speak(text):
#     tts = gTTS(text)
#     tts.save('temp.mp3') 

#     # Initialize Pygame mixer
#     pygame.mixer.init()

#     # Load the MP3 file
#     pygame.mixer.music.load('temp.mp3')

#     # Play the MP3 file
#     pygame.mixer.music.play()

#     # Keep the program running until the music stops playing
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)
    
#     pygame.mixer.music.unload()
#     os.remove("temp.mp3") 

def aiProcess(command):
    client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"),
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().replace("play ", "")
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak_old("Song not found")

    elif "news" in c.lower():

        speak_old("Fetching latest news")

        url = f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={newsapi}"

        r = requests.get(url)

        print(r.status_code)
        print(r.text)

        if r.status_code == 200:

            data = r.json()

            articles = data.get("articles", [])

            if len(articles) == 0:
                speak_old("No news articles found")

            else:
                for article in articles[:5]:

                    title = article['title']

                    print(title)

                    speak_old(title)

        else:
            speak_old("Unable to fetch news")

    else:
        # Let OpenAI handle the request
        output = aiProcess(c)
        speak_old(output) 





if __name__ == "__main__":
    speak_old("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        # r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            word = recognizer.recognize_google(audio)
            print(word)
            if "jarvis" in word.lower():
                speak_old("Ya")
                time.sleep(1)
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
                    command = recognizer.recognize_google(audio)

                    print(command)
                    processCommand(command)


        except Exception as e:
            print(f"Error: {e}")











# recognizer = sr.Recognizer()
# engine = pyttsx3.init()
# newsapi = os.getenv("NEWS_API_KEY")
    
# def speak(text):
#     print("Jarvis:", text)
#     engine.say(text)
#     engine.runAndWait()

# def processCommand(c):
#     print("Command:", c)

#     if "open google" in c.lower():
#         webbrowser.open("https://google.com")

#     elif "open facebook" in c.lower():
#         webbrowser.open("https://facebook.com")

#     elif "open youtube" in c.lower():
#         webbrowser.open("https://youtube.com")

#     elif "open linkedin" in c.lower():
#         webbrowser.open("https://linkedin.com")

#     elif c.lower().startswith("play"):
#         song = c.lower().split(" ")[1]
#         link = musicLibrary.music[song]
#         webbrowser.open(link)

#     elif "news" in c.lower():
#         speak("Fetching news")
#         r = requests.get(f"https://newsapi.org/v2/everything?q=india&sortBy=publishedAt&apiKey={newsapi}")
#         if r.status_code == 200:
#             # Parse the JSON response
#             data = r.json()

#             #Extract the articles
#             articles = data.get('articles', [])

#             # Print yhe headlines
#             for article in articles:
#                 speak(article['title'])

#     else:
#         # Let openAI handle the request
#         pass




# if __name__  == "__main__":
#     speak("Initializing Jarvis....")

#     while True:
#         # Listen for the wake word "Jarvis"
#         # # obtain audio from the microphone
#         r = sr.Recognizer()

#         print("recognizing...")
#         # recognize speech using google
#         try:
#             with sr.Microphone() as source:
#                 print("Listening....")
#                 audio = r.listen(source, timeout=5, phrase_time_limit=5)
#             word = r.recognize_google(audio)
#             if word.lower() == "jarvis":
#                 speak("yes")

#                 # Listen for command
#                 with sr.Microphone() as source:
#                     print("Jarvis Active....")
#                     audio = r.listen(source)
#                     command = r.recognize_google(audio)

#                     print(command)
#                     processCommand(command)

#         except sr.WaitTimeoutError:
#             print("No speech detected")

#         except sr.UnknownValueError:
#             print("Could not understand audio")


#         except Exception as e:
#             print("Error; {0}".format(e))





# recognizer = sr.Recognizer()
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')

# engine.setProperty('voice', voices[0].id)

# engine.setProperty('rate', 170)

# newsapi = os.getenv("NEWS_API_KEY")

# def speak_old(text):
#     engine.say(text)
#     engine.runAndWait()


# def speak(text):

#     print("Jarvis:", text)

#     engine.say(text)

#     engine.runAndWait()



# # def speak(text):
# #     tts = gTTS(text)
# #     tts.save('temp.mp3') 

# #     # Initialize Pygame mixer
# #     pygame.mixer.init()

# #     # Load the MP3 file
# #     pygame.mixer.music.load('temp.mp3')

# #     # Play the MP3 file
# #     pygame.mixer.music.play()

# #     # Keep the program running until the music stops playing
# #     while pygame.mixer.music.get_busy():
# #         pygame.time.Clock().tick(10)
    
# #     pygame.mixer.music.unload()
# #     os.remove("temp.mp3") 

# def aiProcess(command):

#     try:

#         client = OpenAI(
#             api_key=os.getenv("OPENAI_API_KEY")
#         )

#         completion = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {
#                     "role": "system",
#                     "content": "You are a virtual assistant named Jarvis."
#                 },
#                 {
#                     "role": "user",
#                     "content": command
#                 }
#             ]
#         )

#         return completion.choices[0].message.content

#     except Exception as e:

#         print("OpenAI Error:", e)

#         return "OpenAI service is unavailable right now."
# def processCommand(c):
#     if "open google" in c.lower():
#         webbrowser.open("https://google.com")
#     elif "open facebook" in c.lower():
#         webbrowser.open("https://facebook.com")
#     elif "open youtube" in c.lower():
#         webbrowser.open("https://youtube.com")
#     elif "open linkedin" in c.lower():
#         webbrowser.open("https://linkedin.com")
#     elif c.lower().startswith("play"):
#         song = c.lower().split(" ", 1)[1]
#         link = musicLibrary.music[song]
#         webbrowser.open(link)

#     elif "news" in c.lower():
#         speak("Fetching latest news")
#         url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}"
#         r = requests.get(url)

#         print(r.status_code)

#         data = r.json()

#         print(data)

#         if r.status_code == 200:

#             articles = data.get("articles", [])

#             if len(articles) == 0:
#                 speak("No news found")

#             else:

#                 for article in articles[:5]:

#                     title = article["title"]

#                     print(title)

#                     speak(title)

#         else:
#             speak("Unable to fetch news")


# if __name__ == "__main__":
#     speak("Initializing Jarvis....")
#     while True:
#         # Listen for the wake word "Jarvis"
#         # obtain audio from the microphone
#         r = sr.Recognizer()
         
#         print("recognizing...")
#         try:
#             with sr.Microphone() as source:
#                 print("Listening...")
#                 r.adjust_for_ambient_noise(source, duration=1)
#                 audio = r.listen(source, timeout=2, phrase_time_limit=5)
#             word = r.recognize_google(audio)
#             if(word.lower() == "jarvis"):
#                 speak("Ya")
#                 # Listen for command
#                 with sr.Microphone() as source:
#                     print("Jarvis Active...")
#                     audio = r.listen(source)
#                     command = r.recognize_google(audio)

#                     processCommand(command)


#         except Exception as e:
#             print("Error; {0}".format(e))
