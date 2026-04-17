import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
from PIL import Image
import time

fs = 44100
seconds = 3

print("Get ready...")
time.sleep(1)

print("Speak now...")
recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
sd.wait()

write("input.wav", fs, recording)

r = sr.Recognizer()
with sr.AudioFile("input.wav") as source:
    audio = r.record(source)

try:
    text = r.recognize_google(audio).lower()
    print("You said:", text)

    gesture_map = {
        "hello": "hello.jpg",
        "hi":"hello.jpg",
        "good morning":"good1.png",
        "good afternoon":"good2.png",
        "good evening":"good3.png",

        "thank you": "thankyou.jpg",
        "thanks": "thankyou.jpg",
        "please": "please.png",
        "sorry": "sorry.png",
        "excuse me": "excuseme.png",

        "yes": "yes.png",
        "no": "no.png",
        "ok": "ok.png",
        "fine":"fine.png",
        "i understand":"understand.png",

        "help": "help.png",
        "wait": "wait.png",
        "stop": "stop.png",
        "come": "come.png",
        "go": "go.png",

        "what": "what.png",
        "where": "where.png",
        "when": "when.png",
        "who": "who.png",
        "why": "why.png",

    }
    found = False
    for key in gesture_map:
        if key in text:
            img = Image.open("handsigns/" + gesture_map[key])
            img.show()
            found = True
            break

    if not found:
        print("No matching gesture found")

except:
    print("Could not understand audio")