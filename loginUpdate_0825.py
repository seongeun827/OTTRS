import sys
import cx_Oracle

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# login ver#1
# class Login(QWidget):
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.pp = parent
#         # 라벨이랑 버튼 만들기
#         self.width = 400
#         self.height = 500
#
#         self.labelEmail = QLabel("Email", self)
#         self.lineEmail = QLineEdit(self)
#         self.lineEmail.setPlaceholderText('Please enter your email')
#
#         self.labelPw = QLabel("PW", self)
#         self.linePw = QLineEdit(self)
#         self.linePw.setPlaceholderText('Please enter your email')
#         self.linePw.setEchoMode(QLineEdit.Password)
#
#         self.btnSignIn = QPushButton("Sign-In", self)
#         self.btnSignUp = QPushButton("Sign-up", self)
#         self.btnGotoMain = QPushButton("goTOMain", self)
#         self.btnGotoSurvey = QPushButton("goToSurvey", self)
#
#         self.initUI()
#
#     def initUI(self):
#
#         # 라벨 버튼 위치정하기
#         self.labelEmail.setGeometry(30, 60, 56, 12)
#         self.lineEmail.setGeometry(100, 60, 113, 20)
#
#         self.labelPw.setGeometry(30, 90, 56, 12)
#         self.linePw.setGeometry(100, 90, 113, 20)
#
#         self.btnSignIn.setGeometry(30, 230, 75, 23)
#         self.btnSignUp.setGeometry(130, 230, 75, 23)
#
#         self.btnGotoMain.setGeometry(30, 310, 75, 23)
#         self.btnGotoSurvey.setGeometry(130, 310, 75, 23)
#
#         self.btnSignIn.clicked.connect(self.loginApp)
#         self.btnSignUp.clicked.connect(self.signupApp)
#         self.btnGotoMain.clicked.connect(self.goToMain)
#         self.btnGotoSurvey.clicked.connect(self.goToSurvey)
#
#         # 창 이름 정하기
#         self.setWindowTitle("LoginForm")
#         # 위치와 크기 정하기
#         self.setGeometry(100, 100, 240, 320)
#
#         self.show()
#
#     def goToSurvey(self):
#         print("goToSurvey")
#         self.pp.initSurvey()
#
#     def goToMain(self):
#         print("goToMain")
#         self.pp.initMainWidget()
#
#     def loginApp(self):
#         # print("로그인 버튼 누름 로그인 성공 확인한다음 성공하면  메인 화면으로 가야함")
#         # print("로그인 합니다")
#
#         # 1.connection 객체 생성
#         connection = cx_Oracle.connect("scott", "tigertiger", "orcl.cgnlgvycsnjd.us-east-2.rds.amazonaws.com:1521/orcl")
#         # 2.cursor 객체 생성
#         cur = connection.cursor()
#         # 3.사용할 sql문 객체
#         sql = """
#         SELECT 1
#         FROM OTTRS_USER
#         WHERE userEmail=:email and userPw=:pw
#         """
#         # 4.실행
#         cur.execute(sql, email=self.lineEmail.text(), pw=self.linePw.text())
#
#         print("------------------------------------------")
#         # 5.로직 처리
#
#         loginFlag = False
#
#         for value in cur:
#             # print(value,type(value))
#             if value != None:
#                 rep = QMessageBox.question(self, "로그인 성공", "환영합니다", QMessageBox.Yes)
#                 if rep == QMessageBox.Yes:
#                     print("메인 화면으로 보내줄 것")
#                     # 만약에 Yes 이면 메인 창으로 가도록 설계
#                     loginFlag = True
#                     self.pp.initSurvey()
#
#         if loginFlag == False:
#             buttonReply = QMessageBox.question(self, '오류', "다시 입력 하세요", QMessageBox.Ok)
#             print("아이와 패스워드가 없음")
#
#         # 6.자원 반납 ! 필수
#         connection.close()
#
#     def signupApp(self):
#         print("회원 가입 버튼 누름 회원 가입 창 으로 가야함")
#         self.pp.initRegisterWindow()


# class RegisterWindow(QWidget):
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.pp = parent
#         self.width = 240
#         self.height= 320
#
#         # 회원가입
#         self.labelEmail = QLabel("Email", self)
#         self.labelPW = QLabel("PW", self)
#         self.labelPWCheck = QLabel("PW_Check", self)
#
#         self.lineEmail = QLineEdit(self)
#         self.linePW = QLineEdit(self)
#         self.linePWCheck = QLineEdit(self)
#
#         self.btnSignUp = QPushButton("Sign-Up", self)
#         self.btnSignUp.clicked.connect(self.signUP)
#
#         self.initUI()
#
#     def initUI(self):
#         # 위치 시키기
#         self.labelEmail.setGeometry(30, 60, 60, 12)
#         self.labelPW.setGeometry(30, 100, 60, 12)
#         self.labelPWCheck.setGeometry(30, 140, 60, 12)
#         self.btnSignUp.setGeometry(90, 240, 75, 23)
#
#         self.lineEmail.setGeometry(100, 60, 120, 20)
#         self.linePW.setGeometry(100, 100, 120, 20)
#         self.linePWCheck.setGeometry(100, 140, 120, 20)
#
#     def signUP(self):
#         print("여기에 가입완료 한 후 어떤거 실행 할지 나와야 함")
#         # 회원 가입한 내용들이 DB에 저장되도록 할 것임
#         # email, pw, pwcheck 받은 텍스트 값을 변수로 정하고 오라클에 변수 내용 저장
#
#         email = self.lineEmail.text()
#         pw = self.linePW.text()
#         # pw와 pw가 같은 체크 필수!!!
#         pwcheck = self.linePWCheck.text()
#
#         connection = cx_Oracle.connect("scott", "tigertiger", "orcl.cgnlgvycsnjd.us-east-2.rds.amazonaws.com:1521/orcl")
#         cur = connection.cursor()
#         sql = """
#         INSERT INTO OTTRS_USER VALUES ( OTTRS_USER_SEQ.NEXTVAL, :userEmail, :userPw)
#         """
#         cur.execute(sql, userEmail=email, userPw=pw)
#         connection.commit()
#         connection.close()
#         buttonReply = QMessageBox.question(self, '성공', "회원 가입이 완료 되었습니다. 로그인 하세요", QMessageBox.Ok)
#         self.pp.initLogin()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Login()
#     sys.exit(app.exec_())


import sys
import cx_Oracle

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Login(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.pp = parent
        # 라벨이랑 버튼 만들기
        self.width = 1100
        self.height = 730

        self.hbackground = QLabel("hback", self)
        self.background = QPixmap(".\hloginback.png")
        self.background = self.background.scaled(1100, 730, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.hbackground.setPixmap(self.background)

        self.labelname = QLabel("Login", self)
        self.labelEmail = QLabel("Email", self)
        self.lineEmail = QLineEdit(self)
        self.lineEmail.setPlaceholderText('Please enter your email')

        self.labelPw = QLabel("PW", self)
        self.linePw = QLineEdit(self)
        self.linePw.setPlaceholderText('Please enter your password')
        self.linePw.setEchoMode(QLineEdit.Password)

        self.btnSignIn = QPushButton("Sign-In", self)
        self.btnSignUp = QPushButton("Sign-up", self)
        self.btnGotoMain = QPushButton("goTOMain", self)
        self.btnGotoSurvey = QPushButton("goToSurvey", self)

        self.initUI()

    def goToSurvey(self):
        print("goToSurvey")
        self.pp.initSurvey()

    def goToMain(self):
        print("goToMain")
        self.pp.initMainWidget()

    def initUI(self):

        # 라벨 버튼 위치정하기

        self.labelname.move(550, 220)
        self.labelEmail.setGeometry(430, 310, 60, 20)
        self.labelPw.setGeometry(430, 350, 60, 20)

        self.lineEmail.setGeometry(530, 310, 160, 20)
        self.linePw.setGeometry(530, 350, 160, 20)

        self.btnSignUp.setGeometry(440, 490, 100, 23)
        self.btnSignIn.setGeometry(580, 490, 100, 23)

        self.btnSignIn.setStyleSheet("background-color:red;")

        self.btnGotoMain.setGeometry(440, 400, 100, 23)
        self.btnGotoSurvey.setGeometry(580, 400, 100, 23)

        self.btnSignIn.clicked.connect(self.loginApp)
        self.btnSignUp.clicked.connect(self.signupApp)
        self.btnGotoMain.clicked.connect(self.goToMain)
        self.btnGotoSurvey.clicked.connect(self.goToSurvey)

        self.labelname.setStyleSheet("color: black;"

                                     "font-family: '넥슨Lv1고딕 Low OTF';"
                                     "font-weight:bold;"
                                     "font-size: 30px;")

        self.labelEmail.setStyleSheet("color: black;"
                                      "border-style : solid;"
                                      "font-size: 20px;"
                                      # "border-color: yellow;"

                                      "font-family: '넥슨Lv1고딕 Low OTF';")
        self.labelPw.setStyleSheet("color: black;"
                                   "border-style : solid;"
                                   "font-size: 20px;"
                                   # "border-color: yellow;"

                                   "font-family: '넥슨Lv1고딕 Low OTF';")
        self.btnSignIn.setStyleSheet("color: #494650;"
                                     "background-color: #87CEFA;"
                                     "border-style: dashed;"
                                     "font-family: 'Infinity Sans';"
                                     "font-size: 18px;"
                                     "border-color: black;")
        self.btnSignUp.setStyleSheet("color: #494650;"
                                     "background-color: #87CEFA;"
                                     "border-style: dashed;"
                                     "font-family: 'Infinity Sans';"
                                     "font-size: 18px;"
                                     "border-color: black;")

        # 창 이름 정하기
        self.pp.setWindowTitle("OTTRS Login")
        # 위치와 크기 정하기
        self.setGeometry(100, 100, 240, 320)

        self.show()

    def loginApp(self):
        # print("로그인 버튼 누름 로그인 성공 확인한다음 성공하면  메인 화면으로 가야함")
        # print("로그인 합니다")

        # 1.connection 객체 생성
        connection = cx_Oracle.connect("scott", "tigertiger", "orcl.cgnlgvycsnjd.us-east-2.rds.amazonaws.com:1521/orcl")
        # 2.cursor 객체 생성
        cur = connection.cursor()
        # 3.사용할 sql문 객체
        sql = """    
                SELECT 1
                FROM OTTRS_USER
                WHERE userEmail=:email and userPw=:pw
                """
        # 4.실행
        cur.execute(sql, email=self.lineEmail.text(), pw=self.linePw.text())
        # self.pp.loginUserSeq = cur.fetchall()[0][0]
        print("------------------------------------------")
        # 5.로직 처리

        loginFlag = False

        for value in cur:
            # print(value,type(value))
            if value != None:
                rep = QMessageBox.question(self, "로그인 성공", "환영합니다", QMessageBox.Yes)
                if rep == QMessageBox.Yes:
                    print("메인 화면으로 보내줄 것")
                    # 만약에 Yes 이면 메인 창으로 가도록 설계
                    loginFlag = True

                    conn = cx_Oracle.connect("scott", "tigertiger",
                                             "orcl.cgnlgvycsnjd.us-east-2.rds.amazonaws.com:1521/orcl")
                    cur = conn.cursor()
                    userEmail = self.lineEmail.text()
                    print("userEmail :", userEmail)

                    sql = "SELECT USERSEQ FROM OTTRS_USER WHERE USEREMAIL='%s'" % userEmail
                    print(sql)
                    cur.execute(sql)
                    logUserSeq = cur.fetchall()[0][0]

                    self.pp.loginUserSeq = logUserSeq

                    sql = """
                            SELECT USERSEQ FROM USER_GENRE ug
                            WHERE ug.userSeq = (SELECT USERSEQ FROM OTTRS_USER WHERE USEREMAIL='%s')
                            """ % userEmail
                    print("sql :", sql)
                    cur.execute(sql)
                    logUserSeq = 0
                    exFlag = False
                    for userSeq in cur:
                        logUserSeq = userSeq[0]
                        exFlag = True

                    print("-------------------------")
                    if exFlag:
                        print(logUserSeq)

                        self.pp.initMainWidget()

                    else:
                        print("exFlag :", exFlag)
                        self.pp.initSurvey()

                    # cur.execute(sql)

        if loginFlag == False:
            buttonReply = QMessageBox.question(self, '오류', "다시 입력 하세요", QMessageBox.Ok)
            print("아이와 패스워드가 없음")

        # 6.자원 반납 ! 필수
        connection.close()

    def signupApp(self):
        print("회원 가입 버튼 누름 회원 가입 창 으로 가야함")
        self.pp.initRegisterWindow()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Login()
    sys.exit(app.exec_())