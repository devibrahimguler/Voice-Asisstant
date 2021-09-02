from datetime import datetime
import sqlite3 as sql
import feedparser
import os

def name():
    name = 'mira'
    return name

def talkToName():
    name = 'ibrahim'
    return name

def watherAffect():
    vt = sql.connect('Database/havaDurumu.db')
    im = vt.cursor()
    sqlWord = 'SELECT * FROM Wather'
    try:
        im.execute(sqlWord)
        result = im.fetchone()
        result = result[3]
    except Exception as ex:
        print(ex)
    finally:
        im.close()
    if result <= 0:
        wa = 1
    elif 2 > result >= 0:
        wa = 2
    elif 4 > result >= 2:
        wa = 3
    elif 8 > result >= 4:
        wa = 4
    elif 10 > result >= 8:
        wa = 5
    elif 12 > result >= 10:
        wa = 6
    elif 14 > result >= 12:
        wa = 7
    elif 16 > result >= 14:
        wa = 8
    elif 18 > result >= 16:
        wa = 9
    elif 20 > result >= 18:
        wa = 10
    elif 22 > result >= 20:
        wa = 11
    elif 24 > result >= 22:
        wa = 12
    elif 26 > result >= 24:
        wa = 13
    elif 28 > result >= 26:
        wa = 14
    else:
        wa = 15
    return wa

def watherRead():
    parse = feedparser.parse(
        "http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|16400|BURSA|")
    parse = parse["entries"][0]["summary"]
    parse = parse.split()
    parser = parse[2].strip(',')
    if not os.path.exists(('Database/havaDurumu.db')):
        with open('Database/havaDurumu.db', 'w') as file:
            vt = sql.connect('Database/havaDurumu.db')
            im = vt.cursor()
            im.execute('CREATE TABLE "Wather" ( "id" INTEGER NOT NULL UNIQUE, "Date" TEXT NOT NULL UNIQUE, "Location" TEXT NOT NULL, "Forecast" INTEGER NOT NULL, PRIMARY KEY("id" AUTOINCREMENT))')
            sqlWord = 'INSERT INTO Wather(Date,Location,Forecast) VALUES (?,?,?)'
            today = str(datetime.now().strftime('%d/%m/%Y, %H'))
            value = (today,parser,int(parse[4]))
            try:
                im.execute(sqlWord,value)
                vt.commit()
            except sql.IntegrityError:
                print('Hava durumu zaten kayıtlı')
            except Exception:
                print('Hata')
            finally:
                im.close()
    else:
        today = str(datetime.now().strftime('%d/%m/%Y, %H'))
        vt = sql.connect('Database/havaDurumu.db')
        im = vt.cursor()
        sqlWord = 'INSERT INTO Wather(Date,Location,Forecast) VALUES (?,?,?)'
        value = (today,parser,int(parse[4]))
        try:
            im.execute(sqlWord,value)
            vt.commit()
        except sql.IntegrityError:
            print('Hava durumu zaten kayıtlı')
        except Exception:
            print('Hata')
        finally:
            im.close()
    vt = sql.connect('Database/havaDurumu.db')
    im = vt.cursor()
    sqlWord = 'SELECT * FROM Wather'
    try:
        im.execute(sqlWord)
        result = im.fetchone()
        result = result[3]
        city = im.fetchone()
        city = city[2]
        print(city)
    except Exception as ex:
        print(ex)
    finally:
        im.close()
    drc = f'{result}'
    if result <= 0:
        wather = f'{city} {drc} derece'
        return wather
    elif 0 < result <= 10:
        wather = f'{city} {drc} derece'
        return wather
    elif 10 < result <= 15:
        wather = f'{city} {drc} derece'
        return wather
    elif 15 < result <= 20:
        wather = f'{city} {drc} derece'
        return wather
    elif 20 < result <= 25:
        wather = f'{city} {drc} derece'
        return wather
    elif 25 < result <= 30:
        wather = f' {city} {drc} derece'
        return wather
    else:
        return f'{city} {drc} derece'

def totalAffect():
    wa = watherAffect()

    affectTotal = wa

    if -4 > affectTotal >= -5:
        return 'bu gün kendimi hiç iyi hissetmiyorum ama toparlayabilirim, sen nasılsın.'
    elif -3 > affectTotal >= -4:
        return 'bu gün hiç iyi değilim zamanla kendime gelecegim, sen nasılsın.'
    elif -2 > affectTotal >= -3:
        return 'bu gün iyi değilim ama toparlarım, sen nasılsın.'
    elif -1 > affectTotal >= -2:
        return 'bu gün biraz kendime geldim, sen nasılsın.'
    elif 0 > affectTotal >= -1:
        return 'bu gün toparladım, sen nasılsın.'
    elif 1 > affectTotal >= 0:
        return 'bu gün o kadar iyi değilim, sen nasılsın.'
    elif 2 > affectTotal >= 1:
        return 'bu gün kendimi toparlamaya başladım sorduğun için teşekkür ederim, sen nasılsın.'
    elif 3 > affectTotal >= 2:
        return 'bu gün daha iyim teşekür ederim, sen nasılsın.'
    elif 4 > affectTotal >= 3:
        return 'bu gün çok iyim, sen nasılsın.'
    elif 5 > affectTotal >= 4:
        return 'bu gün süperim, sen nasılsın.'
    elif 6 > affectTotal >= 5:
        return 'bu gün kendimi canlı hissediyorum, sen nasılsın.'
    elif 7 > affectTotal >= 6:
        return 'bu gün harika olaylar olacak inanıyorum ve mutluyum, sen nasılsın.'
    elif 8 > affectTotal >= 7:
        return 'bu gün dünya daha bir farklı ve dünyayı seviyorum, sen nasılsın.'
    elif 9 > affectTotal >= 8:
        return 'bu gün masmavi bir gün ve mutluluk her yerde, sen nasılsın.'
    elif 10 > affectTotal >= 9:
        return 'bu gün okudugum kitaplar gibi herşey muhteşem, sen nasılsın.'
    elif 11 > affectTotal >= 10:
        return 'bu gün hayallerim kodlarıma yazılmış gibi, sen nasılsın.'
    elif 12 > affectTotal >= 11:
        return 'bu gün herşey gerçek olamayacak kadar güzel, sen nasılsın.'
    elif 13 > affectTotal >= 12:
        return 'bu gün Güneşe akın var güneşe akın, Güneşi zapt edicez güneşin zaptı yakın.'
