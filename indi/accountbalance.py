# -*- coding: utf-8 -*-
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
        super(IndiWindow, self).__init__()

        # QT 타이틀
        self.setWindowTitle("IndiExample")

        # 인디의 TR을 처리할 변수를 생성합니다.
        #self.IndiTR = QAxWidget("GIEXPERTCONTROL64.GiExpertControl64Ctrl.1")
        self.IndiTR = QAxWidget("GIEXPERTCONTROL.GiExpertControlCtrl.1")

        # Indi API event
        self.IndiTR.ReceiveData.connect(self.ReceiveData)
        self.IndiTR.ReceiveSysMsg.connect(self.ReceiveSysMsg)
        self.rqidD = {} # TR 관리를 위해 사전 변수를 하나 생성합니다.

        # PyQt5를 통해 화면을 그려주는 코드입니다.
        self.MainSymbol = ""
        self.edSymbol = QLineEdit(self)
        self.edSymbol.setGeometry(20, 20, 160, 20)
        self.edSymbol.setText("")

        # PyQt5를 통해 버튼만들고 함수와 연결시킵니다.
        btnResearch = QPushButton("Search", self)
        btnResearch.setGeometry(20, 45, 50, 20)
        btnResearch.clicked.connect(self.btn_Search)  # 버튼을 누르면 'btn_Search' 함수가 실행됩니다.

    # 계좌번호를 입력하고 버튼을 누르면 조회를 요청합니다.
    def btn_Search(self):
        # SABA200QB : 계좌별 잔고 조회를 요청할 TR입니다.
        # 해당 TR의 필드입력형식에 맞춰서 TR을 날리면 됩니다.
        # 데이터 요청 형식은 다음과 같습니다.
        ret = self.IndiTR.dynamicCall("SetQueryName(QString)", "SABA200QB")
        ret = self.IndiTR.dynamicCall("SetSingleData(int, QString)", 0, str(self.MainSymbol))  # 계좌번호
        ret = self.IndiTR.dynamicCall("SetSingleData(int, QString)", 1, "01") # 상품구분 항상 '01'
        ret = self.IndiTR.dynamicCall("SetSingleData(int, QString)", 2, "password")  # 비밀번호
        rqid = self.IndiTR.dynamicCall("RequestData()")  # 데이터 요청
        self.rqidD[rqid] =  "SABA200QB"

    # 요청한 TR로 부터 데이터를 받는 함수입니다.
    def ReceiveData(self, rqid):
        # TR을 날릴때 ID를 통해 TR이름을 가져옵니다.
        TRName = self.rqidD[rqid]

        # SABA200QB에 대한 요청 결과를 받습니다.
        if TRName == "SABA200QB" :
            # GetMultiRowCount()는 TR 결과값의 multi row 개수를 리턴합니다.
            nCnt = self.IndiTR.dynamicCall("GetMultiRowCount()")
            print(nCnt)

            # 받을 열만큼 가거 데이터를 받도록 합니다.
            for i in range(0, nCnt):
                # 데이터 양식
                DATA = {}

                # 데이터 받기
                DATA['ISIN_CODE'] = self.IndiTR.dynamicCall("GetMultiData(int, int)", i, 0)  # 표준코드
                DATA['NAME'] = self.IndiTR.dynamicCall("GetMultiData(int, int)", i, 1)  # 종목명
                DATA['NUM'] = int(self.IndiTR.dynamicCall("GetMultiData(int, int)", i, 2))  # 결재일 잔고 수량
                DATA['SELL_UNFINISHED_NUM'] = int(self.IndiTR.dynamicCall("GetMultiData(int, int)", i, 3))  # 매도 미체결 수량
                DATA['BUY_UNFINISHED_NUM'] = int(self.IndiTR.dynamicCall("GetMultiData(int, int)", i, 4))  # 매수 미체결 수량
                DATA['CURRENT_PRC'] = self.IndiTR.dynamicCall("GetMultiData(int, int)", i, 5)  # 현재가
                DATA['AVG_PRC'] = float(self.IndiTR.dynamicCall("GetMultiData(int, int)", i, 6))  # 평균단가
                DATA['CREDIT_NUM'] = int(self.IndiTR.dynamicCall("GetMultiData(int, int)", i, 7))  # 신용잔고수량
                DATA['KOSPI_NUM'] = int(self.IndiTR.dynamicCall("GetMultiData(int, int)", i, 8))  # 코스피대용수량
                print(DATA)

        self.rqidD.__delitem__(rqid)

    # 시스템 메시지를 받은 경우 출력합니다.
    def ReceiveSysMsg(self, MsgID):
        print("System Message Received = ", MsgID)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    IndiWindow = IndiWindow()
    IndiWindow.show()
    app.exec_()
