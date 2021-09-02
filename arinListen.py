import speech_recognition as sr

import arinSpeak as AS

r = sr.Recognizer()
m = sr.Microphone()


def arinListen(ask=False,open =False):
    with m as source:
        if ask:
            AS.arinSpeak(ask)
        audio = r.listen(source, phrase_time_limit=5)
        voice = ''
        try:
            voice = r.recognize_google(audio, language='tr-TR')
        except sr.UnknownValueError:
            if open:
                print('sistem uyoyor')
            else:
                AS.arinSpeak('Anlamadım')
        except sr.RequestError:
            if open:
                print('Sistem de uyuyor')
            else:
                AS.arinSpeak('Sistem Çalışmıyor')
        return voice


def arinOpen():
    with m as source:
        audio = r.listen(source, phrase_time_limit=None)
        voice = ''
        try:
            voice = r.recognize_google(audio, language='tr-TR')
        except sr.UnknownValueError:
            print('She sleeping at now!')
        except sr.RequestError:
            print('System does not working at now!')
        return voice
