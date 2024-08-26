import openai
import speech_recognition as sr
import webbrowser
import datetime
import pyttsx3
import os

# Load API key from environment variable for security
openai.api_key = os.getenv("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")

def Reply(query):
    try:
        # Replace 'gpt-4' with 'gpt-3.5-turbo' or any available model you have access to
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": query}
            ]
        )
        return completion.choices[0].message['content']
    except Exception as e:
        print(f"Error in Reply function: {e}")
        return "Sorry, I couldn't process your request."

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening .......")
        r.pause_threshold = 1
        try:
            audio = r.listen(source)
            print("Recognizing ....")
            query = r.recognize_google(audio, language='en-in')
            print(f"User Said: {query}\n")
            return query
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return "None"
        except sr.RequestError as e:
            print(f"Error with the request: {e}")
            return "None"

def speak(text):
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)  # Set to desired voice
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in speak function: {e}")

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if query == "none":
            continue

        if 'youtube' in query:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            response = f"The current time is {strTime}"
            print(response)
            speak(response)
        else:
            ans = Reply(query)
            print(ans)
            speak(ans)
