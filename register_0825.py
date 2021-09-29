import sys
import cx_Oracle
import re

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class RegisterWindow(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.pp = parent

        self.width = 1100
        self.height = 730

        # self.oImage = QImage("E:\pythonStudy\ottrsProject\\back.png")

        # self.sImage = self.oImage.scaled(QSize(1100,730))                   # resize Image to widgets size

        # self.palette = QPalette()

        # self.palette.setBrush(10, QBrush(self.sImage))                     # 10 = Windowrole

        # self.setPalette(self.palette)

        # 회원가입

        self.hbackground = QLabel("hback", self)
        self.background = QPixmap(".\hbackgroundreal.png")
        self.background = self.background.scaled(1100, 730, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.hbackground.setPixmap(self.background)

        self.labelname = QLabel("Register", self)
        self.labelEmail = QLabel("Email", self)
        self.lineEmail = QLineEdit(self)
        self.lineEmail.setPlaceholderText('Please enter your email')

        self.labelPW = QLabel("PW", self)
        self.linePW = QLineEdit(self)
        self.linePW.setPlaceholderText('Please enter your password')
        self.linePW.setEchoMode(QLineEdit.Password)

        self.labelPWCheck = QLabel("PW_Check", self)
        self.linePWCheck = QLineEdit(self)
        self.linePWCheck.setPlaceholderText('Please enter your password again')
        self.linePWCheck.setEchoMode(QLineEdit.Password)

        self.linePwinfo = QLabel("패스워드 20자 이내 ,문자는 ~!@?.만 허용 ", self)

        self.btnSignUp = QPushButton("Sign-Up", self)
        self.loginBtn = QPushButton("Login", self)
        self.btnSignUp.clicked.connect(self.signUP)
        self.loginBtn.clicked.connect(self.gotoLogin)

        self.initUI()

    # def set_background_img(self,url):
    #     oImage=QImage(url)
    #     sImage=oImage.scaled(QSize(1100,730))
    #     palette = QPalette()
    #     palette.setBrush(10, QBrush(sImage))
    #     self.setPalette(palette)

    def gotoLogin(self):
        self.pp.initLogin()

    def PwPolicy(self, Pw):
        pw = Pw
        paw = re.compile("[a-zA-Z0-9~!@?.]+")
        for val1 in paw.findall(pw):
            return pw == val1

    def EmailPolicy(self, Email):
        email = Email
        ema = re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+[.][a-zA-Z0-9.]+")
        v = ema.findall(email)
        if len(v) != 0:
            for value in ema.findall(email):
                return email == value
        else:
            return False

    def signUP(self):
        print("여기에 가입완료 한 후 어떤거 실행 할지 나와야 함")
        # 회원 가입한 내용들이 DB에 저장되도록 할 것임
        # email, pw, pwcheck 받은 텍스트 값을 변수로 정하고 오라클에 변수 내용 저장

        regiConditionError = True

        email = self.lineEmail.text()
        pw = self.linePW.text()
        pwcheck = self.linePWCheck.text()

        # 이메일 형식인지 체크 해야함
        if self.EmailPolicy(email) != True:
            rep = QMessageBox.question(self, '에러', '지원하는 이메일 형식이 아닙니다.', QMessageBox.Ok)
            print("5. 지원하는 이메일 형식이 아닙니다.")

        else:
            print("1. 이메일 형식 만족")
            # pw와 pw가 같은 체크 필수!!!
            if self.PwPolicy(pw) != True:
                rep = QMessageBox.question(self, '에러', '패스워드 형식이 아닙니다.', QMessageBox.Ok)
                print("7. 패스워드가 형식 바르지 않음")
                # 패
            else:
                if pw != pwcheck:
                    rep = QMessageBox.question(self, '에러', '패스워드가 일치하지 않습니다.', QMessageBox.Ok)
                    print("4. 패스워드가 일치하지 않습니다")
                else:
                    print("2. 패스워드 두개 일치")
                    # 그 이메일이 존재하는지 확인해야함
                    connection = cx_Oracle.connect(
                        "scott", "tigertiger", "orcl.cgnlgvycsnjd.us-east-2.rds.amazonaws.com:1521/orcl")
                    cur = connection.cursor()
                    sql = """
                    SELECT 1
                    FROM OTTRS_USER
                    WHERE userEmail =:email
                    """
                    cur.execute(sql, email=self.lineEmail.text())
                    for value in cur:
                        if value != None:
                            regiConditionError = False
                            print("3. 같은 이메일이 있다")
                            rep = QMessageBox.question(self, '오류', '다른 이메일로 가입할 수 있다.', QMessageBox.Ok)
                    if regiConditionError == True:
                        print("6. 데이터에 일치하는 이메일이 없으므로 사용 가능")
                        sql = """
                        INSERT INTO OTTRS_USER VALUES ( OTTRS_USER_SEQ.NEXTVAL, :userEmail, :userPw)
                        """
                        cur.execute(sql, userEmail=email, userPw=pw)
                        connection.commit()
                        rep = QMessageBox.question(self, '가입완료', '가입이 완료되었습니다.', QMessageBox.Ok)

                        connection.close()
                        self.pp.initLogin()

        # self.hide()

    def initUI(self):

        # 위치 시키기
        # self.backimage.setGeometry(0,0,1100,730)
        self.labelname.move(550, 220)
        self.labelEmail.setGeometry(430, 310, 60, 20)
        self.labelPW.setGeometry(430, 350, 60, 20)
        self.labelPWCheck.setGeometry(430, 390, 100, 20)
        self.btnSignUp.setGeometry(440, 490, 100, 23)
        self.loginBtn.setGeometry(580, 490, 100, 23)

        self.lineEmail.setGeometry(530, 310, 160, 20)
        self.linePW.setGeometry(530, 350, 160, 20)
        self.linePWCheck.setGeometry(530, 390, 160, 20)
        self.linePwinfo.setGeometry(430, 410, 300, 100)

        self.linePwinfo.setStyleSheet("color: #494650;"

                                      "font-family: '넥슨Lv1고딕 Low OTF';"
                                      "font-size: 12px;")

        self.labelname.setStyleSheet("color: black;"

                                     "font-family: '넥슨Lv1고딕 Low OTF';"
                                     "font-weight:bold;"
                                     "font-size: 30px;")

        self.labelEmail.setStyleSheet("color: black;"

                                      "border-style: solid;"

                                      # "border-color: yellow;"
                                      # "border-radius: 3px;"
                                      "font-family: '넥슨Lv1고딕 Low OTF';"
                                      "font-size: 18px;")
        self.labelPW.setStyleSheet("color: black;"
                                   "border-style : solid;"
                                   "font-size: 18px;"
                                   # "border-color: yellow;"

                                   "font-family: '넥슨Lv1고딕 Low OTF';"
                                   )
        self.labelPWCheck.setStyleSheet("color: black;"
                                        "border-style : solid;"
                                        "font-size: 18px;"
                                        # "border-color: yellow;"

                                        "font-family: '넥슨Lv1고딕 Low OTF';"
                                        )

        self.btnSignUp.setStyleSheet("color: #494650;"
                                     "background-color: #87CEFA;"
                                     "border-style: dashed;"
                                     "font-family: 'Infinity Sans';"
                                     "font-size: 18px;"
                                     "border-color: black;")
        self.loginBtn.setStyleSheet("color: black;"
                                    "background-color: #87CEFA;"
                                    "border-style: dashed;"
                                    "font-family: 'Infinity Sans';"
                                    "font-size: 18px;"
                                    "border-color: black;")

        self.pp.setWindowTitle("OTTRS Register")

        # self.resize(300, 360)
        # self.move(100, 100)
        # self.show()


# stylesheet="""
#     RegisterWindow{
#             background-image : url("E:\pythonStudy\ottrsProject\back.png");
#             background-repeat:no-repeat;
#             background-position:center;
#         }

#         """

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ex = RegisterWindow()
    sys.exit(app.exec_())