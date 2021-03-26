import speech_recognition as sr 
import os

print(os.getcwd())

r = sr.Recognizer()

harvard = sr.AudioFile('tracker/harvard.wav')
with harvard as source:
    audio = r.record(source)

r.recognize_google(audio)
