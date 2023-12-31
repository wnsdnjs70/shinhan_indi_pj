# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'junwonUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1066, 667)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.account = QtWidgets.QTextEdit(self.centralwidget)
        self.account.setGeometry(QtCore.QRect(30, 40, 241, 31))
        self.account.setObjectName("account")
        self.password = QtWidgets.QTextEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(290, 40, 131, 31))
        self.password.setObjectName("password")
        self.balanceBtn = QtWidgets.QPushButton(self.centralwidget)
        self.balanceBtn.setGeometry(QtCore.QRect(440, 40, 91, 31))
        self.balanceBtn.setObjectName("balanceBtn")
        self.itemCode = QtWidgets.QTextEdit(self.centralwidget)
        self.itemCode.setGeometry(QtCore.QRect(30, 90, 141, 31))
        self.itemCode.setObjectName("itemCode")
        self.price = QtWidgets.QTextEdit(self.centralwidget)
        self.price.setGeometry(QtCore.QRect(180, 90, 121, 31))
        self.price.setObjectName("price")
        self.count = QtWidgets.QSpinBox(self.centralwidget)
        self.count.setGeometry(QtCore.QRect(310, 90, 61, 31))
        self.count.setObjectName("count")
        self.buyBtn = QtWidgets.QPushButton(self.centralwidget)
        self.buyBtn.setGeometry(QtCore.QRect(380, 90, 71, 31))
        self.buyBtn.setStyleSheet("background-color:rgb(255, 0, 0)")
        self.buyBtn.setObjectName("buyBtn")
        self.sellBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sellBtn.setGeometry(QtCore.QRect(460, 90, 71, 31))
        self.sellBtn.setStyleSheet("background-color:rgb(0, 0, 255)")
        self.sellBtn.setObjectName("sellBtn")
        self.recommendBtn = QtWidgets.QPushButton(self.centralwidget)
        self.recommendBtn.setGeometry(QtCore.QRect(780, 40, 111, 31))
        self.recommendBtn.setObjectName("recommendBtn")
        self.buyAllBtn = QtWidgets.QPushButton(self.centralwidget)
        self.buyAllBtn.setGeometry(QtCore.QRect(900, 40, 111, 31))
        self.buyAllBtn.setObjectName("buyAllBtn")
        self.accountTable = QtWidgets.QTableWidget(self.centralwidget)
        self.accountTable.setGeometry(QtCore.QRect(30, 140, 501, 461))
        self.accountTable.setObjectName("accountTable")
        self.accountTable.setColumnCount(7)
        self.accountTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.accountTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.accountTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.accountTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.accountTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.accountTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.accountTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.accountTable.setHorizontalHeaderItem(6, item)

        self.itemTable = QtWidgets.QTableWidget(self.centralwidget)
        self.itemTable.setGeometry(QtCore.QRect(610, 90, 401, 201))
        self.itemTable.setObjectName("itemTable")
        self.itemTable.setColumnCount(0)
        self.itemTable.setRowCount(0)
        self.perCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.perCheck.setGeometry(QtCore.QRect(610, 50, 16, 16))
        self.perCheck.setChecked(True)
        self.perCheck.setObjectName("perCheck")
        self.per = QtWidgets.QLabel(self.centralwidget)
        self.per.setGeometry(QtCore.QRect(630, 50, 56, 12))
        self.per.setObjectName("per")
        self.pbrCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.pbrCheck.setGeometry(QtCore.QRect(660, 50, 16, 16))
        self.pbrCheck.setCheckable(True)
        self.pbrCheck.setChecked(True)
        self.pbrCheck.setObjectName("pbrCheck")
        self.pbr = QtWidgets.QLabel(self.centralwidget)
        self.pbr.setGeometry(QtCore.QRect(680, 50, 56, 12))
        self.pbr.setObjectName("pbr")
        self.pcrCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.pcrCheck.setGeometry(QtCore.QRect(710, 50, 16, 16))
        self.pcrCheck.setObjectName("pcrCheck")
        self.pcr = QtWidgets.QLabel(self.centralwidget)
        self.pcr.setGeometry(QtCore.QRect(730, 50, 56, 12))
        self.pcr.setObjectName("pcr")
        self.accountGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.accountGroup.setGeometry(QtCore.QRect(10, 10, 551, 611))
        self.accountGroup.setObjectName("accountGroup")
        self.itemGrouKO = QtWidgets.QGroupBox(self.centralwidget)
        self.itemGrouKO.setGeometry(QtCore.QRect(580, 10, 461, 301))
        self.itemGrouKO.setObjectName("itemGrouKO")
        self.per_us = QtWidgets.QLabel(self.centralwidget)
        self.per_us.setGeometry(QtCore.QRect(630, 360, 56, 12))
        self.per_us.setObjectName("per_us")
        self.pbr_us = QtWidgets.QLabel(self.centralwidget)
        self.pbr_us.setGeometry(QtCore.QRect(680, 360, 56, 12))
        self.pbr_us.setObjectName("pbr_us")
        self.psr_us = QtWidgets.QLabel(self.centralwidget)
        self.psr_us.setGeometry(QtCore.QRect(730, 360, 56, 12))
        self.psr_us.setObjectName("psr_us")
        self.pbrCheckUS = QtWidgets.QCheckBox(self.centralwidget)
        self.pbrCheckUS.setGeometry(QtCore.QRect(660, 360, 16, 16))
        self.pbrCheckUS.setCheckable(True)
        self.pbrCheckUS.setChecked(True)
        self.pbrCheckUS.setObjectName("pbrCheckUS")
        self.itemTableUS = QtWidgets.QTableWidget(self.centralwidget)
        self.itemTableUS.setGeometry(QtCore.QRect(610, 400, 401, 201))
        self.itemTableUS.setObjectName("itemTableUS")
        self.itemTableUS.setColumnCount(0)
        self.itemTableUS.setRowCount(0)
        self.psrCheckUS = QtWidgets.QCheckBox(self.centralwidget)
        self.psrCheckUS.setGeometry(QtCore.QRect(710, 360, 16, 16))
        self.psrCheckUS.setObjectName("psrCheckUS")
        self.perCheckUS = QtWidgets.QCheckBox(self.centralwidget)
        self.perCheckUS.setGeometry(QtCore.QRect(610, 360, 16, 16))
        self.perCheckUS.setChecked(True)
        self.perCheckUS.setObjectName("perCheckUS")
        self.itemGroupUS = QtWidgets.QGroupBox(self.centralwidget)
        self.itemGroupUS.setGeometry(QtCore.QRect(580, 320, 461, 301))
        self.itemGroupUS.setObjectName("itemGroupUS")
        self.recommendBtnUS = QtWidgets.QPushButton(self.itemGroupUS)
        self.recommendBtnUS.setGeometry(QtCore.QRect(320, 30, 111, 31))
        self.recommendBtnUS.setObjectName("recommendBtnUS")
        self.pcrCheckUS = QtWidgets.QCheckBox(self.itemGroupUS)
        self.pcrCheckUS.setGeometry(QtCore.QRect(180, 40, 16, 16))
        self.pcrCheckUS.setObjectName("pcrCheckUS")
        self.pcr_us = QtWidgets.QLabel(self.itemGroupUS)
        self.pcr_us.setGeometry(QtCore.QRect(200, 40, 56, 12))
        self.pcr_us.setObjectName("pcr_us")
        self.itemGroupUS.raise_()
        self.itemGrouKO.raise_()
        self.accountGroup.raise_()
        self.account.raise_()
        self.password.raise_()
        self.balanceBtn.raise_()
        self.itemCode.raise_()
        self.price.raise_()
        self.count.raise_()
        self.buyBtn.raise_()
        self.sellBtn.raise_()
        self.recommendBtn.raise_()
        self.buyAllBtn.raise_()
        self.accountTable.raise_()
        self.itemTable.raise_()
        self.perCheck.raise_()
        self.per.raise_()
        self.pbrCheck.raise_()
        self.pbr.raise_()
        self.pcrCheck.raise_()
        self.pcr.raise_()
        self.per_us.raise_()
        self.pbr_us.raise_()
        self.psr_us.raise_()
        self.pbrCheckUS.raise_()
        self.itemTableUS.raise_()
        self.psrCheckUS.raise_()
        self.perCheckUS.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1066, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.account.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">계좌번호</p></body></html>"))
        self.password.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">비밀번호</p></body></html>"))
        self.balanceBtn.setText(_translate("MainWindow", "잔고 조회"))
        self.itemCode.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">종목코드</p></body></html>"))
        self.price.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">주문가격</p></body></html>"))
        self.buyBtn.setText(_translate("MainWindow", "매수"))
        self.sellBtn.setText(_translate("MainWindow", "매도"))
        self.recommendBtn.setText(_translate("MainWindow", "종목 선별"))
        self.buyAllBtn.setText(_translate("MainWindow", "일괄 매수"))
        self.perCheck.setText(_translate("MainWindow", "CheckBox"))
        self.per.setText(_translate("MainWindow", "PER"))
        self.pbrCheck.setText(_translate("MainWindow", "CheckBox"))
        self.pbr.setText(_translate("MainWindow", "PBR"))
        self.pcrCheck.setText(_translate("MainWindow", "CheckBox"))
        self.pcr.setText(_translate("MainWindow", "PCR"))
        self.accountGroup.setTitle(_translate("MainWindow", "잔고 및 주문"))
        self.itemGrouKO.setTitle(_translate("MainWindow", "국내 종목 추천"))
        self.per_us.setText(_translate("MainWindow", "PER"))
        self.pbr_us.setText(_translate("MainWindow", "PBR"))
        self.psr_us.setText(_translate("MainWindow", "PSR"))
        self.pbrCheckUS.setText(_translate("MainWindow", "CheckBox"))
        self.psrCheckUS.setText(_translate("MainWindow", "CheckBox"))
        self.perCheckUS.setText(_translate("MainWindow", "CheckBox"))
        self.itemGroupUS.setTitle(_translate("MainWindow", "해외 종목 추천"))
        self.recommendBtnUS.setText(_translate("MainWindow", "종목 선별"))
        self.pcrCheckUS.setText(_translate("MainWindow", "CheckBox"))
        self.pcr_us.setText(_translate("MainWindow", "PCR"))
        item = self.accountTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "종목코드"))
        item = self.accountTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "종목명"))
        item = self.accountTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "결제일잔고수량"))
        item = self.accountTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "현재가"))
        item = self.accountTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "평균단가"))
        item = self.tableWidget_4.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "매수미체결수량"))
        item = self.tableWidget_4.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "매도미체결수량"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
