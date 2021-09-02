import os

import arinListen as AL
import arinResponse as AR
import arinSpeak as AS

baseDir = os.path.dirname(os.path.abspath(__file__))
listDir = os.listdir(baseDir)
for i in listDir:
    if '.mp3' in listDir:
        os.remove(i)


def start():
    while True:
        startArin = AL.arinListen(open=True).lower()
        print(startArin)
        if 'mira' in startArin:
            AS.arinSpeak('nasıl yardımcı olabilirim'.lower())
            while True:
                voice = AL.arinListen().lower()
                print(voice)
                if 'uyu' in voice:
                    break
                AR.arinResponse(voice)


start()
