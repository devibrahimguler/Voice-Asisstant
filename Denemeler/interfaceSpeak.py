from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QMovie
from PyQt5 import QtWidgets
from PyQt5 import QtCore
import sys


class InterfaceSpeak(QMainWindow):
    def __init__(self):
        super(InterfaceSpeak, self).__init__()

        self.centralwidget = QtWidgets.QWidget(self)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.movie = QMovie("Database/speak.gif")
        self.timer = QTimer(self)
        self.setWindowTitle("Arin Speak")
        self.setGeometry(700, 350, 350, 350)
        self.initUI()
        self.show()

    def initUI(self):
        self.centralwidget.setObjectName("centralwidget")

        self.label.setGeometry(QtCore.QRect(0, 0, 350, 350))
        self.label.setMinimumSize(QtCore.QSize(350, 350))
        self.label.setMaximumSize(QtCore.QSize(350, 350))
        self.label.setObjectName("Speak")

        self.setCentralWidget(self.centralwidget)

        self.label.setMovie(self.movie)
        self.speakStart()

        self.timer.singleShot(4000, self.speakStop)

    def speakStart(self):
        self.movie.start()

    def speakStop(self):
        self.movie.stop()
        self.close()


def speakApp():
    app = QApplication(sys.argv)
    win = InterfaceSpeak()
    win.show()
    sys.exit(app.exec_())
