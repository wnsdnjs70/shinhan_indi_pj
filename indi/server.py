from telegram.ext.updater import Updater 
from telegram.update import Update 
from telegram.ext.callbackcontext import CallbackContext 
from telegram.ext.commandhandler import CommandHandler 
from telegram.ext.messagehandler import MessageHandler 
from telegram.ext.filters import Filters 
import sys
import pandas as pd
import GiExpertControl as giJongmokTRShow
import GiExpertControl as giJongmokRealTime
from datetime import datetime
from telegram import Telegram
import time

updater = Updater("6723010335:AAHcgR1yxO9vN81w7fTNLEDR5d_e_erf1kg",
				use_context=True) 


def start(update: Update, context: CallbackContext): 
	update.message.reply_text( 
		"Hello sir, Welcome to the Bot.Please write\ /help to see the commands available.")

def help(update: Update, context: CallbackContext): 
	update.message.reply_text("""Available Commands :- 
	/youtube - To get the youtube URL 
	/linkedin - To get the LinkedIn profile URL 
	/gmail - To get gmail URL 
	/geeks - To get the GeeksforGeeks URL""") 


def gmail_url(update: Update, context: CallbackContext):
	update.message.reply_text( 
		"Your gmail link here (I am not\ giving mine one for security reasons)")


def youtube_url(update: Update, context: CallbackContext): 
	update.message.reply_text("Youtube Link =>\ https://www.youtube.com/")


def linkedIn_url(update: Update, context: CallbackContext): 
	update.message.reply_text( 
		"LinkedIn URL => \ https://www.linkedin.com/in/dwaipayan-bandyopadhyay-007a/")


def geeks_url(update: Update, context: CallbackContext): 
	update.message.reply_text( 
		"GeeksforGeeks URL => https://www.geeksforgeeks.org/") 


def unknown(update: Update, context: CallbackContext): 
	update.message.reply_text( 
		"Sorry '%s' is not a valid command" % update.message.text) 


def unknown_text(update: Update, context: CallbackContext): 
	update.message.reply_text( 
		"Sorry I can't recognize you , you said '%s'" % update.message.text)


def giJongmokTRShow_ReceiveData(self, giCtrl, rqid):
	print("in receive_Data:", rqid)
	print('recv rqid: {}->{}\n'.format(rqid, self.rqidD[rqid]))
	TR_Name = self.rqidD[rqid]

	print(TR_Name)

	if TR_Name == "TR_3100_D":  # 뉴스
		nCnt = giCtrl.GetMultiRowCount()
		main_ui.tableWidget_3.setRowCount(nCnt)
		for i in range(0, nCnt):
			main_ui.tableWidget_3.setItem(i, 0, QTableWidgetItem(str(giCtrl.GetMultiData(i, 0))))
			main_ui.tableWidget_3.setItem(i, 1, QTableWidgetItem(str(giCtrl.GetMultiData(i, 2))))

	if TR_Name == "SABA101U1":  # 매수/매도
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

	if TR_Name == "SABA200QB":  # 계좌 조회
		nCnt = giCtrl.GetMultiRowCount()
		main_ui.tableWidget_4.setRowCount(nCnt)
		for i in range(0, nCnt):
			main_ui.tableWidget_4.setItem(i, 0, QTableWidgetItem(str(giCtrl.GetMultiData(i, 0))))  # 종목코드
			main_ui.tableWidget_4.setItem(i, 1, QTableWidgetItem(str(giCtrl.GetMultiData(i, 1))))  # 종목명
			main_ui.tableWidget_4.setItem(i, 2,
										  QTableWidgetItem(str(giCtrl.GetMultiData(i, 2)).lstrip('0')))  # 결제일잔고수량
			main_ui.tableWidget_4.setItem(i, 3, QTableWidgetItem(str(giCtrl.GetMultiData(i, 5)).lstrip('0')))  # 현재가
			main_ui.tableWidget_4.setItem(i, 4,
										  QTableWidgetItem(str(giCtrl.GetMultiData(i, 6)).lstrip('0')))  # 평균단가
			main_ui.tableWidget_4.setItem(i, 5,
										  QTableWidgetItem(str(giCtrl.GetMultiData(i, 3)).lstrip('0')))  # 매수미체결수량
			main_ui.tableWidget_4.setItem(i, 6,
										  QTableWidgetItem(str(giCtrl.GetMultiData(i, 4)).lstrip('0')))  # 매도미체결수량

	if TR_Name == "TR_1864":  # 거래량 급등락 종목 조회
		nCnt = giCtrl.GetMultiRowCount()
		print("거래량 급등종목")
		print(nCnt)
		idx = 0
		main_ui.tableWidget_2.setRowCount(nCnt)
		stock_messages = []
		for i in range(0, nCnt):
			jongmokCode = str(giCtrl.GetMultiData(i, 1))  # 단축코드
			name = str(giCtrl.GetMultiData(i, 2))  # 한글종목명
			price = str(giCtrl.GetMultiData(i, 3))  # 현재가
			riseRate = str(giCtrl.GetMultiData(i, 6))  # 전일대비율
			volume = str(giCtrl.GetMultiData(i, 7))  # 누적거래량
			volumePower = str(giCtrl.GetMultiData(i, 13))  # 체결강도
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

	if TR_Name == "TR_1505_03":  # 신고가/ 신저가
		nCnt = giCtrl.GetMultiRowCount()
		main_ui.tableWidget_2.setRowCount(nCnt)

		for i in range(0, nCnt):
			jongmokCode = str(giCtrl.GetMultiData(i, 0))  # 단축코드
			name = str(giCtrl.GetMultiData(i, 1))  # 한글종목명
			price = str(giCtrl.GetMultiData(i, 2))  # 현재가
			riseRate = str(giCtrl.GetMultiData(i, 5))  # 전일대비율
			volume = str(giCtrl.GetMultiData(i, 8))  # 누적거래량
			volumePower = str(giCtrl.GetMultiData(i, 13))  # 체결강도
			self.stock_dict[jongmokCode] = Stock(jongmokCode, name, price, riseRate, volume, volumePower)  # map에 추가
	# time.sleep(10)


def giJongmokRealTime_ReceiveRTData(self, giCtrl, RealType):
	if RealType == "IC":
		if main_ui.tableWidget_1.rowCount() == 0:
			main_ui.tableWidget_1.insertRow(main_ui.tableWidget_1.rowCount() + 1)
		if str(giCtrl.GetSingleData(0)) == '0001':  # 코스피지수
			main_ui.tableWidget_1.setItem(0, 0, QTableWidgetItem(str(giCtrl.GetSingleData(0))))  # 업종코드
			main_ui.tableWidget_1.setItem(0, 1, QTableWidgetItem(str(giCtrl.GetSingleData(2))))  # 장구분
			main_ui.tableWidget_1.setItem(0, 2, QTableWidgetItem(str(giCtrl.GetSingleData(3))))  # 현재지수
			main_ui.tableWidget_1.setItem(0, 3, QTableWidgetItem(str(giCtrl.GetSingleData(6))))  # 전일대비율
			main_ui.tableWidget_1.setItem(0, 4, QTableWidgetItem(str(giCtrl.GetSingleData(8))))  # 누적거래대금
		if str(giCtrl.GetSingleData(0)) == '1001':  # 코스닥지수
			main_ui.tableWidget_1.setItem(1, 0, QTableWidgetItem(str(giCtrl.GetSingleData(0))))  # 업종코드
			main_ui.tableWidget_1.setItem(1, 1, QTableWidgetItem(str(giCtrl.GetSingleData(2))))  # 장구분
			main_ui.tableWidget_1.setItem(1, 2, QTableWidgetItem(str(giCtrl.GetSingleData(3))))  # 현재지수
			main_ui.tableWidget_1.setItem(1, 3, QTableWidgetItem(str(giCtrl.GetSingleData(6))))  # 전일대비율
			main_ui.tableWidget_1.setItem(1, 4, QTableWidgetItem(str(giCtrl.GetSingleData(8))))  # 누적거래대금
updater.dispatcher.add_handler(CommandHandler('start', start)) 
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown)) 
updater.dispatcher.add_handler(MessageHandler( 
	Filters.command, unknown)) # Filters out unknown commands 

# Filters out unknown messages. 
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text)) 

updater.start_polling()

giJongmokTRShow.SetCallBack('ReceiveData', giJongmokTRShow_ReceiveData)
giJongmokRealTime.SetCallBack('ReceiveRTData', giJongmokRealTime_ReceiveRTData)
