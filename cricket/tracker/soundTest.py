#gTTS doesn't work?
from gtts import gTTS 
from playsound import playsound 
text = "This is in english language"
var = gTTS(text = text,lang = 'en',tld='com') 
var.save('eng.mp3') 
playsound('.\eng.mp3')