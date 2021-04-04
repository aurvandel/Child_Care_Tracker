import speech_recognition as sr 
import os
import json
from dotenv import load_dotenv
load_dotenv()

r = sr.Recognizer()

harvard = sr.AudioFile('harvard.wav')
with harvard as source:
    audio = r.record(source)

GOOGLE_CLOUD_SPEECH_CREDENTIALS = json.dumps(os.getenv('GOOGLE_CLOUD_SPEECH_CREDENTIALS'))

try:
    print("Google Cloud Speech recognition for harvard with different sets of preferred phrases:")
    print(r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))
print(r.recognize_google(audio))
