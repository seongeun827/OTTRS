import sys
import cx_Oracle

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        # 라벨이랑 버튼 만들기
        self.width = 500
        self.height = 500

        self.labelTest = QLabel("Test", self)

        self.initUI()

    def initUI(self):

        # 라벨 버튼 위치정하기
        self.labelTest.setGeometry(30, 60, 300, 300)
        # 창 이름 정하기
        self.setWindowTitle("메인창 창")

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())