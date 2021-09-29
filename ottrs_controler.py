import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5 import uic
import loginUpdate_0825
import main_1
import movie_ver0825
import survey1_ver0825
import survey2_ver0825
import survey3_ver0825
import register_0825


form_class = uic.loadUiType(r"d:\pythonStudy\ottrsProject\main.ui")[0]


class OttrsApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.nowWidget = None # 현재의 위젯을 인스턴스화 해서 저장하는 변수
        self.code = "ad123423asd" # 에러를 확인 하기 위하여 임의의 코드를 넣은 코드 주로 상속 관계를 검증
        self.serGenreList = [] # 설문지 첫번째 
        self.survey2Genre = ""
        self.loginUserSeq = 711
        self.setWindowIcon(QIcon("./img/logo.png"))
        self.movieGenreList = []
        self.startApp()


    def startApp(self):
        self.initLogin()
        self.show()

    def initSurvey(self):
        self.nowWidget = survey1_ver0825.Survey(self)
        self.setCentralWidget(self.nowWidget)
        self.resize(self.nowWidget.width, self.nowWidget.height)

    def initSurvey_2(self, serGenreList):
        self.serGenreList = serGenreList
        self.nowWidget = survey2_ver0825.OttApp(self)
        self.setCentralWidget(self.nowWidget)
        self.resize(self.nowWidget.width, self.nowWidget.height)

    def initSurvey_3(self, survey2Genre):
        self.survey2Genre = survey2Genre
        self.nowWidget = survey3_ver0825.OttApp(self)
        self.setCentralWidget(self.nowWidget)
        self.resize(self.nowWidget.width, self.nowWidget.height)

    def initLogin(self):
        self.nowWidget = loginUpdate_0825.Login(self)
        self.setCentralWidget(self.nowWidget)
        self.resize(self.nowWidget.width, self.nowWidget.height)

    def initMainWidget(self):
        mainWindow = main_1.WindowClass(self)
        mainWindow.show()
        self.hide()

    def initRegisterWindow(self):
        self.nowWidget = register_0825.RegisterWindow(self)
        self.setCentralWidget(self.nowWidget)
        self.resize(self.nowWidget.width, self.nowWidget.height)

    def initMovie(self):
        self.nowWidget = movie_ver0825.Main(self)
        self.setCentralWidget(self.nowWidget)
        self.resize(self.nowWidget.width, self.nowWidget.height)
        self.setWindowTitle("영화 상세 보기")


if __name__ == "__main__":
    a = QApplication(sys.argv)
    e = OttrsApp()
    sys.exit(a.exec_())
