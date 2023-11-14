import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
import pandas as pd
import GiExpertControl as giJongmokTRShow
import GiExpertControl as giJongmokRealTime
from junwonUI import Ui_MainWindow
from datetime import datetime
from telegram import Telegram
from functools import partial
import time

main_ui = Ui_MainWindow()
#telegram = Telegram()

class indiWindow(QMainWindow):
    # UI 선언
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IndiExample")
        giJongmokTRShow.SetQtMode(True)
        giJongmokTRShow.RunIndiPython()
        #giJongmokRealTime.RunIndiPython()
        self.rqidD = {}
        self.stock_dict = {}
        #self.searchFlag = True
        main_ui.setupUi(self)
        #telegram.sendMessage("인디 시작")

        #main_ui.pushButton_1.clicked.connect(self.pushButton_1_clicked) # 지수 시작
        #main_ui.pushButton_2.clicked.connect(self.pushButton_2_clicked) # 지수 종료

        #main_ui.pushButton_3.clicked.connect(self.pushButton_3_clicked) # 검색기 시작 TR_1505_03(신고가)+ TR_1864 (거래량급등락)
        #main_ui.pushButton_4.clicked.connect(self.pushButton_4_clicked) # 검색기 종료

        main_ui.recommendBtn.clicked.connect(self.recommendBtnClicked) # 종목 선별

        main_ui.buyBtn.clicked.connect(self.buyBtnClicked) # 매수
        main_ui.sellBtn.clicked.connect(self.sellBtnClicked) # 매도

        main_ui.balanceBtn.clicked.connect(self.balanceBtnClicked) # 잔고조회

        giJongmokTRShow.SetCallBack('ReceiveData', self.giJongmokTRShow_ReceiveData)
        #giJongmokRealTime.SetCallBack('ReceiveRTData', self.giJongmokRealTime_ReceiveRTData)


    def buyBtnClicked(self): # 매수
        print('매수시작')
        account = main_ui.account.toPlainText()
        password = main_ui.password.toPlainText()
        itemCode = 'A' + main_ui.itemCode.toPlainText()
        orderPrice = main_ui.price.toPlainText()
        quantity = main_ui.count.value()
        TR_Name = "SABA101U1"

        print(account)
        print(password)
        print(itemCode)
        print(orderPrice)
        print(quantity)
        print(TR_Name)
        ret = giJongmokTRShow.SetQueryName(TR_Name)
        ret = giJongmokTRShow.SetSingleData(0, account)  # 계좌번호
        ret = giJongmokTRShow.SetSingleData(1, "01")  # 계좌상품
        ret = giJongmokTRShow.SetSingleData(2, password)  # 비밀번호
        ret = giJongmokTRShow.SetSingleData(3, "")
        ret = giJongmokTRShow.SetSingleData(4, "")
        ret = giJongmokTRShow.SetSingleData(5, "0")  # 선물대용매도여부
        ret = giJongmokTRShow.SetSingleData(6, "00")  # 신용거래구분
        ret = giJongmokTRShow.SetSingleData(7, "2")  # 매도/매수 구분
        ret = giJongmokTRShow.SetSingleData(8, itemCode)  # 종목코드
        ret = giJongmokTRShow.SetSingleData(9, str(quantity))  # 주문 수량
        ret = giJongmokTRShow.SetSingleData(10, orderPrice)  # 주문 가격
        ret = giJongmokTRShow.SetSingleData(11, "1")  # 정규시간외구분코드
        ret = giJongmokTRShow.SetSingleData(12, "2")  # 호가유형코드
        ret = giJongmokTRShow.SetSingleData(13, "0")  # 주문조건코드
        ret = giJongmokTRShow.SetSingleData(14, "0")  # 신용대출통합주문구분코드
        ret = giJongmokTRShow.SetSingleData(15, "")  # 신용대출일자
        ret = giJongmokTRShow.SetSingleData(16, "")  # 원주문번호
        ret = giJongmokTRShow.SetSingleData(17, "")
        ret = giJongmokTRShow.SetSingleData(18, "")
        ret = giJongmokTRShow.SetSingleData(19, "")
        ret = giJongmokTRShow.SetSingleData(20, "")  # 프로그램매매여부
        ret = giJongmokTRShow.SetSingleData(21, "Y")  # 결과메시지 처리여부
        rqid = giJongmokTRShow.RequestData()
        print(giJongmokTRShow.GetErrorCode())
        print(giJongmokTRShow.GetErrorMessage())
        print(type(rqid))
        print('Request Data rqid: ' + str(rqid))
        self.rqidD[rqid] = TR_Name

    def sellBtnClicked(self): # 매도
        print('매도시작')
        account = main_ui.account.toPlainText()
        password = main_ui.password.toPlainText()
        itemCode = 'A' + main_ui.itemCode.toPlainText()
        orderPrice = main_ui.price.toPlainText()
        quantity = main_ui.count.value()
        TR_Name = "SABA101U1"
        print(account)
        print(password)
        print(itemCode)
        print(orderPrice)
        print(quantity)
        print(TR_Name)
        ret = giJongmokTRShow.SetQueryName(TR_Name)
        ret = giJongmokTRShow.SetSingleData(0, account)  # 계좌번호
        ret = giJongmokTRShow.SetSingleData(1, "01")  # 계좌상품
        ret = giJongmokTRShow.SetSingleData(2, password)  # 계좌비번
        ret = giJongmokTRShow.SetSingleData(3, "")
        ret = giJongmokTRShow.SetSingleData(4, "")
        ret = giJongmokTRShow.SetSingleData(5, "0")  # 선물대용매도여부
        ret = giJongmokTRShow.SetSingleData(6, "00")  # 신용거래구분
        ret = giJongmokTRShow.SetSingleData(7, "1")  # 매도/매수 구분
        ret = giJongmokTRShow.SetSingleData(8, itemCode)  # 종목코드
        ret = giJongmokTRShow.SetSingleData(9, str(quantity))  # 주문 수량
        ret = giJongmokTRShow.SetSingleData(10, orderPrice)  # 주문 가격
        ret = giJongmokTRShow.SetSingleData(11, "1")  # 정규시간외구분코드
        ret = giJongmokTRShow.SetSingleData(12, "2")  # 호가유형코드
        ret = giJongmokTRShow.SetSingleData(13, "0")  # 주문조건코드
        ret = giJongmokTRShow.SetSingleData(14, "0")  # 신용대출통합주문구분코드
        ret = giJongmokTRShow.SetSingleData(15, "")  # 신용대출일자
        ret = giJongmokTRShow.SetSingleData(16, "")  # 원주문번호
        ret = giJongmokTRShow.SetSingleData(17, "")
        ret = giJongmokTRShow.SetSingleData(18, "")
        ret = giJongmokTRShow.SetSingleData(19, "")
        ret = giJongmokTRShow.SetSingleData(20, "")  # 프로그램매매여부
        ret = giJongmokTRShow.SetSingleData(21, "Y")  # 결과메시지 처리여부
        rqid = giJongmokTRShow.RequestData()
        print(giJongmokTRShow.GetErrorCode())
        print(giJongmokTRShow.GetErrorMessage())
        print(type(rqid))
        print('Request Data rqid: ' + str(rqid))
        self.rqidD[rqid] = TR_Name

    #def recommendBtnclicked(self):


    def balanceBtnClicked(self): # 계좌 조회
        print('계좌 조회 시작')
        account = main_ui.account.toPlainText()
        password = main_ui.password.toPlainText()
        TR_Name = "SABA200QB"

        ret = giJongmokTRShow.SetQueryName(TR_Name)
        ret = giJongmokTRShow.SetSingleData(0,account)
        ret = giJongmokTRShow.SetSingleData(1,"01")
        ret = giJongmokTRShow.SetSingleData(2,password) # 세팅,,
        rqid = giJongmokTRShow.RequestData() # 요청
        print(giJongmokTRShow.GetErrorCode())
        print(giJongmokTRShow.GetErrorMessage())
        print(type(rqid))
        print('Request Data rqid: ' + str(rqid))
        self.rqidD[rqid] = TR_Name

    def giJongmokTRShow_ReceiveData(self, giCtrl, rqid):
        print("in receive_Data:", rqid)
        print('recv rqid: {}->{}\n'.format(rqid, self.rqidD[rqid]))
        TR_Name = self.rqidD[rqid]

        print(TR_Name)

        if TR_Name == "SABA101U1": # 매수/매도
            print("매수매도 값")
            nCnt = giCtrl.GetSingleRowCount()
            print("c")
            print(nCnt)
            if nCnt != 0:
                print((str(giCtrl.GetSingleData(0))))
                print((str(giCtrl.GetSingleData(1))))
                print((str(giCtrl.GetSingleData(2))))
                print((str(giCtrl.GetSingleData(3))))
                print((str(giCtrl.GetSingleData(4))))
                print((str(giCtrl.GetSingleData(5))))
            else:
                print("주문이 정상적으로 처리되지 않았습니다.")

        if TR_Name == "SABA200QB": # 계좌 조회
            nCnt = giCtrl.GetMultiRowCount()
            main_ui.accountTable.setRowCount(nCnt)
            for i in range(0, nCnt):
                main_ui.accountTable.setItem(i,0,QTableWidgetItem(str(giCtrl.GetMultiData(i, 0)))) # 종목코드
                main_ui.accountTable.setItem(i,1,QTableWidgetItem(str(giCtrl.GetMultiData(i, 1)))) # 종목명
                main_ui.accountTable.setItem(i,2,QTableWidgetItem(str(giCtrl.GetMultiData(i, 2)).lstrip('0'))) # 결제일잔고수량
                main_ui.accountTable.setItem(i,3,QTableWidgetItem(str(giCtrl.GetMultiData(i, 5)).lstrip('0'))) # 현재가
                main_ui.accountTable.setItem(i,4,QTableWidgetItem(str(giCtrl.GetMultiData(i, 6)).lstrip('0'))) # 평균단가


class Stock:
    def __init__(self, jongmokCode, name, price, riseRate, volume, volumePower):
        self.jongmokCode = jongmokCode
        self.name = name
        self.price = price
        self.riseRate = riseRate
        self.volume = volume
        self.volumePower = volumePower

if __name__ == "__main__":
    app = QApplication(sys.argv)
    IndiWindow = indiWindow()
    IndiWindow.show()
    app.exec_()
