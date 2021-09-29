import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import movie_ver0825
import cx_Oracle
from random import randint
from engine_1 import getMovieGenreList

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType(r".\main.ui")[0]


class AfSearchMovieClass(QMainWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.setGeometry(100, 100, 600, 600)
        self.parent = parent
        self.lbany = QLabel(self)

        self.initUI()

    def initUI(self):
        self.lbany.setGeometry(200, 200, 180, 240)
        self.lbanybackground = QPixmap(r"E:\pythonStudy\ottrsProject\img\poster/" + self.parent.movieimgno)
        self.lbany.setPixmap(self.lbanybackground)
        self.show()


class Movie:
    def __init__(self):
        self.MOVIESEQ = ""
        self.MOVIETITLE = ""
        self.MOVIECODE = ""
        self.MOVIEPLOT = ""
        self.MOVIEMODE = ""
        self.MOVIEPRICE = ""
        self.MOVIEPOSTRIMG = ""
        self.MOVIEDIRECTOR = ""
        self.MOVIEGENRE = ""
        self.MOVIEIMGNAME = ""


# 화면을 띄우는데 사용되는 Class 선언
def getConn():
    # conn = cx_Oracle.connect("scott", "scott1234!", "orcl.cu1tbymhc2wb.ap-northeast-2.rds.amazonaws.com:1521/orcl")
    return cx_Oracle.connect("scott", "tigertiger", "orcl.cgnlgvycsnjd.us-east-2.rds.amazonaws.com:1521/orcl")


class WindowClass(QMainWindow, form_class):
    def __init__(self, window):
        super().__init__(window)
        # print("main_1 is called!")
        self.window = window
        self.imgDir = "./img/poster/"
        self.setupUi(self)
        self.btnUp1.setStyleSheet('QPushButton {background-color : white; color : black}')
        self.btnUp2.setStyleSheet('QPushButton {background-color : white; color : black}')
        self.btnUp3.setStyleSheet('QPushButton {background-color : white; color : black}')
        self.btnDown1.setStyleSheet('QPushButton {background-color : white; color : black}')
        self.btnDown2.setStyleSheet('QPushButton {background-color : white; color : black}')
        self.btnDown3.setStyleSheet('QPushButton {background-color : white; color : black}')
        self.setStyleSheet("background-color : white")
        self.idx = 1
        qPixmapVar = QPixmap()
        self.btnUp1.clicked.connect(self.PageUp)
        self.btnUp2.clicked.connect(self.PageUp)
        self.btnUp3.clicked.connect(self.PageUp)
        self.btnDown1.clicked.connect(self.PageDown)
        self.btnDown2.clicked.connect(self.PageDown)
        self.btnDown3.clicked.connect(self.PageDown)
        # self.loadImageFromFile()
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(150)
        self.movieList = []
        # self.initMovieList()
        print("----")
        self.initMovieListByGenre()

        # 검색
        self.searchBtn.clicked.connect(self.searchMovie)
        # print(self.idx, "init")
        self.lb1.mousePressEvent = self.doSomething1
        self.lb2.mousePressEvent = self.doSomething2
        self.lb3.mousePressEvent = self.doSomething3
        self.lb4.mousePressEvent = self.doSomething4
        self.lb5.mousePressEvent = self.doSomething5
        self.lb6.mousePressEvent = self.doSomething6
        self.lb7.mousePressEvent = self.doSomething7
        self.lb8.mousePressEvent = self.doSomething8
        self.lb9.mousePressEvent = self.doSomething9
        self.lb10.mousePressEvent = self.doSomething10
        self.lb11.mousePressEvent = self.doSomething11
        self.lb12.mousePressEvent = self.doSomething12
        self.lb13.mousePressEvent = self.doSomething13
        self.lb14.mousePressEvent = self.doSomething14
        self.lb15.mousePressEvent = self.doSomething15
        self.pos = 0
        self.listLength = 15
        self.initMovieListByIndex()
        # print("event bind!")
        # self.labelList = [self.lb1, self.lb2, self.lb3, self.lb4, self.lb5, self.lb6, self.lb7, self.lb8, self.lb9,
        #                   self.lb10, self.lb11. self.lb12, self.lb13, self.lb14, self.lb15]
        # print("movieList")
        self.selectedMovie = ""
        # print("selectedMovie")
        # self.labelList = [QLabel("", self) for i in range(0, 15)]
        # self.initLabelEvent()
        self.loadImageFromFile()
        self.setWindowTitle("OTTRS Main")
        # self.initMovieImg()

    def loadImageFromFile(self):
        # QPixmap 객체 생성 후 이미지 파일을 이용하여 QPixmap에 사진 데이터 Load하고, Label을 이용하여 화면에 표시

        self.qPixmapFileVar = QPixmap()
        # print(self.movieList[0])
        self.qPixmapFileVar.load(self.imgDir + self.movieList[0].MOVIEIMGNAME)
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(170)
        self.lb1.setPixmap(self.qPixmapFileVar)
        # print(self.idx,"LIFF")
        # print(self.movieList[0].MOVIESEQ)

        self.qPixmapFileVar.load(self.imgDir + self.movieList[1].MOVIEIMGNAME)
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(170)
        self.lb2.setPixmap(self.qPixmapFileVar)

        self.qPixmapFileVar.load(self.imgDir + self.movieList[2].MOVIEIMGNAME)
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(170)
        self.lb3.setPixmap(self.qPixmapFileVar)

        self.qPixmapFileVar.load(self.imgDir + self.movieList[3].MOVIEIMGNAME)
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(170)
        self.lb4.setPixmap(self.qPixmapFileVar)

        self.qPixmapFileVar.load(self.imgDir + self.movieList[4].MOVIEIMGNAME)
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(170)
        self.lb5.setPixmap(self.qPixmapFileVar)

        self.qPixmapFileVar.load(self.imgDir + self.movieList[5].MOVIEIMGNAME)
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(170)
        self.lb6.setPixmap(self.qPixmapFileVar)

        self.qPixmapFileVar.load(self.imgDir + self.movieList[6].MOVIEIMGNAME)
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(170)
        self.lb7.setPixmap(self.qPixmapFileVar)

        self.qPixmapFileVar.load(self.imgDir + self.movieList[7].MOVIEIMGNAME)
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(170)
        self.lb8.setPixmap(self.qPixmapFileVar)

        self.qPixmapFileVar.load(self.imgDir + self.movieList[8].MOVIEIMGNAME)
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(170)
        self.lb9.setPixmap(self.qPixmapFileVar)

        self.qPixmapFileVar.load(self.imgDir + self.movieList[9].MOVIEIMGNAME)
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(170)
        self.lb10.setPixmap(self.qPixmapFileVar)

        self.qPixmapFileVar.load(self.imgDir + self.movieList[10].MOVIEIMGNAME)
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(170)
        self.lb11.setPixmap(self.qPixmapFileVar)

        self.qPixmapFileVar.load(self.imgDir + self.movieList[11].MOVIEIMGNAME)
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(170)
        self.lb12.setPixmap(self.qPixmapFileVar)

        self.qPixmapFileVar.load(self.imgDir + self.movieList[12].MOVIEIMGNAME)
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(170)
        self.lb13.setPixmap(self.qPixmapFileVar)

        self.qPixmapFileVar.load(self.imgDir + self.movieList[13].MOVIEIMGNAME)
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(170)
        self.lb14.setPixmap(self.qPixmapFileVar)

        self.qPixmapFileVar.load(self.imgDir + self.movieList[14].MOVIEIMGNAME)
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(170)
        self.lb15.setPixmap(self.qPixmapFileVar)

    def initMovieListByGenre(self):
        print("initMovieListByGenre")
        print(self.window.loginUserSeq)
        self.window.movieGenreList = getMovieGenreList(self.window.loginUserSeq)
        print(self.window.movieGenreList)

    def initMovieListByIndex(self):
        sIdx = self.pos
        eIdx = self.pos + self.listLength
        # print(sIdx, eIdx)
        movieGenreList = self.window.movieGenreList
        # print(movieGenreList)
        conn = getConn()
        cur = conn.cursor()
        movieSeqList = []

        for i in range(sIdx, eIdx):
            movieSeqList.append(movieGenreList[i])

        for movieSeq in movieSeqList:
            sql = "SELECT * FROM MOVIE WHERE MOVIESEQ ="
            sql += str(movieSeq)
            print(sql)
            cur.execute(sql)
            movie = [i for i in cur.fetchall()][0]
            print(movie)
            movieClass = Movie()

            movieClass.MOVIESEQ = movie[0]
            movieClass.MOVIETITLE = movie[1]
            movieClass.MOVIECODE = movie[2]
            movieClass.MOVIEPLOT = movie[3]
            movieClass.MOVIEMODE = movie[4]
            movieClass.MOVIEPRICE = movie[5]
            movieClass.MOVIEPOSTRIMG = movie[6]
            movieClass.MOVIEDIRECTOR = movie[7]
            movieClass.MOVIEGENRE = movie[8]
            movieClass.MOVIEIMGNAME = movie[9]

            self.movieList.append(movieClass)
        conn.close()

    def initMovieList(self):
        conn = getConn()
        cur = conn.cursor()
        sql = "SELECT * FROM MOVIE"
        cur.execute(sql)
        # print(cur)

        movieSelectList = [i for i in cur.fetchall()]
        movieLen = len(movieSelectList)
        # print(movieSelectList)
        # print(movieLen)
        randomIndexList = self.getLotto(movieLen)
        # print(randomIndexList)
        for index in randomIndexList:
            movie = movieSelectList[index]
            movieClass = Movie()

            movieClass.MOVIESEQ = movie[0]
            movieClass.MOVIETITLE = movie[1]
            movieClass.MOVIECODE = movie[2]
            movieClass.MOVIEPLOT = movie[3]
            movieClass.MOVIEMODE = movie[4]
            movieClass.MOVIEPRICE = movie[5]
            movieClass.MOVIEPOSTRIMG = movie[6]
            movieClass.MOVIEDIRECTOR = movie[7]
            movieClass.MOVIEGENRE = movie[8]
            movieClass.MOVIEIMGNAME = movie[9]

            self.movieList.append(movieClass)

        conn.close()

    # def initLabelEvent(self):
    #     for label in self.labelList:
    #         label.mousePressEvent = self.doSomething

    def initMovieImg(self):
        # print("initMovieImg")
        for idx in range(0, 15):
            # print(idx)
            self.qPixmapFileVar = QPixmap()
            # print(self.imgDir+self.movieList[idx].MOVIEIMGNAME)
            # print(self.labelList[idx])
            self.qPixmapFileVar.load(self.imgDir + self.movieList[idx].MOVIEIMGNAME)
            self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(170)
            self.labelList[idx].setPixmap(self.qPixmapFileVar)

    def getLotto(self, maxLength):
        # print(maxLength)
        lotto = set()
        while len(lotto) < 15:
            lotto.add(randint(0, maxLength - 1))
        lotto = list(lotto)
        return lotto

    def doSomething1(self, event):
        self.selectedMovie = self.movieList[0]
        self.nowWidget = movie_ver0825.Movie(self)
        self.setCentralWidget(self.nowWidget)
        self.resize(self.nowWidget.width, self.nowWidget.height)
        # self.setGeometry(50, 50, self.nowWidget.width, self.nowWidget.height)

    def doSomething2(self, event):
        self.selectedMovie = self.movieList[1]
        self.nowWidget = movie_ver0825.Movie(self)
        self.setCentralWidget(self.nowWidget)
        self.resize(self.nowWidget.width, self.nowWidget.height)
        # self.setGeometry(50, 50, self.nowWidget.width, self.nowWidget.height)

    def doSomething3(self, event):
        self.selectedMovie = self.movieList[2]
        self.nowWidget = movie_ver0825.Movie(self)
        self.setCentralWidget(self.nowWidget)
        self.resize(self.nowWidget.width, self.nowWidget.height)
        # self.setGeometry(50, 50, self.nowWidget.width, self.nowWidget.height)

    def doSomething4(self, event):
        self.selectedMovie = self.movieList[3]
        self.nowWidget = movie_ver0825.Movie(self)
        self.setCentralWidget(self.nowWidget)
        self.resize(self.nowWidget.width, self.nowWidget.height)
        # self.setGeometry(50, 50, self.nowWidget.width, self.nowWidget.height)

    def doSomething5(self, event):
        self.selectedMovie = self.movieList[4]
        self.nowWidget = movie_ver0825.Movie(self)
        self.setCentralWidget(self.nowWidget)
        self.resize(self.nowWidget.width, self.nowWidget.height)
        # self.setGeometry(50, 50, self.nowWidget.width, self.nowWidget.height)

    def doSomething6(self, event):
        self.selectedMovie = self.movieList[5]
        self.nowWidget = movie_ver0825.Movie(self)
        self.setCentralWidget(self.nowWidget)
        self.resize(self.nowWidget.width, self.nowWidget.height)
        # self.setGeometry(50, 50, self.nowWidget.width, self.nowWidget.height)

    def doSomething7(self, event):
        self.selectedMovie = self.movieList[6]
        self.nowWidget = movie_ver0825.Movie(self)
        self.setCentralWidget(self.nowWidget)
        self.resize(self.nowWidget.width, self.nowWidget.height)
        # self.setGeometry(50, 50, self.nowWidget.width, self.nowWidget.height)

    def doSomething8(self, event):
        self.selectedMovie = self.movieList[7]
        self.nowWidget = movie_ver0825.Movie(self)
        self.setCentralWidget(self.nowWidget)
        self.resize(self.nowWidget.width, self.nowWidget.height)
        # self.setGeometry(50, 50, self.nowWidget.width, self.nowWidget.height)

    def doSomething9(self, event):
        self.selectedMovie = self.movieList[8]
        self.nowWidget = movie_ver0825.Movie(self)
        self.setCentralWidget(self.nowWidget)
        self.resize(self.nowWidget.width, self.nowWidget.height)
        # self.setGeometry(50, 50, self.nowWidget.width, self.nowWidget.height)

    def doSomething10(self, event):
        self.selectedMovie = self.movieList[9]
        self.nowWidget = movie_ver0825.Movie(self)
        self.setCentralWidget(self.nowWidget)
        self.resize(self.nowWidget.width, self.nowWidget.height)
        # self.setGeometry(50, 50, self.nowWidget.width, self.nowWidget.height)

    def doSomething11(self, event):
        self.selectedMovie = self.movieList[10]
        self.nowWidget = movie_ver0825.Movie(self)
        self.setCentralWidget(self.nowWidget)
        self.resize(self.nowWidget.width, self.nowWidget.height)
        # self.setGeometry(50, 50, self.nowWidget.width, self.nowWidget.height)

    def doSomething12(self, event):
        self.selectedMovie = self.movieList[11]
        self.nowWidget = movie_ver0825.Movie(self)
        self.setCentralWidget(self.nowWidget)
        self.resize(self.nowWidget.width, self.nowWidget.height)
        # self.setGeometry(50, 50, self.nowWidget.width, self.nowWidget.height)

    def doSomething13(self, event):
        self.selectedMovie = self.movieList[12]
        self.nowWidget = movie_ver0825.Movie(self)
        self.setCentralWidget(self.nowWidget)
        self.resize(self.nowWidget.width, self.nowWidget.height)
        # self.setGeometry(50, 50, self.nowWidget.width, self.nowWidget.height)

    def doSomething14(self, event):
        self.selectedMovie = self.movieList[13]
        self.nowWidget = movie_ver0825.Movie(self)
        self.setCentralWidget(self.nowWidget)
        self.resize(self.nowWidget.width, self.nowWidget.height)
        # self.setGeometry(50, 50, self.nowWidget.width, self.nowWidget.height)

    def doSomething15(self, event):
        self.selectedMovie = self.movieList[14]
        self.nowWidget = movie_ver0825.Movie(self)
        self.setCentralWidget(self.nowWidget)
        self.resize(self.nowWidget.width, self.nowWidget.height)
        # self.setGeometry(50, 50, self.nowWidget.width, self.nowWidget.height)

    # def doSomething(self, event):
    #     # print("성공")
    #     self.nowWidget = movie_2.Movie(self)
    #     self.setCentralWidget(self.nowWidget)
    #     self.resize(self.nowWidget.width, self.nowWidget.height)
    #     # self.setGeometry(50, 50, self.nowWidget.width, self.nowWidget.height)

    def PageUp(self):
        if self.idx >= 134:
            self.idx = 134
        else:
            self.idx += 15
            self.loadImageFromFile()

    def PageDown(self):
        if self.idx == 1:
            self.idx = 1
        else:
            self.idx -= 15
            self.loadImageFromFile()

    def button1Function(self):
        return self.PageUp()

    def button2Function(self):
        return self.PageUp()
        # print("btn2 Clicked")

    def button3Function(self):
        return self.PageUp()
        # print("btn3 Clicked")

    # --------------버튼 실행
    def searchMovie(self):
        connection = cx_Oracle.connect(
            "scott", "tigertiger", "orcl.cgnlgvycsnjd.us-east-2.rds.amazonaws.com:1521/orcl")
        cur = connection.cursor()
        movietitle = self.lineEdit.text()
        sql = """SELECT * FROM MOVIE WHERE MOVIETITLE ='%s'""" % movietitle
        # print(sql)
        cur.execute(sql)
        result = 0
        self.movieimgno = 0
        for value in cur:
            result = value[0]
            self.movieimgno = value[-1]
            print(value)

        # print(result)
        if result:
            print("영화존재. 존재하는 영화 세부페이지로 가기")
            newwindow = AfSearchMovieClass(self)

        else:
            QMessageBox.question(self, '오류', '찾는 영화가 존재하지 않습니다.', QMessageBox.Ok)

    # -----------------------
    def initMainWidget(self):
        # print("main -- initMainWidget ")
        # self.nowWidget = MainWidget(self)
        # self.setCentralWidget(self.nowWidget)
        # self.resize(self.nowWidget.width, self.nowWidget.height)
        # self.setGeometry(50, 50, self.nowWidget.width, self.nowWidget.height)

        self.mainWindow = WindowClass(self.window)
        self.hide()
        self.mainWindow.show()


if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()