import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import PyQt5
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from pandas import Series, DataFrame
import pandas as pd
import numpy as np


class IndiWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IndiExample")

        # 일반 TR OCX
        self.IndiTR = QAxWidget("GIEXPERTCONTROL.GiExpertControlCtrl.1")
        self.IndiTR.ReceiveData.connect(self._ReceiveData)
        self.IndiTR.ReceiveSysMsg.connect(self.ReceiveSysMsg) # 일반 TR에 대한 응답을 받는 함수를 연결해 줍니다.

        # TR ID를 저장해놓고 처리할 딕셔너리 생성
        self.rqidD = {}

        # PyQt5를 통해 화면을 그려주는 코드입니다.
        self.MainSymbol = ""
        self.edSymbol = QLineEdit(self)
        self.edSymbol.setGeometry(20, 20, 60, 20)
        self.edSymbol.setText("")

        # PyQt5를 통해 버튼만들고 함수와 연결시킵니다.
        btnResearch = QPushButton("Search", self)
        btnResearch.setGeometry(85, 20, 50, 20)
        btnResearch.clicked.connect(self.btn_Search)  # 버튼을 누르면 'btn_Search' 함수가 실행됩니다.


    # 버튼을 누르면 조회함수를 호출하도록 합니다.
    def btn_Search(self):
        # 본인의 계좌정보와 원하는 종목코드, 주문유형 등을 입력해주세요!!
        self.order(27051806068, 0000, 'A005930', 70000, 1, 2, 1)


    # 주식을 주문합니다.    
    def order(self, account_num, pwd, code, price, count, order_type, call_type):
        """ 현물 주문을 요청한다.(TR : SABA101U1)
        :param code: 종목코드
        :param count: 주문수량
        :param order_type: (2:매수, 1:매도)
        :return:
        """
        ret = self.IndiTR.dynamicCall("SetQueryName(QString)", "SABA101U1")
        ret = self.IndiTR.dynamicCall("SetSingleData(int, QString)", 0, str(account_num))  # 계좌번호
        ret = self.IndiTR.dynamicCall("SetSingleData(int, QString)", 1, "01")  # 상품구분
        ret = self.IndiTR.dynamicCall("SetSingleData(int, QString)", 2, str(pwd))  # 비밀번호
        ret = self.IndiTR.dynamicCall("SetSingleData(int, QString)", 5, '0')  # 선물대용매도구분
        ret = self.IndiTR.dynamicCall("SetSingleData(int, QString)", 6, '00')  # 신용거래구분
        ret = self.IndiTR.dynamicCall("SetSingleData(int, QString)", 7, str(order_type))  # 매수매도 구분
        ret = self.IndiTR.dynamicCall("SetSingleData(int, QString)", 8, 'A' + str(code))  # 종목코드
        ret = self.IndiTR.dynamicCall("SetSingleData(int, QString)", 9, str(count))  # 주문수량
        #ret = self.IndiTR.dynamicCall("SetSingleData(int, QString)", 10, str(price))  # 주문가격
        ret = self.IndiTR.dynamicCall("SetSingleData(int, QString)", 11, '1')  # 정규장
        ret = self.IndiTR.dynamicCall("SetSingleData(int, QString)", 12, call_type)  # 호가유형, 1: 시장가, X:최유리, Y:최우선
        ret = self.IndiTR.dynamicCall("SetSingleData(int, QString)", 13, '0')  # 주문조건, 0:일반, 3:IOC, 4:FOK
        ret = self.IndiTR.dynamicCall("SetSingleData(int, QString)", 14, '0')  # 신용대출
        ret = self.IndiTR.dynamicCall("SetSingleData(int, QString)", 21, 'Y')  # 결과 출력 여부
        rqid = self.IndiTR.dynamicCall("RequestData()")  # 데이터 요청

        # 요청한 ID를 저장합니다.
        self.rqidD[rqid] = "SABA101U1"
        #self.codeID[rqid] = code
        print("매매TR요청 : ", rqid)


    def _ReceiveData(self, rqid):
        TRName = self.rqidD[rqid]

        if TRName == "SABA101U1":
            DATA = {}
            DATA['Order_Num'] = self.IndiTR.dynamicCall("GetSingleData(int)", 0)  # 주문번호
            DATA['Num'] = self.IndiTR.dynamicCall("GetSingleData(int)", 2)  # 메시지 구분
            DATA['Msg1'] = self.IndiTR.dynamicCall("GetSingleData(int)",  3)  # 메시지1
            DATA['Msg2'] = self.IndiTR.dynamicCall("GetSingleData(int)", 4)  # 메시지2
            DATA['Msg3'] = self.IndiTR.dynamicCall("GetSingleData(int)", 5)  # 메시지3
            print("매수 및 매도 주문결과 :", DATA)

    def ReceiveSysMsg(self, MsgID):
        print("System Message Received = ", MsgID)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    IndiWindow = IndiWindow()
    IndiWindow.show()
    app.exec_()
