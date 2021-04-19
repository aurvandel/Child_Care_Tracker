from django.core.mail import send_mail
from background_task import background
from tracker.models import Contact, Todo
from django.utils import timezone
import datetime
from google.cloud import texttospeech
from playsound import playsound
import os

# timezone.make_naive to get time in timezone

def sayMessage(msg):
    # Setup for tts
    tts_client = texttospeech.TextToSpeechClient()
    params = texttospeech.VoiceSelectionParams(language_code='en-US', ssml_gender=texttospeech.SsmlVoiceGender.FEMALE)
    audio = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    # Say the whats coming due
    si = texttospeech.SynthesisInput(text=msg)
    response = tts_client.synthesize_speech(input=si, voice=params, audio_config=audio)
    f = open('task.mp3', 'wb')
    f.write(response.audio_content)
    f.close()
    playsound('task.mp3')

    if os.path.exists("task.mp3"):
        os.remove("task.mp3")


@background(schedule=0)
def notify_users():
    #print("task ran at ", timezone.make_naive(timezone.now()))

    # get tasks that are due soon and put in list
    msgs = []
    now = (timezone.now())
    withinTime = now + timezone.timedelta(minutes=1)
    tasks = Todo.objects.filter(todoTime__range=(now, withinTime))
    
    if tasks.exists():
        for task in tasks:
            if not task.messageSent:
                print(task.getMessage)
                msgs.append(task.getMessage())
                sayMessage(task.getMessage())


    # get users addresses
    fromEmail = 'parkergw@gmail.com'

    user = Contact.objects.get(pk=2)

    addresses = []
    users = Contact.objects.all()
    if users.exists():
        for user in users:
            addresses.append(user.getEmail())

    # send messages
    for msg in msgs:

        send_mail(
            '',
            msg,
            fromEmail,
            addresses,
            fail_silently=False,
        )
        
        