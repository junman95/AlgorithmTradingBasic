import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Kiwoom login
        self.kiwoom=QAxWidget("A1574A0D-6BFA-4BD7-9020-DED88711818D")
        self.kiwoom.dynamicCall("CommConnect()")

        #Kiwoom API+ Event
        self.kiwoom.OnEventConnect.connect(self.event_connect)

        self.setWindowTitle("계좌 정보 확인")
        self.setGeometry(300,300,300,15)

        btn1=QPushButton("계좌 얻기",self)
        btn1.move(190,20)
        btn1.clicked.connect(self.btn1_clicked)

        self.text_edit=QTextEdit(self)
        self.text_edit.setGeometry(10,60,280,80)

    def btn1_clicked(self):
        account_num=self.kiwoom.dynamicCall("GetLoginInfo(Qstring)",["ACCNO"])
        account_id = self.kiwoom.dynamicCall("GetLoginInfo(Qstring)", ["USER_ID"])
        self.text_edit.append("계죄번호: "+account_num.rstrip(';'))
        self.text_edit.append(("아이디: "+account_id.rstrip(';')))

    def event_connect(self,err_code):
        if err_code==0:
            self.text_edit.append("로그인 성공")

if __name__=="__main__":
    app=QApplication(sys.argv)
    myWindow=MyWindow()
    myWindow.show()
    app.exec_()