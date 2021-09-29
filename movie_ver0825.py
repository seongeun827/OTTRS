import sys
import cx_Oracle
import csv
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineSettings
from PyQt5.QtCore import QUrl
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtWidgets



# self.webview.setUrl(QUrl("https://www.youtube.com/embed/HxM1aZ6l3M0?autoplay=0"))


class Movie(QWidget):
    def __init__(self, parent):
        QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        super().__init__(parent)
        self.webview1 = QtWebEngineWidgets.QWebEngineView()
        self.webview2 = QtWebEngineWidgets.QWebEngineView()
        self.webview3 = QtWebEngineWidgets.QWebEngineView()
        self.webview4 = QtWebEngineWidgets.QWebEngineView()

        self.webViewList = [self.webview1, self.webview2, self.webview3, self.webview4]

        self.img4 = ""
        self.img3 = ""
        self.img2 = ""
        self.img1 = ""
        self.imgList = [self.img1, self.img2, self.img3, self.img4]
        self.pp = parent

        # self.hbackground = QLabel("hback", self)
        # self.background = QPixmap("./hhbackgroundreal.png")
        # self.background = self.background.scaled(1100, 730, Qt.KeepAspectRatio, Qt.FastTransformation)
        # self.hbackground.setPixmap(self.background)

        # self.movieClass =self.pp.selectedMovie
        # print(self.movieClass.MOVIESEQ)
        self.width = 1300
        self.height = 850
        # self.setStyleSheet("background-color: #FEE8DB;")
        self.setStyleSheet("background-color: #F6F6EB;")
        # self.pp.setWindowTitle("OTTRS Movie Info")

        self.imgDir = "./img/movie/"

        #배경넣기
        # self.back= QLabel("back",self)
        # self.blue= QPixmap("E:\pythonStudy\ottrsProject\img\hblue.png")
        # self.blue=self.blue.scaled(1300,850,Qt.KeepAspectRatio, Qt.FastTransformation)
        # self.back.setPixmap(self.blue)

        # "메인으로" 버튼
        self.gotoMainBtn = QPushButton("메인으로", self)
        self.gotoMainBtn.clicked.connect(self.gotoMain)
        # 포스터-img
        self.number = 1  # number=영화번호
        self.movie1 = QPixmap(self.pp.imgDir+self.pp.selectedMovie.MOVIEIMGNAME)  # 포스터그림
        self.movie1 = self.movie1.scaled(190, 273, Qt.KeepAspectRatio, Qt.FastTransformation)  # 포스터 크기조정

        # 포스터 라벨
        self.lePoster = QLabel("포스터칸_라벨", self)
        self.lePoster.setPixmap(self.movie1)

        # 영화정보안내: 라벨들 정의
        self._leTitle = QLabel("제목: ", self)
        self._leTitle.setAlignment(Qt.AlignCenter)  # 가운데정렬(가로세로 모두)
        # 행만 가운데(Qt.AlignHCenter) 열만 가운데(Qt.AlignVCenter) 동시(Qt.AlignRight|Qt.AlignBottom)

        self._leGenre = QLabel("장르: ", self)
        self._leGenre.setAlignment(Qt.AlignCenter)

        self._leDirector = QLabel("감독: ", self)
        self._leDirector.setAlignment(Qt.AlignCenter)

        # self._leCast = QLabel("배우: ", self)
        # self._leCast.setAlignment(Qt.AlignCenter)

        # self._leGrade = QLabel("등급: ", self)
        # self._leGrade.setAlignment(Qt.AlignCenter)

        # 영화정보 라벨들
        self.leTitle = QLabel(self.pp.selectedMovie.MOVIETITLE, self)  # 실제 영화제목 들어가는 라벨
        self.leTitle.setAlignment(Qt.AlignVCenter)  # 행을 가운데정렬

        self.leGenre = QLabel(self.pp.selectedMovie.MOVIEGENRE, self)
        self.leGenre.setAlignment(Qt.AlignVCenter)

        self.leDirector = QLabel(self.pp.selectedMovie.MOVIEDIRECTOR, self)
        self.leDirector.setAlignment(Qt.AlignVCenter)

        # self.leCast = QLabel("배우_라벨", self)
        # self.leCast.setAlignment(Qt.AlignVCenter)

        self.lePlot = QLabel(self.pp.selectedMovie.MOVIEPLOT, self)
        self.lePlot.setAlignment(Qt.AlignVCenter)

        # self.leGrade = QLabel("등급_라벨", self)
        # self.leGrade.setAlignment(Qt.AlignVCenter)

        # 텍스터리뷰 라벨
        self.leTextReview = QLabel("텍스트리뷰내용_라벨", self)
        # self.leTextReview.setAlignment(Qt.AlignVCenter) #정렬



        # 유튜브리뷰 라벨
        # self.leYtReview1 = QLabel("유튜브리뷰1내용_라벨", self)
        # self.leYtReview2 = QLabel("유튜브리뷰2내용_라벨", self)
        # self.leYtReview3 = QLabel("유튜브리뷰3내용_라벨", self)
        # self.leYtReview4 = QLabel("유튜브리뷰4내용_라벨", self)
        #
        # self.leYtReviewList = [self.leYtReview1, self.leYtReview2, self.leYtReview3, self.leYtReview4]
        # self.leYtReview.setAlignment(Qt.AlignVCenter) #정렬

        # 가격비교 라벨
        # self._leGoogle= QLabel("구글",self)
        # self.leGoogle= QLabel("구글가격칸_라벨",self)
        self._leNaver = QLabel("<네이버>  ", self)
        self.leNaver = QLabel(self.pp.selectedMovie.MOVIEMODE+self.pp.selectedMovie.MOVIEPRICE, self)
        print("------------------init---------------")
        self.initUI()

    # 전체 UI를 그리드로/ 각각의 영역을 함수로/ 이후 행-열 숫자 바꾸면 위치 변경 가능
    def initUI(self):
        # self.back.move(0,0)
        # self.setStyleSheet("background-color: #F6F6EB;")
        grid = QGridLayout()
        grid.addWidget(self.gotoMainBtn, 0, 0, 1, 2)
        grid.addWidget(self.poster(), 1, 0, 2, 3)
        grid.addWidget(self.movieinfo(), 1, 3, 2, 3)
        grid.addWidget(self.plot(), 3, 0, 2, 6)
        grid.addWidget(self.price(), 1, 6, 1, 6)
        grid.addWidget(self.textReview(), 2, 6, 1, 6)

        self.setGeometry(50, 50, self.width, self.height)  # 메인 창의 위치와 크기
        self.pp.setWindowTitle("OTTRS Movie") # 창 타이틀 이름

        self.show()
        print("--------before conn--------")
        conn = cx_Oracle.connect("scott", "tigertiger", "orcl.cgnlgvycsnjd.us-east-2.rds.amazonaws.com:1521/orcl")
        cur = conn.cursor()
        movieSeq = self.pp.selectedMovie.MOVIESEQ
        print("movieSeq :", movieSeq)
        sql = "SELECT TEXTREVIEWVALUE FROM TEXT_REVIEW WHERE MOVIESEQ ="+str(movieSeq)
        print(sql)
        cur.execute(sql)
        rvList = [i for i in cur.fetchall()]
        reviewList = [r[0] for r in rvList]
        print(reviewList)

        rvText = ""
        for rv in reviewList:
            rvText += " ▷ " + rv + "\n" + "\n"

        self.leTextReview.setText(rvText)


        self.leTextReview.setWordWrap(True)

        sql = "SELECT THUMBIMG, URL FROM YOUTUBE_REVIEW WHERE MOVIESEQ =" + str(movieSeq)
        # print(sql)
        cur.execute(sql)
        youList = [i for i in cur.fetchall()]
        # print(youList)
        # youtubeThumbImgList = [r[0] for r in youList]
        youtubeUrlList = [r[1] for r in youList]

        # print(self.leYtReviewList[0])
        # print(youtubeThumbImgList)

        # for i, rv in reviewList:
        #     pass
        print(youtubeUrlList)
        grid.addWidget(self.youtubeReview(youtubeUrlList), 3, 6, 2, 6)

        conn.close()

        self.gotoMainBtn.setStyleSheet("color: black;"

                    "font-family: 'GMARKETSANSMEDIUM';"
                    "font-size: 20px;"
                    "color: white;"
                    "background-color: #9aafda;"
             )
        self.groupboxPoster.setStyleSheet("color: black;"
        "font-family: 'NEXON LV1 GOTHIC OTF';"
        "font-weight:bold;"
                    "font-size: 23px;"
                    )

        self.groupboxMovieinfo.setStyleSheet("color: black;"
        "font-family: 'NEXON LV1 GOTHIC OTF';"
        "font-weight:bold;"
                    "font-size: 23px;")

        self.groupboxPrice.setStyleSheet("color: black;"
        "font-family: 'NEXON LV1 GOTHIC OTF';"
        "font-weight:bold;"
                    "font-size: 23px;")

        self.groupboxTextReview.setStyleSheet("color: black;"
        "font-family: 'NEXON LV1 GOTHIC OTF';"
        "font-weight:bold;"
                    "font-size: 23px;")

        self.groupboxPlot.setStyleSheet("color: black;"
        "font-family: 'NEXON LV1 GOTHIC OTF';"
        "font-weight:bold;"
                    "font-size: 23px;")

        self.groupboxYoutubeReview.setStyleSheet("color: black;"
        "font-family: 'NEXON LV1 GOTHIC OTF';"
        "font-weight:bold;"
                    "font-size: 23px;")

        #1영화정보_글꼴
        self._leTitle.setStyleSheet("color: black;"
                    "font-family: 'NEXON LV1 GOTHIC OTF';"
                    "font-weight:500;"
                    "font-size: 20px;")

        self.leTitle.setStyleSheet("color: black;"
                    "font-family: 'NEXON LV1 GOTHIC OTF';"
                    "font-weight:600;"
                    "font-size: 20px;")

        self._leGenre.setStyleSheet("color: black;"
                    "font-family: 'NEXON LV1 GOTHIC OTF';"
                    "font-weight:500;"
                    "font-size: 20px;")

        self.leGenre.setStyleSheet("color: black;"
                    "font-family: 'NEXON LV1 GOTHIC OTF';"
                    "font-weight:600;"
                    "font-size: 20px;")

        self._leDirector.setStyleSheet("color: black;"
                    "font-family: 'NEXON LV1 GOTHIC OTF';"
                    "font-weight:500;"
                    "font-size: 20px;")

        self.leDirector.setStyleSheet("color: black;"
                    "font-family: 'NEXON LV1 GOTHIC OTF';"
                    "font-weight:600;"
                    "font-size: 20px;")

        # self._leCast.setStyleSheet("color: black;"
        #             "font-family: 'NEXON LV1 GOTHIC OTF';"
        #             "font-weight:500;"
        #             "font-size: 20px;")

        # self.leCast.setStyleSheet("color: black;"
        #             "font-family: 'NEXON LV1 GOTHIC OTF';"
        #             "font-weight:600;"
        #             "font-size: 20px;")

        #줄거리_글꼴
        self.lePlot.setStyleSheet("color: black;"
                    "font-family: 'Yoon Minguk';"
                    "font-weight:600;"
                    "font-size: 20px;")

        #텍스트리뷰_글꼴
        self.leTextReview.setStyleSheet("color: black;"
                    "font-family: 'Yoon Minguk';"
                    "font-weight:600;"
                    "font-size: 20px;")

        #가격_글꼴
        self._leNaver.setStyleSheet("color: black;"
                    "font-family: 'NEXON LV1 GOTHIC OTF';"
                    "font-weight:500;"
                    "font-size: 23px;")

        self.leNaver.setStyleSheet("color: black;"
            "font-family: 'NEXON LV1 GOTHIC OTF';"
            "font-weight:500;"
            "font-size: 23px;")

        
        #크기지정

        #포스터 박스
        self.groupboxPoster.setMinimumWidth(285)
        self.groupboxPoster.setMaximumWidth(285)
        self.groupboxPoster.setMinimumHeight(400)
        self.groupboxPoster.setMaximumHeight(400)

        #영화정보 박스
        self.groupboxMovieinfo.setMinimumWidth(285)
        self.groupboxMovieinfo.setMaximumWidth(285)
        self.groupboxMovieinfo.setMinimumHeight(400)
        self.groupboxMovieinfo.setMaximumHeight(400)

        #네이버가격 박스
        self.groupboxPrice.setMinimumWidth(610)
        self.groupboxPrice.setMaximumWidth(610)
        self.groupboxPrice.setMinimumHeight(200)
        self.groupboxPrice.setMaximumHeight(200)

        #텍스트리뷰 박스
        self.groupboxTextReview.setMinimumWidth(610)
        self.groupboxTextReview.setMaximumWidth(610)
        self.groupboxTextReview.setMinimumHeight(200)
        self.groupboxTextReview.setMaximumHeight(200)

        #줄거리 박스
        self.groupboxPlot.setMinimumWidth(590)
        self.groupboxPlot.setMaximumWidth(590)
        self.groupboxPlot.setMinimumHeight(400)
        self.groupboxPlot.setMaximumHeight(400)


        #유튜브 박스
        self.groupboxYoutubeReview.setMinimumWidth(600)
        self.groupboxYoutubeReview.setMaximumWidth(600)
        self.groupboxYoutubeReview.setMinimumHeight(400)      
        self.groupboxYoutubeReview.setMaximumHeight(400)










        



# "font-family: 'Yoon Minguk';"
        self.setLayout(grid)

        # for i, yti in enumerate(youtubeThumbImgList):
        #     # print(self.imgList[i])
        #     # print(self.leYtReviewList[i])
        #     img = QPixmap(self.imgDir + yti)
        #     img = img.scaled(190, 273, Qt.KeepAspectRatio, Qt.FastTransformation)
        #     self.leYtReviewList[i] = self.leYtReviewList[i].setPixmap(img)

    def gotoMain(self):
        self.pp.initMainWidget()

    # 포스터
    def poster(self):
        self.groupboxPoster = QGroupBox("- 포스터 -")

        # 포스터 라벨 넣기
        vbox = QVBoxLayout()
        vbox.addWidget(self.lePoster)
        self.lePoster.setAlignment(Qt.AlignCenter)
        self.groupboxPoster.setLayout(vbox)
        return self.groupboxPoster

    # 영화정보
    def movieinfo(self):
        self.groupboxMovieinfo = QGroupBox("- 영화정보 -")

        # 내부에 "제목:"과 "실제 제목 부분"을 각각을 가로 박스로.
        hboxTitle = QHBoxLayout()
        hboxTitle.addWidget(self._leTitle, 1)  # 영화정보안내- "영화제목:" 부분
        hboxTitle.addWidget(self.leTitle, 2)  # 뒤에 1과 2는 영역 길이비가 1:2

        hboxGenre = QHBoxLayout()
        hboxGenre.addWidget(self._leGenre, 1)  # "장르:" 부분
        hboxGenre.addWidget(self.leGenre, 2)

        hboxDirector = QHBoxLayout()
        hboxDirector.addWidget(self._leDirector, 1)  # "감독:" 부분
        hboxDirector.addWidget(self.leDirector, 2)

        # hboxCast = QHBoxLayout()
        # hboxCast.addWidget(self._leCast, 1)  # "배우:" 부분
        # hboxCast.addWidget(self.leCast, 2)

        # hboxGrade = QHBoxLayout()
        # hboxGrade.addWidget(self._leGrade, 1)  # "등급:" 부분
        # hboxGrade.addWidget(self.leGrade, 2)

        # 각 영역이 5개의 세로박스.
        vbox = QVBoxLayout()
        vbox.addLayout(hboxTitle)
        vbox.addLayout(hboxGenre)
        vbox.addLayout(hboxDirector)
        # vbox.addLayout(hboxCast)
        # vbox.addLayout(hboxGrade)

        self.groupboxMovieinfo.setLayout(vbox)
        return self.groupboxMovieinfo

    def plot(self):
        self.groupboxPlot = QGroupBox("- 줄거리 -")
        
        # 줄거리 라벨 넣기
        vbox = QVBoxLayout()
        scrollArea1= QScrollArea()
        scrollArea1.setWidgetResizable(True)
        # scrollArea1.setFixedHeight(390)
        scrollArea1.setFixedWidth(580)
        vbox.addWidget(scrollArea1)
        scrollArea1.setWidget(self.lePlot)
        self.groupboxPlot.setLayout(vbox)
        return self.groupboxPlot

    # 가격
    def price(self):
        self.groupboxPrice = QGroupBox("- 가격 -")

        # vboxGoogle= QVBoxLayout()
        # vboxGoogle.addWidget(self._leGoogle)
        # vboxGoogle.addWidget(self.leGoogle)

        # 가격 라벨 넣기
        vboxNaver = QVBoxLayout()
        vboxNaver.addWidget(self._leNaver)  # 영화정보안내- "영화제목:" 부분
        vboxNaver.addWidget(self.leNaver)

        hbox = QHBoxLayout()
        # hbox.addLayout(vboxGoogle)
        hbox.addLayout(vboxNaver)

        # vbox= QVBoxLayout()
        # vbox.addWidget(self.lePrice)
        self.groupboxPrice.setLayout(hbox)
        return self.groupboxPrice

    # 텍스트리뷰
    def textReview(self):
        self.groupboxTextReview = QGroupBox("- 텍스트리뷰 -")

        # 텍스트리뷰 라벨 넣기
        vbox = QVBoxLayout()
        scrollArea2= QScrollArea()
        scrollArea2.setWidgetResizable(True)
        # scrollArea1.setFixedHeight(190)
        scrollArea2.setFixedWidth(600)
        vbox.addWidget(scrollArea2)
        scrollArea2.setWidget(self.leTextReview)
        self.groupboxTextReview.setLayout(vbox)
        return self.groupboxTextReview

    # 유튜브리뷰
    def youtubeReview(self, youtubeUrlList):
        self.groupboxYoutubeReview = QGroupBox("- 유튜브리뷰 -")

        # self.webview1 = QtWebEngineWidgets.QWebEngineView()
        # self.webview2 = QtWebEngineWidgets.QWebEngineView()
        # self.webview3 = QtWebEngineWidgets.QWebEngineView()
        # self.webview4 = QtWebEngineWidgets.QWebEngineView()
        # self.webview.setUrl(QUrl("https://www.youtube.com/embed/HxM1aZ6l3M0?autoplay=0"))

        for i, url in enumerate(youtubeUrlList):
            self.webViewList[i].setUrl(QUrl(url))


        # 유튜브리뷰 라벨 넣기 (그리드로)
        grid = QGridLayout()
        grid.addWidget(self.webview1, 0, 0)
        # self.leYtReview1.setFrameShape(QFrame.StyledPanel)
        # 테투리지정 (QFrame.Box) (QFrame.Panel) 진하게_(QFrame.WinPanel) 연하게_(QFrame.StyledPanel)

        grid.addWidget(self.webview2, 0, 1)
        # self.leYtReview2.setFrameShape(QFrame.StyledPanel)

        grid.addWidget(self.webview3, 1, 0)
        # self.leYtReview3.setFrameShape(QFrame.StyledPanel)

        grid.addWidget(self.webview4, 1, 1)
        # self.leYtReview4.setFrameShape(QFrame.StyledPanel)

        self.groupboxYoutubeReview.setLayout(grid)
        return self.groupboxYoutubeReview


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Movie()
    sys.exit(app.exec_())
