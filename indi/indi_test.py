import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
import pandas as pd
import GiExpertControl as giLogin # 통신 모듈 로그인할거
import GiExpertControl as giJongmokTRShow # GiExpertControl은 우리가 파일 넣어줬던거 GiExpertControl.py 이거
import GiExpertControl as giJongmokRealTime # 
import GiExpertControl as buy
from TestUI import Ui_MainWindow

main_ui = Ui_MainWindow()

class indiWindow(QMainWindow): # 
    # UI 선언
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IndiExample")
        giJongmokTRShow.SetQtMode(True)
        giJongmokTRShow.RunIndiPython()
        giLogin.RunIndiPython()
        giJongmokRealTime.RunIndiPython()
        buy.RunIndiPython()
        self.rqidD = {}
        main_ui.setupUi(self)      

        main_ui.pushButton.clicked.connect(self.pushButton_clicked)
        main_ui.pushButton_2.clicked.connect(self.pushButton_2_clicked)
        main_ui.pushButton_3.clicked.connect(self.pushButton_3_clicked)
        giJongmokTRShow.SetCallBack('ReceiveData', self.giJongmokTRShow_ReceiveData) # 단일조회
        giJongmokRealTime.SetCallBack('ReceiveRTData', self.giJongmokRealTime_ReceiveRTData) # 실시간조회
        buy.SetCallBack('ReceiveRTData', self.buy_ReceiveRTData) # 매수
        
        # print(giLogin.GetCommState())
        # if giLogin.GetCommState() == 0: # 정상
        #     print("")        
        # elif  giLogin.GetCommState() == 1: # 비정상
        # #본인의 ID 및 PW 넣으셔야 합니다.
        #     login_return = giLogin.StartIndi('아이디','비밀번호','공인인증서 비밀번호', 'C:\\SHINHAN-i\\indi\\GiExpertStarter.exe')
        #     if login_return == True:
        #         print("INDI 로그인 정보","INDI 정상 호출")
        #     else:
        #         print("INDI 로그인 정보","INDI 호출 실패")                    

    def pushButton_clicked(self): # 위에 버튼
        gaejwa_text = main_ui.textEdit.toPlainText()
        PW_text = main_ui.textEdit_2.toPlainText() # pyqt에 입력된 값들,,
        TR_Name = "SABA200QB"          
        ret = giJongmokTRShow.SetQueryName(TR_Name)          
        # print(giJongmokTRShow.GetErrorCode())
        # print(giJongmokTRShow.GetErrorMessage())
        ret = giJongmokTRShow.SetSingleData(0,gaejwa_text)
        ret = giJongmokTRShow.SetSingleData(1,"01")
        ret = giJongmokTRShow.SetSingleData(2,PW_text) # 세팅,,
        rqid = giJongmokTRShow.RequestData() # 요청
        print(type(rqid))
        print('Request Data rqid: ' + str(rqid))
        self.rqidD[rqid] = TR_Name    
        
    def pushButton_2_clicked(self):      
        jongmokCode = main_ui.textEdit_3.toPlainText()
        rqid = giJongmokRealTime.RequestRTReg("SC",jongmokCode) # SC에 종목을 등록하겠다.
        print(type(rqid))
        print('Request Data rqid: ' + str(rqid))        
        
    def giJongmokTRShow_ReceiveData(self,giCtrl,rqid): # 맨위 버튼 값 처리
        print("in receive_Data:",rqid)
        print('recv rqid: {}->{}\n'.format(rqid, self.rqidD[rqid])) #
        TR_Name = self.rqidD[rqid]
        tr_data_output = []
        output = []

        print("TR_name : ",TR_Name)
        if TR_Name == "SABA200QB":
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
                       
    def giJongmokRealTime_ReceiveRTData(self,giCtrl,RealType):
        if RealType == "SC":
            main_ui.tableWidget_2.insertRow(main_ui.tableWidget_2.rowCount())
            final_rowCount = main_ui.tableWidget_2.rowCount() - 1
            main_ui.tableWidget_2.setItem(final_rowCount,0,QTableWidgetItem(str(giCtrl.GetSingleData(1))))
            main_ui.tableWidget_2.setItem(final_rowCount,1,QTableWidgetItem(str(giCtrl.GetSingleData(2))))
            main_ui.tableWidget_2.setItem(final_rowCount,2,QTableWidgetItem(str(giCtrl.GetSingleData(3))))
            main_ui.tableWidget_2.setItem(final_rowCount,3,QTableWidgetItem(str(giCtrl.GetSingleData(6))))
            
    def pushButton_3_clicked(self): # 시세 등록 끄는거.
        giJongmokRealTime.UnRequestRTReg("SC", "")
    
    def buy_ReceiveRTData(self):
        SetSingleData

if __name__ == "__main__": # 1. 맨처음 메인 탄다.
    app = QApplication(sys.argv)
    IndiWindow = indiWindow()    
    IndiWindow.show()
    app.exec_()
    
    # if IndiWindow.MainSymbol != "":
    #     giJongmokRealTime.UnRequestRTReg("SC", "")