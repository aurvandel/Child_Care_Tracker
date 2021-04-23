from google.cloud import texttospeech
from playsound import playsound

tts_client = texttospeech.TextToSpeechClient()
params = texttospeech.VoiceSelectionParams(language_code='en-US', ssml_gender=texttospeech.SsmlVoiceGender.FEMALE)
audio = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
si = texttospeech.SynthesisInput(text='Peter Piper picked a peck of pickled peppers.')
response = tts_client.synthesize_speech(input=si, voice=params, audio_config=audio)
f = open('en_us_female.mp3', 'wb')
f.write(response.audio_content)
f.close()
playsound('en_us_female.mp3')
