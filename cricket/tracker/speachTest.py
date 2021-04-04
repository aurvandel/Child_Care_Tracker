import speech_recognition as sr 
import os

r = sr.Recognizer()

harvard = sr.AudioFile('harvard.wav')
with harvard as source:
    audio = r.record(source)

GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"test1707-8f2ee577f207.json"
try:
    print("Google Cloud Speech recognition for \"numero\" with different sets of preferred phrases:")
    print(r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))
print(r.recognize_google(audio, show_all=True))
