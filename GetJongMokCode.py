import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.kiwoom = QAxWidget("A1574A0D-6BFA-4BD7-9020-DED88711818D")
        self.kiwoom.dynamicCall("CommConnect()")

        #종목 코드
        self.setWindowTitle("종목코드")
        self.setGeometry(300,300,300,150)

        btn1=QPushButton("종목코드 얻기 ",self)
        btn1.clicked.connect(self.btn1_clicked)

        self.listWidget = QListWidget(self)
        self.listWidget.setGeometry(10,10,170,130)

    def btn1_clicked(self):
        ret=self.kiwoom.dynamicCall("GetCodeListByMarket(Qstring)",["0"])
        kospi_code_list = ret.split(';')
        kospi_code_name_list=[]

        for x in kospi_code_list:
            name= self.kiwoom.dynamicCall("GetMasterCodeName(Qstring)",[x])
            kospi_code_name_list.append(x+":"+name)

        self.listWidget.addItems(kospi_code_name_list)


if __name__=="__main__":
    app=QApplication(sys.argv)
    myWindow=MyWindow()
    myWindow.show()
    sys.exit(app.exec_())