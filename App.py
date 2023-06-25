import travlord as trav
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton,QMainWindow
from time import sleep
import threading 


class AppController:

    def __init__(self,ui,mainWindow):    
        self.ui=ui
        #ui.setupUi(mainWindow)
        ui.buttonlogin.clicked.connect(lambda: self.loginclicked(ui))
        self.ui.labelEmail.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.labelPassword.setStyleSheet("color: rgb(255, 255, 255);")
    def logindriver(mail, password,world):
        driver = webdriver.Chrome()
        driver.get(world)
        emailxpath = "//input[@name='name']"  # Replace with your desired XPath
        passwordxpath = "//input[@name='password']"
        loginbuttonxpath= "//button[@type='submit']"
        wait = WebDriverWait(driver, 10)
        
        element = wait.until(EC.visibility_of_element_located((By.XPATH, emailxpath)))
        element.send_keys(mail)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, passwordxpath)))
        element.send_keys(password)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, loginbuttonxpath)))
        element.click()
        sleep(20)
    def loginclicked(self,ui_MainWindow):
        mail = ui_MainWindow.inputemail.toPlainText()
        password = ui_MainWindow.inputpassword.text()
        
        world = ui_MainWindow.world.toPlainText()
        print(mail,password)
        thread = threading.Thread(target=self.logindriver, args=(mail, password,world))
        thread.start()
    def connectMethodsToUI():
        pass

class myMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.labelEmailInitWidth=230
        self.labelEmailInitHeight=110
        self.labelPassword=
        self.button = QPushButton("Move Me", self)
        self.button.setGeometry(10, 10, 100, 100)
        self.setupUi(self)

    def resizeEvent(self, event):
        # Get the new size of the window
        new_size = event.size()
     
        # Calculate the new position for the button
        new_x = new_size.width() - self.button.width() - 10
        new_y = new_size.height() - self.button.height() - 10

        # Set the new position for the button
        #self.inputemail.move(new_size.width() - self.inputemail.width() - 230,new_size.height() - self.inputemail.height() -170 )
        self.inputemail.move(int(new_size.width()/2),int(new_size.height()/2))        
        #self.labelEmail.move(new_size.width() - self.labelEmail.width() - self.labelEmailInitWidth,new_size.height() - self.inputemail.height() -self.labelEmailInitHeight )
        self.labelEmail.move(int(new_size.width()/2),int(new_size.height()/2))  
        self.button.move(new_x, new_y)
    
        pass
    def setupUi(self, TravLegendsWarLord):
        TravLegendsWarLord.setObjectName("TravLegendsWarLord")
        TravLegendsWarLord.setEnabled(True)
        TravLegendsWarLord.resize(800, 800)
        TravLegendsWarLord.setMinimumSize(QtCore.QSize(500, 500))
        TravLegendsWarLord.setWindowOpacity(100.0)
        TravLegendsWarLord.setStyleSheet("background-image: url(login.png);")
        self.centralwidget = QtWidgets.QWidget(TravLegendsWarLord)
        self.centralwidget.setObjectName("centralwidget")
        self.labelEmail = QtWidgets.QLabel(self.centralwidget)
        self.labelEmail.setGeometry(QtCore.QRect(self.labelEmailInitWidth, self.labelEmailInitHeight, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelEmail.setFont(font)
        self.labelEmail.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelEmail.setFrameShape(QtWidgets.QFrame.Box)
        self.labelEmail.setFrameShadow(QtWidgets.QFrame.Raised)
        self.labelEmail.setObjectName("labelEmail")
        self.labelPassword = QtWidgets.QLabel(self.centralwidget)
        self.labelPassword.setGeometry(QtCore.QRect(230, 210, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelPassword.setFont(font)
        self.labelPassword.setFrameShape(QtWidgets.QFrame.Box)
        self.labelPassword.setFrameShadow(QtWidgets.QFrame.Raised)
        self.labelPassword.setObjectName("labelPassword")
        self.inputemail = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputemail.setGeometry(QtCore.QRect(230, 170, 191, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputemail.sizePolicy().hasHeightForWidth())
        self.inputemail.setSizePolicy(sizePolicy)
        self.inputemail.setSizeIncrement(QtCore.QSize(10, 10))
        self.inputemail.setLineWidth(2)
        self.inputemail.setObjectName("inputemail")
        self.inputpassword = QtWidgets.QLineEdit(self.centralwidget)
        self.inputpassword.setGeometry(QtCore.QRect(230, 260, 191, 31))
        self.inputpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputpassword.setObjectName("inputpassword")
        self.buttonlogin = QtWidgets.QPushButton(self.centralwidget)
        self.buttonlogin.setGeometry(QtCore.QRect(420, 300, 75, 23))
        self.buttonlogin.setObjectName("buttonlogin")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(250, 320, 91, 17))
        self.checkBox.setObjectName("checkBox")
        self.world = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.world.setGeometry(QtCore.QRect(120, 370, 491, 31))
        self.world.setObjectName("world")
        TravLegendsWarLord.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TravLegendsWarLord)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 21))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        TravLegendsWarLord.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TravLegendsWarLord)
        self.statusbar.setObjectName("statusbar")
        TravLegendsWarLord.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menufile.menuAction())

        self.retranslateUi(TravLegendsWarLord)
        QtCore.QMetaObject.connectSlotsByName(TravLegendsWarLord)

    def retranslateUi(self, TravLegendsWarLord):
        _translate = QtCore.QCoreApplication.translate
        TravLegendsWarLord.setWindowTitle(_translate("TravLegendsWarLord", "MainWindow"))
        self.labelEmail.setText(_translate("TravLegendsWarLord", "Account name or e-mail address :"))
        self.labelPassword.setText(_translate("TravLegendsWarLord", "Password :"))
        self.buttonlogin.setText(_translate("TravLegendsWarLord", "login"))
        self.checkBox.setText(_translate("TravLegendsWarLord", "remember me"))
        self.menufile.setTitle(_translate("TravLegendsWarLord", "file"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = myMainWindow()
    #ui = trav.Ui_TravLegendsWarLord()
    #controller = AppController(ui,mainWindow)
    mainWindow.show()
    
    sys.exit(app.exec_())