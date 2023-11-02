import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
import pandas as pd
import GiExpertControl as giJongmokTRShow
import GiExpertControl as giJongmokRealTime
from TestUI import Ui_MainWindow

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
        main_ui.pushButton_6.clicked.connect(self.pushButton_6_clicked) # 뉴스 종료

        giJongmokTRShow.SetCallBack('ReceiveData', self.giJongmokTRShow_ReceiveData)
        giJongmokRealTime.SetCallBack('ReceiveRTData', self.giJongmokRealTime_ReceiveRTData)

    def pushButton_1_clicked(self):
        rqid = giJongmokRealTime.RequestRTReg("IC", "0001")  # 실시간 코스피 지수 TR
        print(type(rqid))
        print('Request Data rqid: ' + str(rqid))

    def pushButton_2_clicked(self):
        giJongmokRealTime.UnRequestRTReg("IC", "")

    def pushButton_3_clicked(self):
        rqid = giJongmokRealTime.RequestRTReg("IC", "0001")  # 실시간 코스피 지수 TR
        print(type(rqid))
        print('Request Data rqid: ' + str(rqid))

    def pushButton_4_clicked(self):
        giJongmokRealTime.UnRequestRTReg("IC", "")

    def pushButton_5_clicked(self):
        rqid = giJongmokRealTime.RequestRTReg("N2", "*")  # 실시간 뉴스 TR
        print(type(rqid))
        print('Request Data rqid: ' + str(rqid))

    def pushButton_6_clicked(self):
        giJongmokRealTime.UnRequestRTReg("N2", "")


    def giJongmokTRShow_ReceiveData(self, giCtrl, rqid):
        print("in receive_Data:", rqid)
        print('recv rqid: {}->{}\n'.format(rqid, self.rqidD[rqid]))
        TR_Name = self.rqidD[rqid]
        tr_data_output = []
        output = []

        print("TR_name : ", TR_Name)
        if TR_Name == "SABA101U1":
            nCnt = giCtrl.GetMultiRowCount()
            print("c")
            for i in range(0, nCnt):
                tr_data_output.append([])
                main_ui.tableWidget.setItem(i,0,QTableWidgetItem(str(giCtrl.GetMultiData(i, 0))))
                main_ui.tableWidget.setItem(i,1,QTableWidgetItem(str(giCtrl.GetMultiData(i, 1))))
                main_ui.tableWidget.setItem(i,2,QTableWidgetItem(str(giCtrl.GetMultiData(i, 2))))
                main_ui.tableWidget.setItem(i,3,QTableWidgetItem(str(giCtrl.GetMultiData(i, 5))))
                main_ui.tableWidget.setItem(i,4,QTableWidgetItem(str(giCtrl.GetMultiData(i, 6))))
                for j in range(0,5):
                    tr_data_output[i].append(giCtrl.GetMultiData(i, j))
            print(type(tr_data_output))

    def giJongmokRealTime_ReceiveRTData(self, giCtrl, RealType):
        if RealType == "IC":
            main_ui.tableWidget_1.insertRow(main_ui.tableWidget_1.rowCount())
            final_rowCount = main_ui.tableWidget_2.rowCount() - 1
            main_ui.tableWidget_1.setItem(final_rowCount, 0, QTableWidgetItem(str(giCtrl.GetSingleData(0))))  # 업종코드
            main_ui.tableWidget_1.setItem(final_rowCount, 1, QTableWidgetItem(str(giCtrl.GetSingleData(2))))  # 장구분
            main_ui.tableWidget_1.setItem(final_rowCount, 2, QTableWidgetItem(str(giCtrl.GetSingleData(3))))  # 현재지수
            main_ui.tableWidget_1.setItem(final_rowCount, 3, QTableWidgetItem(str(giCtrl.GetSingleData(6))))  # 전일대비율
            main_ui.tableWidget_1.setItem(final_rowCount, 4, QTableWidgetItem(str(giCtrl.GetSingleData(8))))  # 누적거래대금
        if RealType == "N2":
            main_ui.tableWidget_3.insertRow(main_ui.tableWidget_3.rowCount())
            final_rowCount = main_ui.tableWidget_2.rowCount() - 1
            main_ui.tableWidget_3.setItem(final_rowCount, 0, QTableWidgetItem(str(giCtrl.GetSingleData(0)))) # 뉴스구분
            main_ui.tableWidget_3.setItem(final_rowCount, 1, QTableWidgetItem(str(giCtrl.GetSingleData(1)))) # 뉴스일자
            main_ui.tableWidget_3.setItem(final_rowCount, 2, QTableWidgetItem(str(giCtrl.GetSingleData(2)))) # 뉴스기사번호
            main_ui.tableWidget_3.setItem(final_rowCount, 3, QTableWidgetItem(str(giCtrl.GetSingleData(5)))) # 뉴스 제목




if __name__ == "__main__":
    app = QApplication(sys.argv)
    IndiWindow = indiWindow()
    # IndiWindow.show()
    app.exec_()

    # if IndiWindow.MainSymbol != "":
    #     giJongmokRealTime.UnRequestRTReg("SC", "")