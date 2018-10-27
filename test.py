from PyQt5 import QtWidgets
from login_window import Ui_Login_Window
import sys
import copy
import os

class ApplicationWindow(QtWidgets.QMainWindow):
	def test_clicked(self):
		self.ui.mylab.setText(str(self.i))
		self.i += 1

	def login_clicked(self):
		self.user = copy.copy(self.ui.username.text())
		self.pwd = copy.copy(self.ui.pwd.text())
		self.ui.pwd.setText("")
		self.ui.username.setText("")
		if len(self.user) == 0 or len(self.pwd) == 0:
			QtWidgets.QMessageBox.critical(self, "error", "Enter something!")
			return
		QtWidgets.QMessageBox.information(self, "warining", "username: %s\npassword: %s\n" % (self.user, self.pwd))

	def reg_clicked(self):
		self.user = copy.copy(self.ui.username.text())
		self.pwd = copy.copy(self.ui.pwd.text())
		self.ui.pwd.setText("")
		self.ui.username.setText("")
		if len(self.user) == 0 or len(self.pwd) == 0:
			QtWidgets.QMessageBox.critical(self, "error", "Enter something!")
			return
		QtWidgets.QMessageBox.information(self, "cong", "username: %s\npassword: %s\ncreated!" % (self.user, self.pwd))


	def __init__(self):
		super(ApplicationWindow, self).__init__()
		self.user = None
		self.pwd = None
		self.i = 0
		self.other = None
		self.ui = Ui_Login_Window()
		self.ui.setupUi(self)
		self.ui.reg.clicked.connect(self.reg_clicked)
		self.ui.login.clicked.connect(self.login_clicked)
		self.ui.test.clicked.connect(self.test_clicked)


def start():
	app = QtWidgets.QApplication(sys.argv)
	application = ApplicationWindow()
	application.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	start()