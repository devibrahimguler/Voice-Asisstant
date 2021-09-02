from gtts import gTTS
import random
import os

def arinSpeak(string):
    tts = gTTS(text=string, lang='tr')
    rand = random.randint(1, 10000)
    file = 'audio-' + str(rand) + '.mp3'
    tts.save(file)
    os.system("afplay " + file)
    os.remove(file)
