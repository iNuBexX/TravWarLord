import travlord as trav
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from time import sleep

import threading 


class AppController:

    def __init__(self,mainWindow):   
        self.isLoggedIn=False
        #self.ui=ui
        #ui.setupUi(mainWindow)
        self.mainWindow = mainWindow
        self.resourcesfield3 = loginWindow()
        mainWindow.buttonlogin.clicked.connect(lambda: self.loginclicked(mainWindow))
        self.loadLoginCreds()
        #self.ui.labelEmail.setStyleSheet("color: rgb(255, 255, 255);")
        #self.ui.labelPassword.setStyleSheet("color: rgb(255, 255, 255);")
    def thread__logindriver(self,mail, password,world):
        print("login thread")
        driver = webdriver.Chrome()
        driver.get(world)
        emailxpath = "//input[@name='name']"  # Replace with your desired XPath
        passwordxpath = "//input[@name='password']"
        loginbuttonxpath= "//button[@type='submit']"
        resourcesFieldType = "//div[@id='resourceFieldContainer']"
        #TODO fix
        # resources gonna go play cs  figure it out later
        
        wait = WebDriverWait(driver, 10)
        
        element = wait.until(EC.visibility_of_element_located((By.XPATH, emailxpath)))
        element.send_keys(mail)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, passwordxpath)))
        element.send_keys(password)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, loginbuttonxpath)))
        element.click()
        element = wait.until(EC.visibility_of_element_located((By.XPATH, resourcesFieldType)))
        string = ""
        string += element.get_attribute("class")
        print(string)
        if string.find("resourceField3")!= -1:
            self.isLoggedIn=True



        return 
        sleep(20)
    def loginclicked(self,ui_MainWindow):
        mail = ui_MainWindow.inputEmail.toPlainText()
        password = ui_MainWindow.inputPassword.text()
        world = ui_MainWindow.world.toPlainText()
        print(mail,password)
        thread__login = threading.Thread(target=self.thread__logindriver, args=(mail, password,world))
        #self.isLoggedIn = 
        thread__login.start()
        thread__login.join()
        if self.isLoggedIn:
            new_widget = QWidget()
            layout = QVBoxLayout()
            label = QLabel()
            pixmap = QPixmap("src/img/bgResources")
            scaled_pixmap = pixmap.scaled(self.mainWindow.size(), aspectRatioMode=Qt.KeepAspectRatioByExpanding)
            label.setPixmap(scaled_pixmap)
            label.setAlignment(Qt.AlignCenter)
            

            layout.addWidget(label)
            centralWidget = self.mainWindow.centralWidget()

            # Replace the existing layout with the new layout
            

            #self.mainWindow.setLayout(layout)
            # Create new content (e.g., different widgets) for the new widget
            #self.mainWindow.setStyleSheet("background-image: url(src/img/bgResources);background-size: cover;")  
            #new_label = QLabel("New Content")
            #new_layout.addWidget(new_label)
            #self.mainWindow.setCentralWidget(new_widget)
            centralWidget.setLayout(layout)
    #TODO change into an .env file and add it to git ignore
    def loadLoginCreds(self):
        self.mainWindow.inputEmail.setPlainText("kelkor664455@gmail.com")
        self.mainWindow.inputPassword.setText("123456789")
        self.mainWindow.world.setPlainText("https://nordics.x3.nordics.travian.com/")


    def connectMethodsToUI():
        pass

class loginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #MainWindow
        self.mainWindowInitsize = {'x':800,'y':800}
        #Email label
        self.labelEmailInitPos = {'x':200,'y':200}
        self.labelEmailInitSize = {'x':251,'y':41}
        #Email input
        self.inputEmailInitPos = {'x':200,'y':280}
        self.inputEmailInitSize = {'x':191,'y':41}
        #Password Label
        self.labelPasswordInitPos = {'x':170,'y':350} 
        self.labelPasswordInitSize = {'x':91,'y':41}
        #Password Input
        self.inputPasswordInitPos = {'x':260,'y':430}
        self.inputPasswordInitSize = {'x':191,'y':41}
        #Login Button
        self.buttonLoginInitPos = {'x':420,'y':500}
        self.buttonLoginInitSize = {'x':75,'y':23}
        #World choice
        self.inputWorldInitPos = {'x':100,'y':615}
        self.inputWorldInitSize = {'x':490,'y':35}
        #Remember me ?
        self.checkBoxRememberMeInitPos = {'x':300,'y':503}
        self.checkBoxRememberMeInitSize = {'x':90,'y':20}

        self.labelWorld = {'x':170,'y':590} 

        self.setupUi(self)

    def resizeEvent(self, event):
        pass        
        # Get the new size of the window
        new_size = event.size()

        #log in widget
        #################################################################################################### 
        resizedinputmail = self.findChild(QtWidgets.QPlainTextEdit, "inputemail")
        if resizedinputmail :
            self.inputEmail.move(int(new_size.width()/2-self.inputEmailInitSize['x']/2),int(new_size.height()*(self.inputEmailInitPos['y']/self.mainWindowInitsize['y'])))        
        resizedlabelEmail = self.findChild(QLabel, "labelemail")
        if  resizedlabelEmail:
            self.labelEmail.move(int(new_size.width()/2-self.labelEmailInitSize['x']/2),int(new_size.height()*(self.labelEmailInitPos['y']/self.mainWindowInitsize['y']))) 
        resizedinputPassword = self.findChild(QtWidgets.QLineEdit, "inputpassword")
        if resizedinputPassword:
            self.inputPassword.move(int(new_size.width()/2-self.inputPasswordInitSize['x']/2),int(new_size.height()*(self.inputPasswordInitPos['y']/self.mainWindowInitsize['y']))) 
        resizedlabelPassword = self.findChild(QLabel, "labelpassword")
        if resizedlabelPassword:
            self.labelPassword.move(int(new_size.width()/2-self.labelPasswordInitSize['x']/2),int(new_size.height()*(self.labelPasswordInitPos['y']/self.mainWindowInitsize['y']))) 
        resizedbuttonlogin = self.findChild(QtWidgets.QPushButton, "buttonlogin")
        if resizedbuttonlogin:
            self.buttonlogin.move(int(new_size.width()*(self.buttonLoginInitPos['x']/self.mainWindowInitsize['x'])),int(new_size.height()*(self.buttonLoginInitPos['y']/self.mainWindowInitsize['y']))) 
        resizedcheckBox = self.findChild(QtWidgets.QCheckBox, "checkBox")
        if resizedcheckBox:
            self.checkBox.move(int(new_size.width()/2-self.checkBoxRememberMeInitSize['x']),int(new_size.height()*(self.checkBoxRememberMeInitPos['y']/self.mainWindowInitsize['y']))) 
        resizedworld = self.findChild(QtWidgets.QPlainTextEdit, "world")
        if resizedworld:
            self.world.move(int(new_size.width()/2-self.inputWorldInitSize['x']/2),int(new_size.height()*(self.inputWorldInitPos['y']/self.mainWindowInitsize['y']))) 
        
    
        pass
    def setupUi(self, TravLegendsWarLord):
        TravLegendsWarLord.setObjectName("TravLegendsWarLord")
        TravLegendsWarLord.setEnabled(True)
        TravLegendsWarLord.resize(self.mainWindowInitsize['y'], self.mainWindowInitsize['x'])
        TravLegendsWarLord.setMinimumSize(QtCore.QSize(500, 500))
        TravLegendsWarLord.setWindowOpacity(100.0)
        TravLegendsWarLord.setStyleSheet("background-image: url(src/img/login.png);")
        self.centralwidget = QtWidgets.QWidget(TravLegendsWarLord)
        self.centralwidget.setObjectName("centralwidget")


        #Login widget elements definition
        ####################################################################################################  
        #################################################################################################### 
     

        #email label
        self.labelEmail = QtWidgets.QLabel(self.centralwidget)
        #email input
        self.inputEmail = QtWidgets.QPlainTextEdit(self.centralwidget)
        
        #password label
        self.labelPassword = QtWidgets.QLabel(self.centralwidget)
        #password input
        self.inputPassword = QtWidgets.QLineEdit(self.centralwidget)
        
        #login button
        self.buttonlogin = QtWidgets.QPushButton(self.centralwidget)
        
        #login remember me checkbox
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)

        #world input
        self.world = QtWidgets.QPlainTextEdit(self.centralwidget)

        #menubar 
        self.menubar = QtWidgets.QMenuBar(TravLegendsWarLord)

        #statusbar
        self.statusbar = QtWidgets.QStatusBar(TravLegendsWarLord)

        #Elements innitial naming setup 
        ####################################################################################################  
        ####################################################################################################  
        self.inputEmail.setObjectName("inputemail")
        self.inputPassword.setObjectName("inputpassword")
        self.labelEmail.setObjectName("labelemail")
        self.labelPassword.setObjectName("labelpassword")
        self.buttonlogin.setObjectName("buttonlogin")
        self.checkBox.setObjectName("checkBox")
        self.world.setObjectName("world")
        self.menubar.setObjectName("menubar")
        self.statusbar.setObjectName("statusbar")

        #Elements innitial positioning 
        ####################################################################################################  
        #################################################################################################### 
        
        
        #Elements innitial geometry setup 
        ####################################################################################################  
        ####################################################################################################  

        #email input
        self.inputEmail.setGeometry(QtCore.QRect(self.inputEmailInitPos['x'], self.inputEmailInitPos['y'], 191, 31))
        
        #password input
        self.inputPassword.setGeometry(QtCore.QRect(230, 260, 191, 31))
        self.inputEmail.setSizeIncrement(QtCore.QSize(10, 10))
        self.inputEmail.setLineWidth(2)

        self.inputPassword.setEchoMode(QtWidgets.QLineEdit.Password)



        self.world.setGeometry(QtCore.QRect(120, 370, 491, 31))
        
        TravLegendsWarLord.setCentralWidget(self.centralwidget)
        
        self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 21))
        
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        TravLegendsWarLord.setMenuBar(self.menubar)
        
        
        TravLegendsWarLord.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menufile.menuAction())
        self.labelEmail=self.labelstyleup(self.labelEmail,"labelEmail")
        self.labelPassword=self.labelstyleup(self.labelPassword,"labelPassword")
        self.inputPassword.setStyleSheet("color: rgb(255, 255, 255);")
        self.inputEmail.setStyleSheet("color: rgb(255, 255, 255);")
        self.buttonlogin.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.world.setStyleSheet("color: rgb(255, 255, 255);")
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
    def labelstyleup(self,widget,name):
        widget = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        widget.setFont(font)
        widget.setStyleSheet("color: rgb(255, 255, 255);")
        widget.setFrameShape(QtWidgets.QFrame.Box)
        widget.setFrameShadow(QtWidgets.QFrame.Raised)
        widget.setObjectName(name)
        return widget

class resourcesWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        pass

    def setupUi(self,resourceswindow):
        resourceswindow.setObjectName("TravLegendsWarLord")
        resourceswindow.setEnabled(True)
        resourceswindow.resize(self.mainWindowInitsize['y'], self.mainWindowInitsize['x'])
        resourceswindow.setMinimumSize(QtCore.QSize(500, 500))
        resourceswindow.setWindowOpacity(100.0)
        resourceswindow.setStyleSheet("background-image: url(src/img/bgResources);")  
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = loginWindow()
    controller = AppController(mainWindow)
    mainWindow.show()
    
    sys.exit(app.exec_())
