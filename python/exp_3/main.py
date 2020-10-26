# -*- coding: utf-8 -*-
import sys
import os
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 30, 201, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.button1)

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 130, 201, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.button2)

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 220, 201, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.button3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "离散信号"))
        self.pushButton.setText(_translate("Form", "单位脉冲序列"))
        self.pushButton_2.setText(_translate("Form", "正弦信号"))
        self.pushButton_3.setText(_translate("Form", "复指数信号"))

class Function(QMainWindow,Ui_Form):
	def __init__(self,parent=None):
		super(Function,self).__init__(parent)
		self.setupUi(self)
	
	def button1(self):
		str1=('python button1.py')
		os.system(str1)
	def button2(self):
		str2=('python button2.py')
		os.system(str2)
	def button3(self):
		str3=('python button3.py')
		os.system(str3)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	test_demo = Function()
	test_demo.show()
	sys.exit(app.exec_())