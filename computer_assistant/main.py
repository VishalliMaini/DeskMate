import datetime
import speech_recognition as sr
import os
import webbrowser
import subprocess, sys
import cv2
import openai
from conf import apikey
import random
def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt}\n**********************\n\n"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text += response['choices'][0]['text']
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/prompt-{random.randint(1, 2345678)}", "w") as f:
        f.write(text)
chatStr=""


def say(text):
    #for female voice -v en+f3 is used
    os.system(f"espeak -v en+f3 '{text}'")

def takeCommand():
    r=sr.Recognizer();
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio=r.listen(source, phrase_time_limit=3)
        try:
            query=r.recognize_google(audio,language="en-in")
            print(f"User said:'{query}'")
            return query
        except Exception as e:
            return "Some Error Occured, I am Sorry."

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Vishalli: {query}\nNandini:"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    reply = response["choices"][0]["text"]
    say(reply)
    chatStr += f"{reply}\n"
    return reply
if __name__ == '__main__':
    print("PyCharm")
    say("Hello, I am Nandini AI")
    while True:
        print("Listening....")
        query=takeCommand()
        sites=[["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"],["gmail","https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} mam....")
                webbrowser.open(site[1])

        if "play music" in query:
            say(f"playong mam....")
            musicpath="/home/vishalli/Music/obsessed.mp3"
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, musicpath])


        if "time" in query:
            t=datetime.datetime.now().strftime("%I:%M %p")
            say(f" Mam the time is {t}")

        if "camera" in query.lower():
            capture = cv2.VideoCapture(0, cv2.CAP_V4L)
            while True:
                ret, frame = capture.read()
                cv2.imshow('Camera', frame)

            # Press 'q' to exit the camera
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            capture.release()
            cv2.destroyAllWindows()

        if "open vs code" in query.lower():
            say("Opening Visual Studio Code application.")
            subprocess.Popen(["code"])

        if "using ai" in query.lower():
            ai(prompt=query)

        else:
            chat(query)