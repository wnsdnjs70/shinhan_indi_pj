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

main_ui = Ui_MainWindow()


class indiWindow(QMainWindow):
    # UI 선언
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IndiExample")
        giJongmokTRShow.SetQtMode(True)
        giJongmokTRShow.RunIndiPython()
        giJongmokRealTime.RunIndiPython()
        self.rqidD = {}

        main_ui.setupUi(self)

        main_ui.pushButton_1.clicked.connect(self.pushButton_1_clicked) # 지수 시작
        main_ui.pushButton_2.clicked.connect(self.pushButton_2_clicked) # 지수 종료

        main_ui.pushButton_3.clicked.connect(self.pushButton_3_clicked) # 검색기 시작 TR_1505_03(신고가)+ TR_1864 (거래량급등락)
        main_ui.pushButton_4.clicked.connect(self.pushButton_4_clicked) # 검색기 종료

        main_ui.pushButton_5.clicked.connect(self.pushButton_5_clicked) # 뉴스 종료

        giJongmokTRShow.SetCallBack('ReceiveData', self.giJongmokTRShow_ReceiveData)
        giJongmokRealTime.SetCallBack('ReceiveRTData', self.giJongmokRealTime_ReceiveRTData)

    def pushButton_1_clicked(self):
        rqid = giJongmokRealTime.RequestRTReg("IC", "0001")  # 실시간 코스피 지수 TR
        print(type(rqid))
        print('지수실시간버튼')
        print('Request Data rqid: ' + str(rqid))

    def pushButton_2_clicked(self):
        giJongmokRealTime.UnRequestRTReg("IC", "")
        print('지수실시간종료')

    def pushButton_3_clicked(self):
        rqid = giJongmokRealTime.RequestRTReg("IC", "0001")  # 검색기 TR
        print(type(rqid))
        print('검색기시작')
        print('Request Data rqid: ' + str(rqid))

    def pushButton_4_clicked(self):
        giJongmokRealTime.UnRequestRTReg("IC", "")
        print('검색기종료')

    def pushButton_5_clicked(self):
        # rqid = giJongmokRealTime.RequestRTReg("N0", "*")  # 실시간 뉴스 TR
        TR_Name = "TR_3100_D"   
        ret = giJongmokTRShow.SetQueryName(TR_Name)
        # 현재 날짜를 가져오기
        today = datetime.now()
        formatted_date = today.strftime("%Y%m%d")
        print(formatted_date)
        ret = giJongmokTRShow.SetSingleData(0,"055550")
        ret = giJongmokTRShow.SetSingleData(1,"1")
        ret = giJongmokTRShow.SetSingleData(2, formatted_date)
        rqid = giJongmokTRShow.RequestData() # 요청
        print(type(rqid))
        print('뉴스시작')
        print('Request Data rqid: ' + str(rqid))
        self.rqidD[rqid] = TR_Name

    def pushButton_6_clicked(self): # 매수
        giJongmokRealTime.UnRequestRTReg("IC", "")
        print('검색기종료')

    def pushButton_7_clicked(self): # 매도
        giJongmokRealTime.UnRequestRTReg("IC", "")
        print('검색기종료')       




    def giJongmokTRShow_ReceiveData(self, giCtrl, rqid):
        print("in receive_Data:", rqid)
        print('recv rqid: {}->{}\n'.format(rqid, self.rqidD[rqid]))
        TR_Name = self.rqidD[rqid]
        
        print("inin")
        output = []
        tr_data_output = []

        print(TR_Name)

        if TR_Name == "TR_3100_D": # 뉴스
            nCnt = giCtrl.GetMultiRowCount()
            main_ui.tableWidget_3.setRowCount(nCnt)
            for i in range(0, nCnt):
                main_ui.tableWidget_3.setItem(i,0,QTableWidgetItem(str(giCtrl.GetMultiData(i, 0))))
                main_ui.tableWidget_3.setItem(i,1,QTableWidgetItem(str(giCtrl.GetMultiData(i, 2))))

    def giJongmokRealTime_ReceiveRTData(self, giCtrl, RealType):
        if RealType == "IC":
            if main_ui.tableWidget_1.rowCount() == 0:
                main_ui.tableWidget_1.insertRow(main_ui.tableWidget_1.rowCount())
            main_ui.tableWidget_1.setItem(0, 0, QTableWidgetItem(str(giCtrl.GetSingleData(0))))  # 업종코드
            main_ui.tableWidget_1.setItem(0, 1, QTableWidgetItem(str(giCtrl.GetSingleData(2))))  # 장구분
            main_ui.tableWidget_1.setItem(0, 2, QTableWidgetItem(str(giCtrl.GetSingleData(3))))  # 현재지수
            main_ui.tableWidget_1.setItem(0, 3, QTableWidgetItem(str(giCtrl.GetSingleData(6))))  # 전일대비율
            main_ui.tableWidget_1.setItem(0, 4, QTableWidgetItem(str(giCtrl.GetSingleData(8))))  # 누적거래대금

if __name__ == "__main__":
    app = QApplication(sys.argv)
    IndiWindow = indiWindow()
    IndiWindow.show()
    app.exec_()

    # if IndiWindow.MainSymbol != "":
    #     giJongmokRealTime.UnRequestRTReg("SC", "")