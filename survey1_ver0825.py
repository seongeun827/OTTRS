import sys
from PyQt5.QtWidgets import *


class Survey(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.pp = parent

        self.width = 1200
        self.height = 800
        self.setStyleSheet("background-color: white;")
        self.pp.setWindowTitle("OTTRS Survey")

        # self.hbackground = QLabel("hback", self) 
        # self.hbackground.setGeometry(0,0,1100,730)
        # self.background= QPixmap("E:\pythonStudy\ottrsProject\survey01back.jpg")
        # self.background=self.background.scaled(1100,730,Qt.KeepAspectRatio, Qt.FastTransformation)
        # self.hbackground.setPixmap(self.background)

        #장르선호 변수를 기본으로 0으로.
        #추후에 "좋아함" 라디오버튼이 눌리면 해당 장르값이 1이 됨.
        #하지만 리스트로 담기는 거라서 self.userGenreList[0] 리스트 인덱스 값으로 접근해야함. (genre1 값으로는 계속 0만 나옴)
        #그리고 리스트 기준 0번째가 genre1 액선이 됨.
        self.genre1=0  #액션
        self.genre2=0  #코미디
        self.genre3=0  #드라마
        self.genre4=0  #멜로
        self.genre5=0  #공포/스릴러
        self.genre6=0  #SF/스릴러
        self.genre7=0  #애니메이션
        self.genre8=0  #디큐멘터리
        self.genre9=0  #독립영화
        self.genre10=0  #공연실황

        #리스트로.
        self.userGenreList= [self.genre1, self.genre2, self.genre3, self.genre4, self.genre5, self.genre6, self.genre7, self.genre8, self.genre9, self.genre10]


        #라벨 정의
        self.question = QLabel('선호하는 장르를 알려주세요. 영화를 추천해드리는 데 도움이 됩니다. (1/3)''\n''\n''모두 선택하신 후에 "선택완료!" 버튼을 클릭해주세요!', self)

 
        self.leGenre1 = QLabel("액션",self)

        self.leGenre2 = QLabel("코미디",self)

        self.leGenre3 = QLabel("드라마",self)

        self.leGenre4 = QLabel("멜로",self)

        self.leGenre5 = QLabel("공포/스릴러",self)

        self.leGenre6 = QLabel("SF/판타지",self)

        self.leGenre7 = QLabel("애니메이션",self)

        self.leGenre8 = QLabel("다큐멘터리",self)
        
        self.leGenre9 = QLabel("독립영화",self)

        self.leGenre10 = QLabel("공연실황",self)
    

        #좋아함, 좋아하지 않음 라디오 버튼 각각
        self.g1button1 = QRadioButton("좋아함",self)
        self.g1button1.clicked.connect(self.btnClicked)
        self.g1button0 = QRadioButton("좋아하지않음",self)
        self.g1button0.clicked.connect(self.btnClicked)

        self.g2button1 = QRadioButton("좋아함",self)
        self.g2button1.clicked.connect(self.btnClicked)
        self.g2button0 = QRadioButton("좋아하지않음",self)
        self.g2button0.clicked.connect(self.btnClicked)
        
        self.g3button1 = QRadioButton("좋아함",self)
        self.g3button1.clicked.connect(self.btnClicked)
        self.g3button0 = QRadioButton("좋아하지않음",self)
        self.g3button0.clicked.connect(self.btnClicked)

        self.g4button1 = QRadioButton("좋아함",self)
        self.g4button1.clicked.connect(self.btnClicked)
        self.g4button0 = QRadioButton("좋아하지않음",self)
        self.g4button0.clicked.connect(self.btnClicked)

        self.g5button1 = QRadioButton("좋아함",self)
        self.g5button1.clicked.connect(self.btnClicked)
        self.g5button0 = QRadioButton("좋아하지않음",self)
        self.g5button0.clicked.connect(self.btnClicked)

        self.g6button1 = QRadioButton("좋아함",self)
        self.g6button1.clicked.connect(self.btnClicked)
        self.g6button0 = QRadioButton("좋아하지않음",self)
        self.g6button0.clicked.connect(self.btnClicked)

        self.g7button1 = QRadioButton("좋아함",self)
        self.g7button1.clicked.connect(self.btnClicked)
        self.g7button0 = QRadioButton("좋아하지않음",self)
        self.g7button0.clicked.connect(self.btnClicked)

        self.g8button1 = QRadioButton("좋아함",self)
        self.g8button1.clicked.connect(self.btnClicked)
        self.g8button0 = QRadioButton("좋아하지않음",self)
        self.g8button0.clicked.connect(self.btnClicked)

        self.g9button1 = QRadioButton("좋아함",self)
        self.g9button1.clicked.connect(self.btnClicked)
        self.g9button0 = QRadioButton("좋아하지않음",self)
        self.g9button0.clicked.connect(self.btnClicked)

        self.g10button1 = QRadioButton("좋아함",self)
        self.g10button1.clicked.connect(self.btnClicked)
        self.g10button0 = QRadioButton("좋아하지않음",self)
        self.g10button0.clicked.connect(self.btnClicked)

        #완료 버튼 
        self.doneBtn = QPushButton("\n""선택완료!""\n",self) 
        self.doneBtn.clicked.connect(self.doneClicked)   #self.doneClicked 함수로

        #다음으로 버튼
        self.gotoNextBtn = QPushButton("\n""⟶ 다음""\n",self)
        self.gotoNextBtn.clicked.connect(self.gotoNext) #self.gotoNext 함수로


        
        self.initUI()

    def initUI(self):

        #각각의 영역을 함수로 정의후 그리드에 담음
        grid=QGridLayout()
        grid.addWidget(self.boxQ(),0,0,1,2)
        grid.addWidget(self.genre1_Action(),1,0)
        grid.addWidget(self.genre2_Comedy(),2,0)
        grid.addWidget(self.genre3_Drama(),3,0)
        grid.addWidget(self.genre4_Romance(),4,0)
        grid.addWidget(self.genre5_Horror(),5,0)
        grid.addWidget(self.genre6_SF(),1,1)
        grid.addWidget(self.genre7_Ani(),2,1)
        grid.addWidget(self.genre8_Docu(),3,1)
        grid.addWidget(self.genre9_Indie(),4,1)
        grid.addWidget(self.genre10_Concert(),5,1)
        grid.addWidget(self.doneBtn,6,0)
        grid.addWidget(self.gotoNextBtn,6,1)



        #선택완료버튼 기본 색깔은 연두색.
        # self.doneBtn.setStyleSheet("background-color:purple")


        #라디오 버튼이 클릭되기 전에는 "다음으로" 버튼이 비활성화 상태. 
        #이후에 클릭하면 버튼이 활성화(누를수있게되고) 버튼 색깔이 (회색에서 연두색으로 바뀜)
        self.gotoNextBtn.setEnabled(False)  
        # self.gotoNextBtn.setStyleSheet("background-color:rgb(169,169,169)")


        self.question.setStyleSheet("color: black;"
        

                    "font-family: 'GMARKETSANSMEDIUM';"
                    "font-size: 25px;")

        self.g1button1.setStyleSheet("color: black;"

                    "font-family: 'netmarble';"
                    
                    "font-size: 19px;")

        self.g1button0.setStyleSheet("color: black;"

                    "font-family: 'netmarble';"
                   
                    "font-size: 19px;")


        self.g2button1.setStyleSheet("color: black;"

                    "font-family: 'netmarble';"
                    
                    "font-size: 19px;")

        self.g2button0.setStyleSheet("color: black;"

                    "font-family: 'netmarble';"
                   
                    "font-size: 19px;")

        self.g3button1.setStyleSheet("color: black;"

                    "font-family: 'netmarble';"
                    
                    "font-size: 19px;")

        self.g3button0.setStyleSheet("color: black;"

                    "font-family: 'netmarble';"
                   
                    "font-size: 19px;")

        self.g4button1.setStyleSheet("color: black;"

                    "font-family: 'netmarble';"
                    
                    "font-size: 19px;")

        self.g4button0.setStyleSheet("color: black;"

                    "font-family: 'netmarble';"
                   
                    "font-size: 19px;")

        self.g5button1.setStyleSheet("color: black;"

                    "font-family: 'netmarble';"
                    
                    "font-size: 19px;")

        self.g5button0.setStyleSheet("color: black;"

                    "font-family: 'netmarble';"
                   
                    "font-size: 19px;")

        self.g6button1.setStyleSheet("color: black;"

                    "font-family: 'netmarble';"
                    
                    "font-size: 19px;")

        self.g6button0.setStyleSheet("color: black;"

                    "font-family: 'netmarble';"
                   
                    "font-size: 19px;")

        self.g7button1.setStyleSheet("color: black;"

                    "font-family: 'netmarble';"
                    
                    "font-size: 19px;")

        self.g7button0.setStyleSheet("color: black;"

                    "font-family: 'netmarble';"
                   
                    "font-size: 19px;")

        self.g8button1.setStyleSheet("color: black;"

                    "font-family: 'netmarble';"
                    
                    "font-size: 19px;")

        self.g8button0.setStyleSheet("color: black;"

                    "font-family: 'netmarble';"
                   
                    "font-size: 19px;")

        self.g9button1.setStyleSheet("color: black;"

                    "font-family: 'netmarble';"
                    
                    "font-size: 19px;")

        self.g9button0.setStyleSheet("color: black;"

                    "font-family: 'netmarble';"
                   
                    "font-size: 19px;")

        self.g10button1.setStyleSheet("color: black;"

                    "font-family: 'netmarble';"
                    
                    "font-size: 19px;")

        self.g10button0.setStyleSheet("color: black;"

                    "font-family: 'netmarble';"
                   
                    "font-size: 19px;")


        self.leGenre1.setStyleSheet("color: black;"

                    "font-family: 'NEXON LV1 GOTHIC OTF';"
                    "font-weight:bold;"
                    "font-size: 20px;")

        self.leGenre2.setStyleSheet("color: black;"

                    "font-family: 'NEXON LV1 GOTHIC OTF';"
                    "font-weight:bold;"
                    "font-size: 20px;")

        self.leGenre3.setStyleSheet("color: black;"

                    "font-family: 'NEXON LV1 GOTHIC OTF';"
                    "font-weight:bold;"
                    "font-size: 20px;")

        self.leGenre4.setStyleSheet("color: black;"

                    "font-family: 'NEXON LV1 GOTHIC OTF';"
                    "font-weight:bold;"
                    "font-size: 20px;")

        self.leGenre5.setStyleSheet("color: black;"

                    "font-family: 'NEXON LV1 GOTHIC OTF';"
                    "font-weight:bold;"
                    "font-size: 20px;")

        self.leGenre6.setStyleSheet("color: black;"

                    "font-family: 'NEXON LV1 GOTHIC OTF';"
                    "font-weight:bold;"
                    "font-size: 20px;")

        self.leGenre7.setStyleSheet("color: black;"

                    "font-family: 'NEXON LV1 GOTHIC OTF';"
                    "font-weight:bold;"
                    "font-size: 20px;")

        self.leGenre8.setStyleSheet("color: black;"

                    "font-family: 'NEXON LV1 GOTHIC OTF';"
                    "font-weight:bold;"
                    "font-size: 20px;")

        self.leGenre9.setStyleSheet("color: black;"

                    "font-family: 'NEXON LV1 GOTHIC OTF';"
                    "font-weight:bold;"
                    "font-size: 20px;")


        self.leGenre10.setStyleSheet("color: black;"

                    "font-family: 'NEXON LV1 GOTHIC OTF';"
                    "font-weight:bold;"
                    "font-size: 20px;")

        self.doneBtn.setStyleSheet("color: black;"

                    "font-family: 'GMARKETSANSMEDIUM';"
                    "font-weight:bold;"
                    "font-size: 20px;"
                    "background-color: #9aafda;"
             )
      

        self.gotoNextBtn.setStyleSheet("color: black;"

                    "font-family: 'GMARKETSANSMEDIUM';"
                    "font-weight:bold;"
                    "font-size: 20px;"
                    "background-color: #6E727D;"
                    
                    
             )

        self.groupboxQ.setStyleSheet("background-color: #E7CEBF;")


        self.setLayout(grid)


        self.setWindowTitle("영화 취향 선택!")
        # self.setGeometry(50,50,1100,730) #메인 창의 위치와 크기
        self.setWindowTitle("OTTRS movie") #창 타이틀 이름

        self.show()


    def btnClicked(self):

        #장르1 
        if self.g1button1.isChecked():   #만약에. g1button1(버튼-"장르1_액션"&"좋아함").체크되었다면,
            self.userGenreList[0]=1                #userGenreList[0]=1 값.   #리스트의 시작은 0번째부터이기 때문에.
            # print("장르1",self.userGenreList[0])
        
        elif self.g1button0.isChecked():  #만약에. g1button0(버튼-"장르1_액션"&"좋아하지않음").체크되었다면,    
            self.userGenreList[0]=0                #userGenreList[0]=0 값.
            # print("장르1",self.userGenreList[0])


        #장르2
        if self.g2button1.isChecked():   #만약에. g2button1(버튼-"장르2_코미디"&"좋아함").체크되었다면,
            self.userGenreList[1]=1                #self.genre2=1 값.
            # print("장르2",self.userGenreList[1])
        
        elif self.g2button0.isChecked():  #만약에. g2button0(버튼-"장르2_코미디"&"좋아하지않음").체크되었다면,    
            self.userGenreList[1]=0                #self.genre2=0 값.
            # print("장르2",self.userGenreList[1])

        #장르3
        if self.g3button1.isChecked():   
            self.userGenreList[2]=1                
  
        elif self.g3button0.isChecked():    
            self.userGenreList[2]=0               


        #장르4
        if self.g4button1.isChecked():   
            self.userGenreList[3]=1                
      
        elif self.g4button0.isChecked():    
            self.userGenreList[3]=0               


        #장르5
        if self.g5button1.isChecked():   
            self.userGenreList[4]=1                
       
        elif self.g5button0.isChecked():    
            self.userGenreList[4]=0               
   

        #장르6
        if self.g6button1.isChecked():   
            self.userGenreList[5]=1                
        
        elif self.g6button0.isChecked():    
            self.userGenreList[5]=0               
 

        #장르7
        if self.g7button1.isChecked():   
            self.userGenreList[6]=1                
        
        elif self.g7button0.isChecked():    
            self.userGenreList[6]=0               
 

        #장르8
        if self.g8button1.isChecked():   
            self.userGenreList[7]=1                
        
        if self.g8button0.isChecked():    
            self.userGenreList[7]=0                

        #장르9
        if self.g9button1.isChecked():   
            self.userGenreList[8]=1                
        
        elif self.g9button0.isChecked():    
            self.userGenreList[8]=0               
  

        #장르10
        if self.g10button1.isChecked():   
            self.userGenreList[9]=1                
    
        elif self.g10button0.isChecked():    
            self.userGenreList[9]=0               
   
        


    def doneClicked(self):                 #모든 장르에 대한 선택이 모두 완료되면 "다음으로 버튼" 활성화
        if (self.g1button1.isChecked() or self.g1button0.isChecked()) and (self.g2button1.isChecked() or self.g2button0.isChecked()) and (self.g3button1.isChecked() or self.g3button0.isChecked()) and (self.g4button1.isChecked() or self.g4button0.isChecked()) and (self.g5button1.isChecked() or self.g5button0.isChecked()) and (self.g6button1.isChecked() or self.g6button0.isChecked()) and (self.g7button1.isChecked() or self.g7button0.isChecked()) and (self.g8button1.isChecked() or self.g8button0.isChecked()) and (self.g9button1.isChecked() or self.g9button0.isChecked()) and (self.g10button1.isChecked() or self.g10button0.isChecked()):
            # print("okay")
            self.gotoNextBtn.setEnabled(True)  #다음으로 버튼 활성화
            # self.gotoNextBtn.setStyleSheet("background-color:rgb(154,205,50)")  #버튼 색깔 회색에서 연두색으로.
            self.gotoNextBtn.setStyleSheet("background-color: #9aafda;"
                    "color: black;"    
                    "font-family: 'GMARKETSANSMEDIUM';"
                    "font-weight:bold;"
                    "font-size: 20px;"
                    )


    def gotoNext(self):
        print(self.userGenreList)
        print("다음으로 버튼 눌림")
        #survey2 화면으로 가야함
        #self.userGenreList가 [1, 0, 1, 0, 1, 0, 1, 0, 1, 0] 과 같이 프린트됨. (1: 좋아함 의미/ 0: 좋아하지않음 의미)
        self.pp.initSurvey_2(self.userGenreList)

        
     

    def boxQ(self):
        self.groupboxQ= QGroupBox()

        #포스터 라벨 넣기
        vbox = QVBoxLayout()
        vbox.addWidget(self.question)
        self.groupboxQ.setLayout(vbox)
        return self.groupboxQ


    #영역 정의
    def genre1_Action(self):
        groupbox= QGroupBox()
        hbox = QHBoxLayout()
        hbox.addWidget(self.leGenre1)
        hbox.addWidget(self.g1button1)
        hbox.addWidget(self.g1button0)
        groupbox.setLayout(hbox)
        return groupbox


    def genre2_Comedy(self):
        groupbox= QGroupBox()
        hbox = QHBoxLayout()
        hbox.addWidget(self.leGenre2)
        hbox.addWidget(self.g2button1)
        hbox.addWidget(self.g2button0)
        groupbox.setLayout(hbox)
        return groupbox

    def genre3_Drama(self):
        groupbox= QGroupBox()
        hbox = QHBoxLayout()
        hbox.addWidget(self.leGenre3)
        hbox.addWidget(self.g3button1)
        hbox.addWidget(self.g3button0)
        groupbox.setLayout(hbox)
        return groupbox

    def genre4_Romance(self):
        groupbox= QGroupBox()
        hbox = QHBoxLayout()
        hbox.addWidget(self.leGenre4)
        hbox.addWidget(self.g4button1)
        hbox.addWidget(self.g4button0)
        groupbox.setLayout(hbox)
        return groupbox

    def genre5_Horror(self):
        groupbox= QGroupBox()
        hbox = QHBoxLayout()
        hbox.addWidget(self.leGenre5)
        hbox.addWidget(self.g5button1)
        hbox.addWidget(self.g5button0)
        groupbox.setLayout(hbox)
        return groupbox

    def genre6_SF(self):
        groupbox= QGroupBox()
        hbox = QHBoxLayout()
        hbox.addWidget(self.leGenre6)
        hbox.addWidget(self.g6button1)
        hbox.addWidget(self.g6button0)
        groupbox.setLayout(hbox)
        return groupbox

    def genre7_Ani(self):
        groupbox= QGroupBox()
        hbox = QHBoxLayout()
        hbox.addWidget(self.leGenre7)
        hbox.addWidget(self.g7button1)
        hbox.addWidget(self.g7button0)
        groupbox.setLayout(hbox)
        return groupbox

    def genre8_Docu(self):
        groupbox= QGroupBox()
        hbox = QHBoxLayout()
        hbox.addWidget(self.leGenre8)
        hbox.addWidget(self.g8button1)
        hbox.addWidget(self.g8button0)
        groupbox.setLayout(hbox)
        return groupbox

    def genre9_Indie(self):
        groupbox= QGroupBox()
        hbox = QHBoxLayout()
        hbox.addWidget(self.leGenre9)
        hbox.addWidget(self.g9button1)
        hbox.addWidget(self.g9button0)
        groupbox.setLayout(hbox)
        return groupbox

    def genre10_Concert(self):
        groupbox= QGroupBox()
        hbox = QHBoxLayout()
        hbox.addWidget(self.leGenre10)
        hbox.addWidget(self.g10button1)
        hbox.addWidget(self.g10button0)
        groupbox.setLayout(hbox)
        return groupbox


if __name__ == "__main__":
    a = QApplication(sys.argv)
    e = Survey()
    sys.exit(a.exec_())