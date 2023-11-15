import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
import pandas as pd
import GiExpertControl as giJongmokTRShow
import GiExpertControl as giJongmokRealTime
from junwonUI3 import Ui_MainWindow
from datetime import datetime
from telegram import Telegram
from functools import partial
import time
import finterstellar as fs

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
        self.count = 0
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
        main_ui.recommendBtnUS.clicked.connect(self.recommendBtnUSClicked) # 종목 선별

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

    def recommendBtnClicked(self):
        TR_Name = "TR_1856_IND"
        ret = giJongmokTRShow.SetQueryName(TR_Name)
        ret = giJongmokTRShow.SetSingleData(0,"1")
        ret = giJongmokTRShow.SetSingleData(1,"2100")
        rqid = giJongmokTRShow.RequestData() # 요청
        print(giJongmokTRShow.GetErrorCode())
        print(giJongmokTRShow.GetErrorMessage())
        print(type(rqid))
        print('Request Data rqid: ' + str(rqid))
        self.rqidD[rqid] = TR_Name

    def recommendBtnUSClicked(self):
        term = '2023Q3'  # terms에 하나의 요소만 들어가 있다면 해당 값을 직접 사용
        data = fs.fn_consolidated(otp='16998495801191101151', term=term)

        # PER, PBR, PSR, PCR을 구함
        data['Market Cap'] = data['Price_M3'] * data['Shares']
        data['PER'] = data['Price_M3'] / data['EPS']
        data['PBR'] = data['Price_M3'] / (data['Shareholders Equity'] / data['Shares'])
        data['PSR'] = data['Price_M3'] / (data['Revenue'] / data['Shares'])
        data['PCR'] = data['Price_M3'] / ((data['Net Income'] + data['Depreciation']) / data['Shares'])

        market = fs.fn_filter(data, by='Market Cap', floor=0, n=1000, asc=True)
        per = fs.fn_score(data, by='PER', method='relative', floor=1, asc=True)
        pbr = fs.fn_score(data, by='PBR', method='relative', floor=0.1, asc=True)
        psr = fs.fn_score(data, by='PSR', method='relative', floor=0.1, asc=True)
        pcr = fs.fn_score(data, by='PCR', method='relative', floor=0.1, asc=True)

        psr_checked = main_ui.psrCheckUS.isChecked()
        pcr_checked = main_ui.pcrCheckUS.isChecked()

        if not psr_checked and not pcr_checked:
            print("PER, PBR로 종목 선별 중 ...")
            combined_score = fs.combine_score(per, pbr)
            combined_score.rename(columns={'Score': 'per_score', 'Score_': 'pbr_score'}, inplace=True)
            # 스코어를 기준으로 내림차순 정렬하고 상위 30개를 선택
            result = combined_score.sort_values(by='Sum', ascending=False).head(30)
            print(result)

        elif psr_checked and not pcr_checked:
            print("PER, PBR, PSR로 종목 선별 중 ...")
            combined_score = fs.combine_score(per, pbr, psr)
            combined_score.columns = ['per_score', 'pbr_score', 'psr_score', 'Sum']
            # 스코어를 기준으로 내림차순 정렬하고 상위 30개를 선택
            result = combined_score.sort_values(by='Sum', ascending=False).head(30)
            print(result)

        elif not psr_checked and pcr_checked:
            print("PER, PBR, PCR로 종목 선별 중 ...")
            combined_score = fs.combine_score(per, pbr, pcr)
            combined_score.columns = ['per_score', 'pbr_score', 'pcr_score', 'Sum']
            # 스코어를 기준으로 내림차순 정렬하고 상위 30개를 선택
            result = combined_score.sort_values(by='Sum', ascending=False).head(30)
            print(result)

        elif psr_checked and pcr_checked:
            print("PER, PBR, PSR, PCR로 종목 선별 중 ...")
            combined_score = fs.combine_score(per, pbr, psr, pcr)
            combined_score.columns = ['per_score', 'pbr_score', 'psr_score', 'pcr_score', 'Sum']
            # 스코어를 기준으로 내림차순 정렬하고 상위 30개를 선택
            result = combined_score.sort_values(by='Sum', ascending=False).head(30)
            print(result)


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
                main_ui.accountTable.setItem(i,5,QTableWidgetItem(str(giCtrl.GetMultiData(i, 4)).lstrip('0'))) # 매수미체결수량
                main_ui.accountTable.setItem(i,6,QTableWidgetItem(str(giCtrl.GetMultiData(i, 3)).lstrip('0'))) # 매도미체결수량


        if TR_Name == "TR_1856_IND":

            psr_checked = main_ui.psrCheck.isChecked()

            nCnt = giCtrl.GetMultiRowCount()

            data = []

            for i in range(nCnt):
                # 각 데이터를 가져오고 문자열로 변환
                itemNm = str(giCtrl.GetMultiData(i, 1))
                itemCd = str(giCtrl.GetMultiData(i, 0))
                price = str(giCtrl.GetMultiData(i, 2))
                PER = str(giCtrl.GetMultiData(i, 12))
                market = str(giCtrl.GetMultiData(i, 13))
                revenue = str(giCtrl.GetMultiData(i, 27))
                PBR = str(giCtrl.GetMultiData(i, 36))

                # 데이터를 리스트에 추가
                data.append([itemNm, itemCd, price, PER, market, revenue, PBR])

            # 데이터프레임으로 변환
            df = pd.DataFrame(data, columns=['itemNm', 'itemCd', 'price', 'PER', 'market', 'revenue', 'PBR'])

            # 시가총액을 기준으로 정렬
            df['market'] = pd.to_numeric(df['market'])
            df = df.sort_values(by='market', ascending=True)

            # 시가총액 하위 30% 선별
            top_20_percent = int(0.3 * len(df))
            df = df.head(top_20_percent)

            # 연산 할 숫자들 타입 변경하기
            df[['PER', 'PBR', 'market', 'revenue']] = df[['PER', 'PBR', 'market', 'revenue']].apply(pd.to_numeric)
            df['PSR'] = df['market'] / df['revenue'] * 1000

            if psr_checked:
                print("PER, PBR, PSR을 기준으로 종목 선별 중 ... ")
                # PER, PBR, PCR에 대한 상대 점수 계산
                max_score = 33.33
                df['PER_Score'] = (df['PER'].rank(ascending=True) / len(df)) * max_score
                df['PBR_Score'] = (df['PBR'].rank(ascending=True) / len(df)) * max_score
                df['PSR_Score'] = (df['PBR'].rank(ascending=True) / len(df)) * max_score

                # PER PBR 점수 합산
                df['Total_Score'] = df['PER_Score'] + df['PBR_Score'] + df['PSR_Score']

                # score 기준 정렬
                df = df.sort_values(by='Total_Score', ascending=False)
                
                # 상위 30개 아이템 선택
                includePsr = df.head(30)
                
                main_ui.itemTable.clearContents()
                main_ui.itemTable.setRowCount(30)

                for i in range(0, 30):
                    main_ui.itemTable.setItem(i, 0, QTableWidgetItem(str(includePsr.iloc[i]['itemNm'])))
                    main_ui.itemTable.setItem(i, 1, QTableWidgetItem(str(includePsr.iloc[i]['itemCd'])))
                    main_ui.itemTable.setItem(i, 2, QTableWidgetItem(str(includePsr.iloc[i]['price'])))
                    main_ui.itemTable.setItem(i, 3, QTableWidgetItem(str(includePsr.iloc[i]['Total_Score'])))
                    main_ui.itemTable.setItem(i, 4, QTableWidgetItem(str(includePsr.iloc[i]['PER_Score'])))
                    main_ui.itemTable.setItem(i, 5, QTableWidgetItem(str(includePsr.iloc[i]['PBR_Score'])))
                    main_ui.itemTable.setItem(i, 6, QTableWidgetItem(str(includePsr.iloc[i]['PSR_Score'])))

            else:
                print("PER, PBR을 기준으로 종목 선별 중 ... ")

                # PER, PBR에 대한 상대 점수 계산
                max_score = 50
                df['PER_Score'] = (df['PER'].rank(ascending=True) / len(df)) * max_score
                df['PBR_Score'] = (df['PBR'].rank(ascending=True) / len(df)) * max_score

                # PER PBR 점수 합산
                df['Total_Score'] = df['PER_Score'] + df['PBR_Score']

                # score 기준 정렬
                df = df.sort_values(by='Total_Score', ascending=False)
                
                # 상위 30개 아이템 선택
                exceptPsr = df.head(30)
                
                main_ui.itemTable.clearContents()
                main_ui.itemTable.setRowCount(30)
                for i in range(0, 30):
                    main_ui.itemTable.setItem(i, 0, QTableWidgetItem(str(exceptPsr.iloc[i]['itemNm'])))
                    main_ui.itemTable.setItem(i, 1, QTableWidgetItem(str(exceptPsr.iloc[i]['itemCd'])))
                    main_ui.itemTable.setItem(i, 2, QTableWidgetItem(str(exceptPsr.iloc[i]['price'])))
                    main_ui.itemTable.setItem(i, 3, QTableWidgetItem(str(exceptPsr.iloc[i]['Total_Score'])))
                    main_ui.itemTable.setItem(i, 4, QTableWidgetItem(str(exceptPsr.iloc[i]['PER_Score'])))
                    main_ui.itemTable.setItem(i, 5, QTableWidgetItem(str(exceptPsr.iloc[i]['PBR_Score'])))
                    main_ui.itemTable.setItem(i, 6, QTableWidgetItem(str("NAN")))


            
            

            

            



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
