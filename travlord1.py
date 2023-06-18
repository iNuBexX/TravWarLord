# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TravLord_Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep

class Ui_MainWindow(object):
    def __init__(self):
        self.loggedin: False
        self.driver:webdriver.Chrome()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(809, 505)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 130, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 210, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.inputemail = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputemail.setGeometry(QtCore.QRect(260, 160, 191, 31))
        self.inputemail.setObjectName("inputemail")
        self.inputpassword = QtWidgets.QLineEdit(self.centralwidget)
        self.inputpassword.setGeometry(QtCore.QRect(260, 240, 191, 31))
        self.inputpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputpassword.setObjectName("inputpassword")
        self.buttonlogin = QtWidgets.QPushButton(self.centralwidget)
        self.buttonlogin.setGeometry(QtCore.QRect(410, 290, 91, 31))
        self.buttonlogin.setObjectName("buttonlogin")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(230, 300, 91, 17))
        self.checkBox.setObjectName("checkBox")
        self.world = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.world.setGeometry(QtCore.QRect(110, 360, 491, 31))
        self.world.setObjectName("world")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 21))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menufile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.buttonlogin.clicked.connect(lambda: self.loginclicked("login was clicked"))

    def loginclicked(self,text):
        mail = self.inputemail.toPlainText()
        password = self.inputpassword.text()
        world = self.world.toPlainText()
        print(mail,password)
        self.driver = webdriver.Chrome()
        self.driver.get(world)
        emailxpath = "//input[@name='name']"  # Replace with your desired XPath
        passwordxpath = "//input[@name='password']"
        loginbuttonxpath= "//button[@type='submit']"
        wait = WebDriverWait(self.driver, 10)
        
        element = wait.until(EC.visibility_of_element_located((By.XPATH, emailxpath)))
        element.send_keys(mail)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, passwordxpath)))
        element.send_keys(password)
        self.loggedin = True
        self.driverloop()

    def driverloop(self ):
        while(self.loggedin):
            sleep(2)
    def login(self,mail,passwd):
        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Account name or e-mail address :"))
        self.label_2.setText(_translate("MainWindow", "Password :"))
        self.buttonlogin.setText(_translate("MainWindow", "login"))
        self.checkBox.setText(_translate("MainWindow", "remember me"))
        self.menufile.setTitle(_translate("MainWindow", "file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
