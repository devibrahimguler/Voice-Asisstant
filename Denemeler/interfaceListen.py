from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QMovie
from PyQt5 import QtWidgets
from PyQt5 import QtCore
import sys


class InterfaceListen(QMainWindow):
    def __init__(self):
        super(InterfaceListen, self).__init__()

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.centralwidget = QtWidgets.QWidget(self)
        self.movie = QMovie("Database/listen.gif")
        self.timer = QTimer(self)
        self.setWindowTitle("Arin Listen")
        self.setGeometry(700, 350, 350, 350)
        self.initUI()
        self.show()

    def initUI(self):
        self.centralwidget.setObjectName("centralwidget")

        self.label.setGeometry(QtCore.QRect(0, 0, 350, 350))
        self.label.setMinimumSize(QtCore.QSize(350, 350))
        self.label.setMaximumSize(QtCore.QSize(350, 350))
        self.label.setObjectName("Listen")

        self.setCentralWidget(self.centralwidget)

        self.label.setMovie(self.movie)
        self.listenStart()

        self.timer.singleShot(6000, self.listenStop)

    def listenStart(self):
        self.movie.start()

    def listenStop(self):
        self.movie.stop()
        self.close()


def listenApp():
    app = QApplication(sys.argv)
    win = InterfaceListen()
    win.show()
    sys.exit(app.exec_())
