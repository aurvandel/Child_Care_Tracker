from django.core.mail import send_mail
from background_task import background
from tracker.models import Contact, Todo
from django.utils import timezone
import datetime
from google.cloud import texttospeech
import os
import time
import pygame
import logging

# TODO: implement logging

# timezone.make_naive to get time in timezone

def sayMessage(msg):
    print("speeking", msg)
    # Setup for tts
    tts_client = texttospeech.TextToSpeechClient()
    params = texttospeech.VoiceSelectionParams(language_code='en-US', ssml_gender=texttospeech.SsmlVoiceGender.FEMALE)
    audio = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.LINEAR16)
    # Say the whats coming due
    si = texttospeech.SynthesisInput(text=msg)
    response = tts_client.synthesize_speech(input=si, voice=params, audio_config=audio)
    f = open('task.wav', 'wb')
    f.write(response.audio_content)
    f.close()
    
    pygame.mixer.init()
    pygame.mixer.music.load(open('task.wav', "rb"))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

    if os.path.exists("task.wav"):
        os.remove("task.wav")


def getMsgs():
    # get tasks that are due soon and put in list
    print("getting msgs")
    msgs = []
    #now = (timezone.now())
    now = datetime.datetime.now()
    withinTime = now + timezone.timedelta(minutes=1)
    print(now, withinTime)
    tasks = Todo.objects.filter(todoTime__range=(now, withinTime))
    tasksToday = Todo.objects.filter(todoDate__date=datetime.date.today())
    # change message to get rid of seconds 
    if tasks.exists() and tasksToday.exists():
        for task in tasks:
            if not task.messageSent:
                print(task.getMessage)
                msgs.append(task.getMessage())
                sayMessage(task.getMessage())
    
    return msgs


def getEmailAddresses():
    print("getting contacts")
    addresses = []
    users = Contact.objects.all()
    if users.exists():
        for user in users:
            addresses.append(user.getEmail())
    return addresses


@background(schedule=0)
def notify_users():
    print("starting msg send")
    msgs = getMsgs()
    print(msgs)
    # get users addresses
    fromEmail = 'parkergw@gmail.com'

    addresses = getEmailAddresses()
    print(addresses)
    # send messages
    for msg in msgs:
        send_mail(
            '',
            msg,
            fromEmail,
            addresses,
            fail_silently=False,
        )
    print("Done")
        
