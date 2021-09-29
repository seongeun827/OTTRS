import sys
import cx_Oracle
import csv
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class OttApp(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.pp = parent
        self.width = 1200
        self.height = 800
        self.setStyleSheet("background-color: white;")
        # self.pp.setWindowTitle("OTTRS Survey")


        self.question = QLabel("선호하는 컨텐츠를 선택하세요! 영화를 추천해드리는 데 도움이 됩니다. (3/3)", self)
        #지금은 장르 기준이지만 survey1 설문 바탕으로 알고리즘에 따라 포스터 들어가는 자리
        #이전 버전이 장르 기준이어서 이렇게 쓰여있음. 변경 가능
        self.answer1 = QLabel("코미디", self)  #지금은 장르 기준이지만 survey1 설문 바탕으로 알고리즘에 따라 포스터 들어가는 자리
        self.answer1.setAlignment(Qt.AlignVCenter|Qt.AlignRight) #가운데 정렬
        self.answer2 = QLabel("멜로", self)
        self.answer2.setAlignment(Qt.AlignVCenter|Qt.AlignRight)
        self.answer3 = QLabel("SF/판타지", self)
        self.answer3.setAlignment(Qt.AlignVCenter|Qt.AlignRight)
        self.answer4 = QLabel("다큐멘터리", self)
        self.answer4.setAlignment(Qt.AlignVCenter|Qt.AlignRight)
        self.answer5 = QLabel("공연실황", self)
        self.answer5.setAlignment(Qt.AlignVCenter|Qt.AlignRight)

        self.gotoResultBtn = QPushButton("완료! OTTRS 시작하고""\n""\n""메인화면에서 영화 추천 받기",self)
        self.gotoResultBtn.clicked.connect(self.gotoResult)
        #다음으로 버튼을 누르면 self.gotoResult() 함수로 연결됨

        

        self.img1 = QPixmap("E:\dev\python_workspace\img\survey2_poster\img1.jpg")
        self.img2 = QPixmap("E:\dev\python_workspace\img\survey2_poster\img2.jpg")
        self.img3 = QPixmap("E:\dev\python_workspace\img\survey2_poster\img3.jpg")
        self.img4 = QPixmap("E:\dev\python_workspace\img\survey2_poster\img4.jpg")
        self.img5 = QPixmap("E:\dev\python_workspace\img\survey2_poster\img5.jpg")

        self.img1=self.img1.scaled(190,273,Qt.KeepAspectRatio, Qt.FastTransformation) #포스터 크기조정
        self.img2=self.img2.scaled(190,273,Qt.KeepAspectRatio, Qt.FastTransformation) 
        self.img3=self.img3.scaled(190,273,Qt.KeepAspectRatio, Qt.FastTransformation) 
        self.img4=self.img4.scaled(190,273,Qt.KeepAspectRatio, Qt.FastTransformation) 
        self.img5=self.img5.scaled(190,273,Qt.KeepAspectRatio, Qt.FastTransformation) 


        self.button1 = QRadioButton("트루먼쇼",self)
        self.button1.clicked.connect(self.mvbtnClicked)   #버튼이 눌리면 self.mvbtnClicked 함수로 연결됨.
        self.button2 = QRadioButton("윤희에게",self)
        self.button2.clicked.connect(self.mvbtnClicked)
        self.button3 = QRadioButton("신과 함께",self)
        self.button3.clicked.connect(self.mvbtnClicked)
        self.button4 = QRadioButton("말하는""\n""건축가",self)
        self.button4.clicked.connect(self.mvbtnClicked)
        self.button5 = QRadioButton("레미제라블""\n""뮤지컬""\n""콘서트",self)
        self.button5.clicked.connect(self.mvbtnClicked)



        self.initUI()



    def initUI(self):

        self.answer1.setPixmap(self.img1)
        self.answer2.setPixmap(self.img2)
        self.answer3.setPixmap(self.img3)
        self.answer4.setPixmap(self.img4)
        self.answer5.setPixmap(self.img5)

        grid=QGridLayout()

        grid.addWidget(self.boxQ(),0,0,1,3)
        grid.addWidget(self.box1(),1,0,3,1)
        grid.addWidget(self.box2(),1,1,3,1)
        grid.addWidget(self.box3(),1,2,3,1)
        grid.addWidget(self.box4(),4,0,3,1)
        grid.addWidget(self.box5(),4,1,3,1)
        grid.addWidget(self.gotoResultBtn,5,2)


 
        self.setLayout(grid)

        self.gotoResultBtn.setEnabled(False)  #추천받기 버튼 비활성화 상태가 기본값
        # self.gotoResultBtn.setStyleSheet("background-color:rgb(169,169,169)") #비활성화 버튼 상태 회색

        # self.setWindowTitle("영화 취향 선택!")
        # self.setGeometry(50,50,1100,730) #메인 창의 위치와 크기
        self.setWindowTitle("OTTRS Survey") #창 타이틀 이름


        self.question.setStyleSheet(
            "color: black;"
            "font-family: 'GMARKETSANSMEDIUM';"
            "font-size: 25px;")

        self.button1.setStyleSheet("color: black;"

                    "font-family: 'NEXON LV1 GOTHIC OTF';"
                    "font-weight:bold;"
                    "font-size: 23px;")

        self.button2.setStyleSheet("color: black;"

                    "font-family: 'NEXON LV1 GOTHIC OTF';"
                    "font-weight:bold;"
                    "font-size: 23px;")
        self.button3.setStyleSheet("color: black;"

                    "font-family: 'NEXON LV1 GOTHIC OTF';"
                    "font-weight:bold;"
                    "font-size: 23px;")

        self.button4.setStyleSheet("color: black;"

                    "font-family: 'NEXON LV1 GOTHIC OTF';"
                    "font-weight:bold;"
                    "font-size: 23px;")

        self.button5.setStyleSheet("color: black;"

                    "font-family: 'NEXON LV1 GOTHIC OTF';"
                    "font-weight:bold;"
                    "font-size: 23px;")

        self.gotoResultBtn.setStyleSheet("color: black;"

                    "font-family: 'GMARKETSANSMEDIUM';"
                    "font-weight:bold;"
                    "font-size: 20px;"
                    "background-color: #6E727D;"
                    
             )

        self.groupboxQ.setStyleSheet("background-color:#ECC165;")

        self.show()







    def boxQ(self):
        self.groupboxQ= QGroupBox()

        #포스터 라벨 넣기
        vbox = QVBoxLayout()
        vbox.addWidget(self.question)
        self.groupboxQ.setLayout(vbox)
        return self.groupboxQ

    def box1(self):
        groupbox= QGroupBox()
        hbox= QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.answer1)
        groupbox.setLayout(hbox)
        return groupbox

    def box2(self):
        groupbox= QGroupBox()
        hbox= QHBoxLayout()
        hbox.addWidget(self.button2)
        hbox.addWidget(self.answer2)
        groupbox.setLayout(hbox)
        return groupbox

    def box3(self):
        groupbox= QGroupBox()
        hbox= QHBoxLayout()
        hbox.addWidget(self.button3)
        hbox.addWidget(self.answer3)
        groupbox.setLayout(hbox)
        return groupbox

    def box4(self):
        groupbox= QGroupBox()
        hbox= QHBoxLayout()
        hbox.addWidget(self.button4)
        hbox.addWidget(self.answer4)
        groupbox.setLayout(hbox)
        return groupbox

    def box5(self):
        groupbox= QGroupBox()
        hbox= QHBoxLayout()
        hbox.addWidget(self.button5)
        hbox.addWidget(self.answer5)
        groupbox.setLayout(hbox)
        return groupbox

    def mvbtnClicked(self):  
        if self.button1.isChecked() or self.button2.isChecked() or self.button3.isChecked() or self.button4.isChecked() or self.button5.isChecked():
            #button1~button5 중에 하나가 눌리면(or로 연결) 
            #추천받기 버튼 활성화!
            self.gotoResultBtn.setEnabled(True)  
            self.gotoResultBtn.setStyleSheet("color: black;"

            "font-family: 'GMARKETSANSMEDIUM';"
            "font-weight:bold;"
            "font-size: 20px;"
            "background-color: #9aafda;")

    def gotoResult(self):
        print("다음으로 버튼이 눌림")
        survey3 = ""
        if self.button1.isChecked():
            print("영화1 선택됨")
            survey3 = 1
        elif self.button2.isChecked():
            print("영화2 선택됨")
            survey3 = 3
        elif self.button3.isChecked():
            print("영화3 선택됨")
            survey3 = 5
        elif self.button4.isChecked():
            print("영화4 선택됨")
            survey3 = 7
        elif self.button5.isChecked():
            print("영화5 선택됨")
            survey3 = 9
        print(self.pp.serGenreList)
        print(self.pp.survey2Genre)
        print(survey3)

        genreList = self.pp.serGenreList
        survey2 = self.pp.survey2Genre

        genreList[survey2] += 2
        genreList[survey3] += 2

        print(genreList)
        # 액션, 코미디, 드라마, 멜로, 공포 / 스릴러, SF / 판타지, 애니메이션, 다큐멘터리
        sql = """ INSERT INTO USER_GENRE VALUES (OTTRS_USER_SEQ.NEXTVAL,"""
        sql += str(genreList[0]) + ","
        sql += str(genreList[1]) + ","
        sql += str(genreList[2]) + ","
        sql += str(genreList[3]) + ","
        sql += str(genreList[4]) + ","
        sql += str(genreList[5]) + ","
        sql += str(genreList[6]) + ","
        sql += str(genreList[7]) + ","
        sql += str(self.pp.loginUserSeq)
        sql += ")"

        print(sql)

        conn = cx_Oracle.connect("scott", "tigertiger", "orcl.cgnlgvycsnjd.us-east-2.rds.amazonaws.com:1521/orcl")
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        conn.close()

        self.pp.initMainWidget()




if __name__ == "__main__":
    a = QApplication(sys.argv)
    e = OttApp()
    sys.exit(a.exec_())