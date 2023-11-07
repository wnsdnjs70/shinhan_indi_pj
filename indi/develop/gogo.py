import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
import pandas as pd
import GiExpertControl as giJongmokTRShow
import GiExpertControl as giJongmokRealTime
from finalUI import Ui_MainWindow
from datetime import datetime
from telegram import Telegram
import time

main_ui = Ui_MainWindow()
telegram = Telegram()

class indiWindow(QMainWindow):
    # UI 선언
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IndiExample")
        giJongmokTRShow.SetQtMode(True)
        giJongmokTRShow.RunIndiPython()
        giJongmokRealTime.RunIndiPython()
        self.rqidD = {}
        self.stock_dict = {}
        self.searchFlag = True
        main_ui.setupUi(self)
        telegram.sendMessage("인디 시작")

        main_ui.pushButton_1.clicked.connect(self.pushButton_1_clicked) # 지수 시작
        main_ui.pushButton_2.clicked.connect(self.pushButton_2_clicked) # 지수 종료

        main_ui.pushButton_3.clicked.connect(self.pushButton_3_clicked) # 검색기 시작 TR_1505_03(신고가)+ TR_1864 (거래량급등락)
        main_ui.pushButton_4.clicked.connect(self.pushButton_4_clicked) # 검색기 종료

        main_ui.pushButton_5.clicked.connect(self.pushButton_5_clicked) # 뉴스 불러오기

        main_ui.pushButton_6.clicked.connect(self.pushButton_6_clicked) # 매수
        main_ui.pushButton_7.clicked.connect(self.pushButton_7_clicked) # 매도

        main_ui.pushButton_8.clicked.connect(self.pushButton_8_clicked) # 잔고조회

        giJongmokTRShow.SetCallBack('ReceiveData', self.giJongmokTRShow_ReceiveData)
        giJongmokRealTime.SetCallBack('ReceiveRTData', self.giJongmokRealTime_ReceiveRTData)

    def pushButton_1_clicked(self): # 지수 실시간
        rqid = giJongmokRealTime.RequestRTReg("IC", "0001")  # 실시간 코스피 지수 TR
        print(type(rqid))
        print('지수실시간버튼')
        print('Request Data rqid: ' + str(rqid))

    def pushButton_2_clicked(self): # 지수 멈춤
        giJongmokRealTime.UnRequestRTReg("IC", "")
        print('지수실시간종료')

    def pushButton_3_clicked(self): # 검색기 시작
        self.searchFlag = True
        
        TR_Name = "TR_1864" # TR_1864 거래량 금등락 종목 조회
        ret = giJongmokTRShow.SetQueryName(TR_Name)
        ret = giJongmokTRShow.SetSingleData(0, "2")  # 장구분자 (전체)
        ret = giJongmokTRShow.SetSingleData(1, "1")  # 대비급등락구분(5일평균대비 급증)
        ret = giJongmokTRShow.SetSingleData(2, "2")  # 대비율 ( 100% 이상)
        ret = giJongmokTRShow.SetSingleData(3, "1") # 거래량 조건
        ret = giJongmokTRShow.SetSingleData(4, "1") # 종목조건 (전체조회)
        ret = giJongmokTRShow.SetSingleData(5, "500") # 시가총액조건 (500억)
        rqid = giJongmokTRShow.RequestData()
        print(giJongmokTRShow.GetErrorCode())
        print(giJongmokTRShow.GetErrorMessage())
        print(type(rqid))
        print('Request Data rqid: ' + str(rqid))
        self.rqidD[rqid] = TR_Name
        
        TR_Name = "TR_1505_03"  # TR_1505_03 신고가/ 신저가
        ret = giJongmokTRShow.SetQueryName(TR_Name)
        ret = giJongmokTRShow.SetSingleData(0, "2")  # 장구분자 (전체)
        ret = giJongmokTRShow.SetSingleData(1, "2")  # 종류(52주 신고가)
        ret = giJongmokTRShow.SetSingleData(2, "1")  # 거래량 조건
        ret = giJongmokTRShow.SetSingleData(3, "1")  # 종목조건 (전체조회)
        ret = giJongmokTRShow.SetSingleData(4, "500") # 시가총액조건 (500억)
        rqid = giJongmokTRShow.RequestData()
        print(giJongmokTRShow.GetErrorCode())
        print(giJongmokTRShow.GetErrorMessage())
        print(type(rqid))
        print('Request Data rqid: ' + str(rqid))
        self.rqidD[rqid] = TR_Name

    def pushButton_4_clicked(self): #검색기 종료
        # giJongmokRealTime.UnRequestRTReg("IC", "")
        self.searchFlag = False
        print('검색기종료')

    def pushButton_5_clicked(self): # 뉴스 불러오기
        TR_Name = "TR_3100_D"   
        print('뉴스시작')
        ret = giJongmokTRShow.SetQueryName(TR_Name)
        # 현재 날짜를 가져오기
        today = datetime.now()
        formatted_date = today.strftime("%Y%m%d")
        ret = giJongmokTRShow.SetSingleData(0,"055550")
        ret = giJongmokTRShow.SetSingleData(1,"1")
        ret = giJongmokTRShow.SetSingleData(2, formatted_date)
        rqid = giJongmokTRShow.RequestData() # 요청
        self.rqidD[rqid] = TR_Name

    def pushButton_6_clicked(self): # 매수
        print('매수시작')
        gaejwa_text = main_ui.textEdit_1.toPlainText()
        PW_text = main_ui.textEdit_2.toPlainText()
        jongmokCode = 'A' + main_ui.textEdit_3.toPlainText()
        orderPrice = main_ui.textEdit_4.toPlainText()
        quantity = main_ui.spinBox.value()
        TR_Name = "SABA101U1"

        print(gaejwa_text)
        print(PW_text)
        print(jongmokCode)
        print(orderPrice)
        print(quantity)
        print(TR_Name)
        ret = giJongmokTRShow.SetQueryName(TR_Name)
        ret = giJongmokTRShow.SetSingleData(0, gaejwa_text)  # 계좌번호
        ret = giJongmokTRShow.SetSingleData(1, "01")  # 계좌상품
        ret = giJongmokTRShow.SetSingleData(2, PW_text)  # 계좌비번
        ret = giJongmokTRShow.SetSingleData(3, "")
        ret = giJongmokTRShow.SetSingleData(4, "")
        ret = giJongmokTRShow.SetSingleData(5, "0")  # 선물대용매도여부
        ret = giJongmokTRShow.SetSingleData(6, "00")  # 신용거래구분
        ret = giJongmokTRShow.SetSingleData(7, "2")  # 매도/매수 구분
        ret = giJongmokTRShow.SetSingleData(8, jongmokCode)  # 종목코드
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

    def pushButton_7_clicked(self): # 매도
        print('매도시작')
        gaejwa_text = main_ui.textEdit_1.toPlainText()
        PW_text = main_ui.textEdit_2.toPlainText()
        jongmokCode = 'A' + main_ui.textEdit_3.toPlainText()
        orderPrice = main_ui.textEdit_4.toPlainText()
        quantity = main_ui.spinBox.value()
        TR_Name = "SABA101U1"
        print(gaejwa_text)
        print(PW_text)
        print(jongmokCode)
        print(orderPrice)
        print(quantity)
        print(TR_Name)
        ret = giJongmokTRShow.SetQueryName(TR_Name)
        ret = giJongmokTRShow.SetSingleData(0, gaejwa_text)  # 계좌번호
        ret = giJongmokTRShow.SetSingleData(1, "01")  # 계좌상품
        ret = giJongmokTRShow.SetSingleData(2, PW_text)  # 계좌비번
        ret = giJongmokTRShow.SetSingleData(3, "")
        ret = giJongmokTRShow.SetSingleData(4, "")
        ret = giJongmokTRShow.SetSingleData(5, "0")  # 선물대용매도여부
        ret = giJongmokTRShow.SetSingleData(6, "00")  # 신용거래구분
        ret = giJongmokTRShow.SetSingleData(7, "1")  # 매도/매수 구분
        ret = giJongmokTRShow.SetSingleData(8, jongmokCode)  # 종목코드
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

    def pushButton_8_clicked(self): # 계좌 조회
        print('계좌조회시작')
        gaejwa_text = main_ui.textEdit_1.toPlainText()
        PW_text = main_ui.textEdit_2.toPlainText()
        TR_Name = "SABA200QB"

        ret = giJongmokTRShow.SetQueryName(TR_Name)
        ret = giJongmokTRShow.SetSingleData(0,gaejwa_text)
        ret = giJongmokTRShow.SetSingleData(1,"01")
        ret = giJongmokTRShow.SetSingleData(2,PW_text) # 세팅,,
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

        if TR_Name == "TR_3100_D": # 뉴스
            nCnt = giCtrl.GetMultiRowCount()
            main_ui.tableWidget_3.setRowCount(nCnt)
            for i in range(0, nCnt):
                main_ui.tableWidget_3.setItem(i,0,QTableWidgetItem(str(giCtrl.GetMultiData(i, 0))))
                main_ui.tableWidget_3.setItem(i,1,QTableWidgetItem(str(giCtrl.GetMultiData(i, 2))))

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
            main_ui.tableWidget_4.setRowCount(nCnt)
            for i in range(0, nCnt):
                main_ui.tableWidget_4.setItem(i,0,QTableWidgetItem(str(giCtrl.GetMultiData(i, 0))))
                main_ui.tableWidget_4.setItem(i,1,QTableWidgetItem(str(giCtrl.GetMultiData(i, 1))))
                main_ui.tableWidget_4.setItem(i,2,QTableWidgetItem(str(giCtrl.GetMultiData(i, 2)).lstrip('0')))
                main_ui.tableWidget_4.setItem(i,3,QTableWidgetItem(str(giCtrl.GetMultiData(i, 5)).lstrip('0')))
                main_ui.tableWidget_4.setItem(i,4,QTableWidgetItem(str(giCtrl.GetMultiData(i, 6)).lstrip('0')))

        if TR_Name == "TR_1864": # 거래량 급등락 종목 조회
            nCnt = giCtrl.GetMultiRowCount()
            print("거래량 급등종목")
            print(nCnt)
            idx = 0
            main_ui.tableWidget_2.setRowCount(nCnt)
            stock_messages = []
            for i in range(0, nCnt):
                jongmokCode = str(giCtrl.GetMultiData(i,1)) # 단축코드
                name = str(giCtrl.GetMultiData(i,2)) # 한글종목명
                price = str(giCtrl.GetMultiData(i,3)) # 현재가
                riseRate = str(giCtrl.GetMultiData(i,6)) # 전일대비율
                volume = str(giCtrl.GetMultiData(i,7)) # 누적거래량
                volumePower = str(giCtrl.GetMultiData(i,13)) # 체결강도
                # print(jongmokCode)

                if jongmokCode in self.stock_dict:
                    found_stock = self.stock_dict.get(jongmokCode)
                    main_ui.tableWidget_2.setItem(idx, 0, QTableWidgetItem(str(jongmokCode)))
                    main_ui.tableWidget_2.setItem(idx, 1, QTableWidgetItem(str(found_stock.name)))
                    main_ui.tableWidget_2.setItem(idx, 2, QTableWidgetItem(str(found_stock.price)))
                    main_ui.tableWidget_2.setItem(idx, 3, QTableWidgetItem(str(found_stock.riseRate)))
                    main_ui.tableWidget_2.setItem(idx, 4, QTableWidgetItem(str(found_stock.volume)))
                    main_ui.tableWidget_2.setItem(idx, 5, QTableWidgetItem(str(found_stock.volumePower)))
                    idx += 1
                    message = f"{name.strip()} 현재가 {price}원 {riseRate}% 등락 중 체결강도: {volumePower}"
                    print(message)
                    stock_messages.append(message)
            if stock_messages:
                combined_message = "\n".join(stock_messages)
                telegram.sendMessage(combined_message)

        if TR_Name == "TR_1505_03": # 신고가/ 신저가
            nCnt = giCtrl.GetMultiRowCount()
            main_ui.tableWidget_2.setRowCount(nCnt)
            
            for i in range(0, nCnt):
                jongmokCode = str(giCtrl.GetMultiData(i,0)) # 단축코드
                name = str(giCtrl.GetMultiData(i,1)) # 한글종목명
                price = str(giCtrl.GetMultiData(i,2)) # 현재가
                riseRate = str(giCtrl.GetMultiData(i,5)) # 전일대비율
                volume = str(giCtrl.GetMultiData(i,8)) # 누적거래량
                volumePower = str(giCtrl.GetMultiData(i,13)) # 체결강도
                self.stock_dict[jongmokCode] = Stock(jongmokCode, name, price, riseRate, volume, volumePower) # map에 추가
            # time.sleep(10)


    def giJongmokRealTime_ReceiveRTData(self, giCtrl, RealType):
        if RealType == "IC":
            if main_ui.tableWidget_1.rowCount() == 0:
                main_ui.tableWidget_1.insertRow(main_ui.tableWidget_1.rowCount())
            main_ui.tableWidget_1.setItem(0, 0, QTableWidgetItem(str(giCtrl.GetSingleData(0))))  # 업종코드
            main_ui.tableWidget_1.setItem(0, 1, QTableWidgetItem(str(giCtrl.GetSingleData(2))))  # 장구분
            main_ui.tableWidget_1.setItem(0, 2, QTableWidgetItem(str(giCtrl.GetSingleData(3))))  # 현재지수
            main_ui.tableWidget_1.setItem(0, 3, QTableWidgetItem(str(giCtrl.GetSingleData(6))))  # 전일대비율
            main_ui.tableWidget_1.setItem(0, 4, QTableWidgetItem(str(giCtrl.GetSingleData(8))))  # 누적거래대금

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
