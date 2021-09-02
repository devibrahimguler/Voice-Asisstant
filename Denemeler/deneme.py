from pygame import mixer
# import numpy as np
# import matplotlib
# import matplotlib.pyplot as plt
#
# import librosa
# import librosa.display
#
# x_1, fs = librosa.load('')
# # And a second version, slightly faster.
# x_2, fs = librosa.load('audio/sir_duke_fast.ogg')
#
# fig, ax = plt.subplots(nrows=2, sharex=True, sharey=True)
# librosa.display.waveplot(x_1, sr=fs, ax=ax[0])
# ax[0].set(title='Slower Version $X_1$')
# ax[0].label_outer()
#
# librosa.display.waveplot(x_2, sr=fs, ax=ax[1])
# ax[1].set(title='Faster Version $X_2$')

# import matplotlib.pyplot as plt
# import numpy as np
#
# def deVoice(string):
#     char = 0
#     for i in string:
#         if 'a' in i:
#             char += 0.10
#         elif 'b' in i:
#             char += 0.20
#         elif 'c' in i:
#             char += 0.30
#         elif 'ç' in i:
#             char += 0.40
#         elif 'd' in i:
#             char += 0.50
#         elif 'e' in i:
#             char += 0.60
#         elif 'f' in i:
#             char += 0.70
#         elif 'g' in i:
#             char += 0.80
#         elif 'ğ' in i:
#             char += 0.90
#         elif 'h' in i:
#             char += 0.100
#         elif 'i' in i:
#             char += 0.110
#         elif 'ı' in i:
#             char += 0.120
#         elif 'j' in i:
#             char += 0.130
#         elif 'k' in i:
#             char += 0.140
#         elif 'l' in i:
#             char += 0.150
#         elif 'm' in i:
#             char += 0.160
#         elif 'n' in i:
#             char += 0.170
#         elif 'o' in i:
#             char += 0.180
#         elif 'ö' in i:
#             char += 0.190
#         elif 'p' in i:
#             char += 0.200
#         elif 'r' in i:
#             char += 0.210
#         elif 's' in i:
#             char += 0.220
#         elif 'ş' in i:
#             char += 0.230
#         elif 't' in i:
#             char += 0.240
#         elif 'u' in i:
#             char += 0.250
#         elif 'ü' in i:
#             char += 0.260
#         elif 'v' in i:
#             char += 0.270
#         elif 'y' in i:
#             char += 0.280
#         elif 'z' in i:
#             char += 0.290
#         else:
#             char += 0
#     return char
# string = 'bu bir denemedir'
# rows = 1
# cols = 1
# isim = 'isim'
# n = rows * cols
# i = np.int_(deVoice(string))
# fig, axes = plt.subplots(rows, cols, figsize=(10, 12))
# r = i // cols
# c = i % cols
# ax = axes[r][c]
# ax.plot(np.int_(deVoice(string)))
# ax.set_yticks(np.arange(-1.2, 1.2, 0.2))
# label = isim
# ax.set_title(isim)
#
# plt.show()


# from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.QtGui import QMovie
# from PyQt5 import QtWidgets
# from PyQt5 import QtCore
# import sys
#
# class Listen(QMainWindow):
#     def __init__(self):
#         super(Listen, self).__init__()
#
#         self.setWindowTitle("Arin Listen")
#         self.setGeometry(700,350,350,350)
#         self.initUI()
#         self.show()
#     def initUI(self):
#         self.centralwidget = QtWidgets.QWidget(self)
#         self.centralwidget.setObjectName("centralwidget")
#
#         # create label
#         self.label = QtWidgets.QLabel(self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(0, 0, 350, 350))
#         self.label.setMinimumSize(QtCore.QSize(350, 350))
#         self.label.setMaximumSize(QtCore.QSize(350, 350))
#         self.label.setObjectName("label")
#
#         self.setCentralWidget(self.centralwidget)
#
#         self.movie = QMovie("speak.gif")
#         self.label.setMovie(self.movie)
#         self.movie.start()
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     win = Listen()
#     win.show()
#     sys.exit(app.exec_())


# from datetime import datetime
# now = datetime.now().strftime('%d/%m/%Y')
# print(now)


# def strDecoder(char):
#     x = 0
#     if char == "a":
#         x += 10
#         return x
#     elif char == "b":
#         x += 20
#         return x
#     elif char == "c":
#         x += 30
#         return x
#     elif char == "ç":
#         x += 40
#         return x
#     elif char == "d":
#         x += 50
#         return x
#     elif char == "e":
#         x += 60
#         return x
#     elif char == "f":
#         x += 70
#         return x
#     elif char == "g":
#         x += 80
#         return x
#     elif char == "ğ":
#         x += 90
#         return x
#     elif char == "h":
#         x += 100
#         return x
#     elif char == "ı":
#         x += 110
#         return x
#     elif char == "i":
#         x += 120
#         return x
#     elif char == "j":
#         x += 130
#         return x
#     elif char == "k":
#         x += 140
#         return x
#     elif char == "l":
#         x += 150
#         return x
#     elif char == "m":
#         x += 160
#         return x
#     elif char == "n":
#         x += 170
#         return x
#     elif char == "o":
#         x += 180
#         return x
#     elif char == "ö":
#         x += 190
#         return x
#     elif char == "p":
#         x += 200
#         return x
#     elif char == "r":
#         x += 210
#         return x
#     elif char == "s":
#         x += 220
#         return x
#     elif char == "ş":
#         x += 230
#         return x
#     elif char == "t":
#         x += 240
#         return x
#     elif char == "u":
#         x += 250
#         return x
#     elif char == "ü":
#         x += 260
#         return x
#     elif char == "v":
#         x += 270
#         return x
#     elif char == "y":
#         x += 280
#         return x
#     elif char == "z":
#         x += 290
#         return x
#     else:
#         return x


# class MainWindows(QMainWindow):
#     def __init__(self):
#         super(MainWindows, self).__init__()

#         self.setWindowTitle('Title')
#         self.setGeometry(700,300,500,500)


#     def initUI(self, char):
#         for i in char:
#             for j in range(len(char)):

#                 self.btn = QtWidgets.QPushButton(self)
#                 self.btn.setText('-')
#                 self.btn.resize(i,10)
#                 self.btn.move(100,100)
#                 print(j,i)

# def app(char):
#     app = QApplication(sys.argv)
#     win = MainWindows()
#     win.show()
#     win.initUI(char)
#     win.show()
#     sys.exit(app.exec_())

# def deCode(char):
#     chars = []
#     for i in char:
#         chars.append(strDecoder(i))
#     return chars

# while True:
#     chars = 'Nasıl Yardımcı Olabilirim?'
#     app(deCode(chars))
#     speak(chars)
#     voice = listen()
#     voice = voice.lower()
#     responce(voice)


# from selenium.webdriver.common.keys import Keys
# from selenium import webdriver
# import time
# browser = webdriver.Chrome()
# browser.get('https://www.instagram.com')
# time.sleep(2)
# browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('muntazif')
# time.sleep(2)
# browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('130419IG', Keys.ENTER)
# time.sleep(3)
# browser.get('https://www.instagram.com/explore/')
# time.sleep(3)
# while True:
#   browser.find_element_by_xpath('/html/body').send_keys(Keys.SPACE)
#   time.sleep(2)

# with open('voice.txt', 'r', encoding='utf-8') as file:
#   file.seek(0)
#   text = file.read()
#   text = text.replace('{','')
#   text = text.split('}')
#   for i in text:
#     if 'nasılsın' in i :
#       va+=1
#     if 'teşekkür ederim' in i:
#       va+=1
#     if 'çok iyisin' in i:
#       va+=1
#     if 'zekisin' in i:
#       va+=1
#     if 'sus' in i:
#       va+=-1
#     if 'giri zekalı' in i:
#       va+=-1
#     if 'seni sevmiyorum' in i:
#       va+=-1
#     if 'bir şeyi beceremedin' in i:
#       va+=-1
#     if 'seni seviyorum' in i:
#       va+=10
#     if 'özür dilerim' in i:
#       va+=100
#   return va


# import json
# with open('havaDurumu.json', 'r') as file:
#   file.seek(0)
#   list = file.read()
#   result = json.loads(list)
#   print(result['time'])

# import feedparser
# # locCode=EUR|TR|06420|ANKARA| > KITA|ULKE|POSTAKODU|IL
# def hava():
#     parse = feedparser.parse("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|16400|BURSA|")
#     parse = parse["entries"][0]["summary"]
#     parse = parse.split()
#     print (parse[2], parse[4], parse[5])
#     return (hava)
# hava()


# from selenium.webdriver.common.keys import Keys
# from selenium import webdriver
# from bs4 import BeautifulSoup
# import requests
# import time
# browser = webdriver.Chrome(executable_path='Database/chromedriver.exe')
# browser.get('https://sozluk.gov.tr')
# browser.minimize_window()
# time.sleep(1)
# browser.find_element_by_xpath('//*[@id="tdk-srch-input"]').send_keys('arzu',Keys.ENTER)
# time.sleep(1)
# title = browser.find_elements_by_css_selector('div[id=anlamlar-gts0] p')
# quen = []
# for i in title:
#   quen.append(i.text)
# print(quen)
# meaning = quen[0].split(':')
# desc = meaning[0]
# meaning = meaning[1].split('.')
# meaning = meaning[0].lstrip()
# meaning = meaning[1::]
# restr = 'söylediğin kelimenin anlamı ' +desc+' ve onla ilgili cümle' + meaning


# time.sleep(1)
# url = browser.current_url
# html = requests.get(url).content
# soup = BeautifulSoup(html, 'html.parser')
# result = soup.find_all('p')
# for i in result:
#   print(str(i) + '\n')
