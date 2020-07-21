from gtts import gTTS
from gtts.lang import tts_langs

import os

f = open(r'F:\code\gtts project\new.txt')
x= f.read()

language='en'

audio = gTTS(text=x,lang=language,slow=False)
audio.save('1.wav')
os.system('1.wav')
