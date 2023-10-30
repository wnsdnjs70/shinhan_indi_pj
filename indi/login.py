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

'''
    신한아이 인디 자동로그인 예제
'''

class IndiWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IndiExample")

        # 일반 TR OCX
        self.IndiTR = QAxWidget("GIEXPERTCONTROL.GiExpertControlCtrl.1")

        # 신한i Indi 자동로그인
        while True:
            login = self.IndiTR.StartIndi('id', 'password', 'authpassword', 'C:\SHINHAN-i\indi\giexpertstarter.exe')
            print(login)
            if login == True :
                break

if __name__ == "__main__":
    app = QApplication(sys.argv)
    IndiWindow = IndiWindow()
    IndiWindow.show()
    app.exec_()
