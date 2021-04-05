from __future__ import print_function

import speech_recognition as sr
import os
import json
import sys
from dotenv import load_dotenv
load_dotenv()

def stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

r = sr.Recognizer()

mic = sr.Microphone()
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

# GOOGLE_CLOUD_SPEECH_CREDENTIALS = json.dumps(os.getenv('GOOGLE_CLOUD_SPEECH_CREDENTIALS'))
#
# try:
#     print("Google Cloud Speech recognition for harvard with different sets of preferred phrases:")
#     print(r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
# except sr.UnknownValueError:
#     print("Google Cloud Speech could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Cloud Speech service; {0}".format(e))
try:
    response = r.recognize_google(audio)
except sr.RequestError:
    stderr("API unavailable")
except sr.UnknownValueError:
    # speech was unintelligible
    stderr("Unable to recognize speech")