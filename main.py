
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
       # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    print(("I am jarvis . Please tell me how may I help you"))
    speak("I am jarvis . Please tell me how may I help you")
    while True:
        # if 1:
        query = takeCommand().lower()
        if 'jarvis' in query:
            query = query.replace('jarvis', '')
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak('no information found sir')

        elif 'google' in query:
            l1 = ['youtube', 'on youtube', 'play', 'at youtube', 'jarvis',
                  'youtube', '  ', 'on google', 'wikipedia', 'search', 'find', ]
            for word in l1:
                query = query.replace(word, ' ')
            speak('here is the search results sir')
            pywhatkit.search(query)
            print(query)
        elif 'search' in query:
            l1 = ['youtube', 'on youtube', 'play', 'at youtube', 'jarvis',
                  'youtube', '  ', 'on google', 'wikipedia', 'search', 'find', ]
            for word in l1:
                query = query.replace(word, ' ')
            speak('here is the search results sir')
            pywhatkit.search(query)
            print(query)
        elif 'open insta' in query:
            pywhatkit.search('https:////www.instagram.com')

        elif 'play music' in query:
            # music_dir = 'C:\\Users\\Abhishek\\Desktop\\songs\\y music'
            # songs = os.listdir(music_dir)
            # print(songs)
            # os.startfile(os.path.join(music_dir, songs[3]))
            pywhatkit.playonyt('music mashup')
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Abhishek\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke('en'))
        # elif 'play' and 'youtube' in query:
        #     query = query.replace('youtube', '')
        #     query = query.replace('play', '')
        #     pywhatkit.playonyt(query)
        elif 'on youtube' in query:
            l1 = ['on', 'on youtube', 'play', 'at']
            l1 = ['on youtube', 'play', 'at youtube', 'jarvis', 'youtube', ]
            for word in l1:
                query = query.replace(word, ' ')

            print(f'playing {query} on youtube sir...')
            speak(f'playing {query} on youtube sir')
            pywhatkit.playonyt(query)
        elif 'meaning' in query:
            pywhatkit.search(query)
            l1 = ['meaning', 'in hindi', 'on google', 'translate']
            for word in l1:
                query = query.replace(word, '')
            speak(f'the meaning of the word {query} is on your screen sir')

        elif 'shutdown' in query:
            speak('quiting jarvis...')
            break
            