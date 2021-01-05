#coding: UTF-8
import sys
import os
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(344, 266)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(30, 30, 121, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.clicked.connect(self.button1)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 210, 71, 51))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 30, 121, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.button2)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 150, 121, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.button3)


        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 150, 121, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.button4)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(110, 90, 121, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.button5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DTMF双音多频信号的分析与识别"))
        self.pushButton_1.setText(_translate("MainWindow", "转码"))
        self.pushButton_2.setText(_translate("MainWindow", "降噪"))
        self.pushButton_3.setText(_translate("MainWindow", "测试文件分析"))
        self.pushButton_4.setText(_translate("MainWindow", "识别"))
        self.pushButton_5.setText(_translate("MainWindow", "原始样本分析"))
        self.label.setText(_translate("MainWindow", "Ver1.2"))


class Function(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(Function,self).__init__(parent)
        self.setupUi(self)
        
    def button1(self):
        str1=('ffmpeg -i test//test.m4a test//test.wav')
        os.system(str1)
    def button2(self):
        str2=('sox test//test.wav test//test_new.wav noisered noise.prof 0.23')
        os.system(str2)
    def button3(self):
        str1=('python single_analyzer.py')
        os.system(str1)
    def button4(self):
        str1=('python detector.py test//test_new.wav')
        os.system(str1)
    def button5(self):
        str1=('python all_analyzer.py')
        os.system(str1)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	test_demo = Function()
	test_demo.show()
	sys.exit(app.exec_())