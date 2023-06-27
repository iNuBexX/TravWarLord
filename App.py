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
        #MainWindow
        self.mainWindowInitsize = {'y':800,'x':800}
        #Email label
        self.labelEmailInitPos = {'y':200,'x':200}
        self.labelEmailInitSize = {'y':251,'x':41}
        #Email input
        self.inputEmailInitPos = {'y':280,'x':200}
        self.inputEmailInitSize = {'y':191,'x':41}
        #Password Label
        self.labelPasswordInitPos = {'y':350,'x':170} 
        self.labelPasswordInitSize = {'y':251,'x':41}
        #Password Input
        self.inputPasswordInitPos = {'y':430,'x':260}
        self.inputPasswordInitSize = {'y':191,'x':41}
        #Login Button
        self.buttonLoginInitPos = {'y':500,'x':420}
        self.buttonLoginInitSize = {'y':23,'x':75}
        #World choice
        self.inputWorldInitPos = {'y':600,'x':100}
        self.inputWorldInitSize = {'y':35,'x':490}
        #Remember me ?
        self.checkBoxRememberMeInitPos = {'y':500,'x':300}
        self.checkBoxRememberMeInitSize = {'y':20,'x':90}



        self.setupUi(self)

    def resizeEvent(self, event):
        # Get the new size of the window
        new_size = event.size()
     
        # Calculate the new position for the button
        # Set the new position for the button
        #self.inputemail.move(new_size.width() - self.inputemail.width() - 230,new_size.height() - self.inputemail.height() -170 )
   
        self.inputemail.move(int(new_size.width()/2-self.inputEmailInitSize['y']/2),int(new_size.height()*(self.inputEmailInitPos['y']/self.mainWindowInitsize['y'])))        
        #self.labelEmail.move(new_size.width() - self.labelEmail.width() - self.labelEmailInitWidth,new_size.height() - self.inputemail.height() -self.labelEmailInitHeight )
        self.labelEmail.move(int(new_size.width()/2-self.labelEmailInitSize['y']/2),int(new_size.height()*(self.labelEmailInitPos['y']/self.mainWindowInitsize['y']))) 
       
        self.inputpassword.move(int(new_size.width()/2-self.inputPasswordInitSize['y']/2),int(new_size.height()*(self.inputPasswordInitPos['y']/self.mainWindowInitsize['y']))) 
       
        self.labelPassword.move(int(new_size.width()/2-self.labelPasswordInitSize['y']/2),int(new_size.height()*(self.labelPasswordInitPos['y']/self.mainWindowInitsize['y']))) 
       
        self.buttonlogin.move(int(new_size.width()*(self.buttonLoginInitPos['x']/self.mainWindowInitsize['x'])),int(new_size.height()*(self.buttonLoginInitPos['y']/self.mainWindowInitsize['y']))) 
       
        #self.checkBox.move(int(new_size.width()*(self.checkBoxRememberMeInitPos['x']/self.mainWindowInitsize['x'])),int(new_size.height()*(self.checkBoxRememberMeInitPos['y']/self.mainWindowInitsize['y']))) 
        self.checkBox.move(int(new_size.width()/2-self.checkBoxRememberMeInitSize['x']),int(new_size.height()*(self.checkBoxRememberMeInitPos['y']/self.mainWindowInitsize['y']))) 
       
        self.world.move(int(new_size.width()/2-self.inputWorldInitSize['x']/2),int(new_size.height()*(self.inputWorldInitPos['y']/self.mainWindowInitsize['y']))) 
       
        #print(self.labelEmailInitPos.ge)
        #self.button.move(new_x, new_y)
    
        pass
    def setupUi(self, TravLegendsWarLord):
        TravLegendsWarLord.setObjectName("TravLegendsWarLord")
        TravLegendsWarLord.setEnabled(True)
        TravLegendsWarLord.resize(self.mainWindowInitsize['y'], self.mainWindowInitsize['x'])
        TravLegendsWarLord.setMinimumSize(QtCore.QSize(500, 500))
        TravLegendsWarLord.setWindowOpacity(100.0)
        TravLegendsWarLord.setStyleSheet("background-image: url(login.png);")
        self.centralwidget = QtWidgets.QWidget(TravLegendsWarLord)
        self.centralwidget.setObjectName("centralwidget")
    
        self.labelPassword = QtWidgets.QLabel(self.centralwidget)
        #self.labelPassword.setGeometry(QtCore.QRect(230, 210, 251, 41))
        self.labelEmail = QtWidgets.QLabel(self.centralwidget)
        #self.labelEmail.setGeometry(QtCore.QRect(self.labelEmailInitSize['x'], self.labelEmailInitSize['y'], 251, 41))




        self.inputemail = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputemail.setGeometry(QtCore.QRect(self.inputEmailInitPos['y'], self.inputEmailInitPos['x'], 191, 31))


       
        self.inputemail.setSizeIncrement(QtCore.QSize(10, 10))
        self.inputemail.setLineWidth(2)
        self.inputemail.setObjectName("inputemail")
        self.inputpassword = QtWidgets.QLineEdit(self.centralwidget)
        self.inputpassword.setGeometry(QtCore.QRect(230, 260, 191, 31))
        self.inputpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputpassword.setObjectName("inputpassword")
        
        self.buttonlogin = QtWidgets.QPushButton(self.centralwidget)
        self.buttonlogin.setGeometry(QtCore.QRect(self.buttonLoginInitPos['x'],self.buttonLoginInitPos['y'], self.buttonLoginInitSize['x'], self.buttonLoginInitSize['y']))
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
        self.labelEmail=self.labelstyleup(self.labelEmail,"labelEmail")
        self.labelPassword=self.labelstyleup(self.labelPassword,"labelPassword")

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = myMainWindow()
    #ui = trav.Ui_TravLegendsWarLord()
    #controller = AppController(ui,mainWindow)
    mainWindow.show()
    
    sys.exit(app.exec_())