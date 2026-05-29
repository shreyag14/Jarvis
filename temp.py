# import pyttsx3

# engine = pyttsx3.init('sapi5')

# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)

# engine.say("yes")
# engine.runAndWait()

# import speech_recognition as sr

# r = sr.Recognizer()

# with sr.Microphone() as source:
#     print("Speak now...")
#     r.adjust_for_ambient_noise(source)
#     audio = r.listen(source)

# try:
#     text = r.recognize_google(audio)
#     print("You said:", text)

# except Exception as e:
#     print(e)



# from dotenv import load_dotenv
# import os

# load_dotenv()

# print(os.getenv("OPENAI_API_KEY"))
# print(os.getenv("NEWS_API_KEY"))


# speak_old("Testing news feature")


# import pyttsx3

# engine = pyttsx3.init('sapi5')

# voices = engine.getProperty('voices')

# engine.setProperty('voice', voices[0].id)

# engine.setProperty('rate', 170)

# engine.say("Hello Shreya, Jarvis is working")

# engine.runAndWait()


# import pyttsx3
# import threading

# engine = pyttsx3.init()

# def speak(text):

#     def run():
#         engine.say(text)
#         engine.runAndWait()

#     threading.Thread(target=run).start()

# speak("Hello Shreya")



# import pyttsx3

# engine = pyttsx3.init()

# voices = engine.getProperty('voices')

# print(voices)

# engine.setProperty('voice', voices[0].id)

# engine.setProperty('rate', 170)

# engine.setProperty('volume', 1)

# engine.say("Hello Shreya")

# engine.runAndWait()


# import win32com.client

# speaker = win32com.client.Dispatch("SAPI.SpVoice")

# speaker.Speak("Hello Shreya")


# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# load_dotenv()

# print(os.getenv("OPENAI_API_KEY"))

# client = OpenAI(
#     api_key=os.getenv("OPENAI_API_KEY")
# )

# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {
#             "role": "user",
#             "content": "Hello"
#         }
#     ]
# )

# print(response.choices[0].message.content)

# echo %OPENAI_API_KEY%