from PyQt5 import QtWidgets, QtCore, QtGui
import sys, time
from PyQt5.QtCore import QUrl
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtWebEngineCore
from PyQt5.QtWebEngineWidgets import QWebEngineSettings


class YoutubeWidget(QtWidgets.QMainWindow):
    def __init__(self):
        QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        super(YoutubeWidget, self).__init__()
        self.centralwid = QtWidgets.QWidget(self)
        self.vlayout = QtWidgets.QVBoxLayout()
        self.webview = QtWebEngineWidgets.QWebEngineView()
        self.webview.setUrl(QUrl("https://www.youtube.com/embed/HxM1aZ6l3M0?autoplay=0"))
        self.vlayout.addWidget(self.webview)
        self.centralwid.setLayout(self.vlayout)
        self.setCentralWidget(self.centralwid)
        self.show()


app = QtWidgets.QApplication([])
ex = YoutubeWidget()
sys.exit(app.exec_())