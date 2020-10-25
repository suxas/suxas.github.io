import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from test import *

class Test_Demo(QMainWindow,Ui_Form):
	def __init__(self,parent=None):
		super(Test_Demo,self).__init__(parent)
		self.setupUi(self)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	test_demo = Test_Demo()
	test_demo.show()
	sys.exit(app.exec_())