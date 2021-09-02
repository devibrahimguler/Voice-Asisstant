from datetime import datetime
import arinSould as Sould
import arinAsking as AA
import arinListen as AL
import arinSpeak as AS


def arinResponse(voice):
    if 'ismin ne' in voice:
        AS.arinSpeak(Sould.name())
    if 'merhaba' in voice:
        AS.arinSpeak('merhaba' + Sould.talkToName())
    if 'nasılsın' in voice:
        AS.arinSpeak(Sould.totalAffect())
        while True:
            asking = AL.arinListen().lower()
            print(asking)
            if 'iyim' in asking:
                AS.arinSpeak('sevindim birşey istersen söyle')
            elif 'kötüyüm' in asking:
                AS.arinSpeak('üzüldüm yardımcı olabilir miyim')
            else:
                AS.arinSpeak('yardımcı olabilecegim bir konu var mı')
                break
    if 'saat kaç' in voice:
        AS.arinSpeak(datetime.now().strftime("%X"))
    if 'hava nasıl' in voice:
        AS.arinSpeak(Sould.watherRead())
    if 'arama yap' in voice:
        AS.arinSpeak('ne aramak istiyorsun')
        while True:
            asking = AL.arinListen().lower()
            print(asking)
            if 'kapat' in asking:
                break
            AA.asks(asking)
    if 'görüşürüz' in voice:
        AS.arinSpeak('görüşürüz')
        exit()
