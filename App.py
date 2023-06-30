import resourceswindow as Rwindow
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QWidget, QGridLayout, QLabel,QPushButton,QSpacerItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from time import sleep

import threading 

from PyQt5.QtCore import QObject, pyqtSignal

class ResourcesDataObject(QObject):
    
    lumber_signal = pyqtSignal(str)
    clay_signal = pyqtSignal(str)
    iron_signal = pyqtSignal(str)
    crops_signal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self._lumber = ""
        self._clay= ""
        self._iron= ""
        self._crops= ""

    @property
    def lumber(self):
        return self._lumber
    @property
    def iron(self):
        return self._iron
    @property
    def crops(self):
        return self._crops
    @property
    def clay(self):
        return self._clay
    
    @lumber.setter
    def lumber(self, value):
        self._lumber = value
        self.lumber_signal.emit(value)
    @clay.setter
    def clay(self, value):
        self._clay = value
        self.clay_signal.emit(value)
    @iron.setter
    def iron(self, value):
        self._iron = value
        self.iron_signal.emit(value)
    @crops.setter
    def crops(self, value):
        self._crops = value
        self.crops_signal.emit(value)

class AppController:

    def __init__(self,mainWindow):   
        #TODO this feels like it doesn't belong here 
        self.lumberStrogeLocator ="//div[@id='l1']"
        self.clayStorageLocator ="//div[@id='l2']"
        self.ironStorageLocator ="//div[@id='l3']"
        self.cropsStorageLocator ="//div[@id='l4']"
        self.isLoggedIn=False
        self.driver = None
        self.wait = None
        self.resourcesWindow = None
        #self.ui=ui
        #ui.setupUi(mainWindow)
        self.mainWindow = mainWindow
        mainWindow.buttonlogin.clicked.connect(lambda: self.loginclicked(mainWindow))
        self.loadLoginCreds()
        self.resources_data_object = ResourcesDataObject()
        
        #self.ui.labelEmail.setStyleSheet("color: rgb(255, 255, 255);")
        #self.ui.labelPassword.setStyleSheet("color: rgb(255, 255, 255);")
    def thread__loginDriver(self,mail, password,world):
        print("login thread")
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(world)
        emailxpath = "//input[@name='name']"  # Replace with your desired XPath
        passwordxpath = "//input[@name='password']"
        loginbuttonxpath= "//button[@type='submit']"
        resourcesFieldType = "//div[@id='resourceFieldContainer']"
        
        #TODO fix
        # resources gonna go play cs  figure it out later
        
        
        
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, emailxpath)))
        element.send_keys(mail)
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, passwordxpath)))
        element.send_keys(password)
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, loginbuttonxpath)))
        element.click()
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, resourcesFieldType)))
        string = ""
        string += element.get_attribute("class")
        print(string)
        if string.find("resourceField3")!= -1:
            self.isLoggedIn = True
            

    def thread__getResourcesDriver(self):
        while(self.isLoggedIn): 
            self.resources_data_object.lumber = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.lumberStrogeLocator))).text
            self.resources_data_object.clay = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.clayStorageLocator))).text
            self.resources_data_object.iron = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.ironStorageLocator))).text
            self.resources_data_object.crops = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.cropsStorageLocator))).text
            sleep(3)
            #TODO set self data signal thingies here
    def GUI_updateLumber(self,amount):
        self.resourcesWindow.label_10.setText(amount)
    def GUI_updateClay(self,amount):
        self.resourcesWindow.label_11.setText(amount)
    def GUI_updateCrops(self,amount):
        self.resourcesWindow.label_12.setText(amount)
    def GUI_updateIron(self,amount):
        self.resourcesWindow.label_13.setText(amount)

    def loginclicked(self,ui_MainWindow):
        mail = ui_MainWindow.inputEmail.toPlainText()
        password = ui_MainWindow.inputPassword.text()
        world = ui_MainWindow.world.toPlainText()
        print(mail,password)
        thread__login = threading.Thread(target=self.thread__loginDriver, args=(mail, password,world))
        #self.isLoggedIn = 
        thread__login.start()
        thread__login.join()
        if(self.isLoggedIn == True):
            self.resourcesWindow = Rwindow.Ui_MainWindow()
            self.resourcesWindow .setupUi(self.mainWindow)
            self.resources_data_object.lumber_signal.connect(self.GUI_updateLumber)
            self.resources_data_object.clay_signal.connect(self.GUI_updateClay)
            self.resources_data_object.iron_signal.connect(self.GUI_updateIron)
            self.resources_data_object.crops_signal.connect(self.GUI_updateCrops)
            thread__getResources = threading.Thread(target=self.thread__getResourcesDriver)
            thread__getResources.start()


    #TODO change into an .env file and add it to git ignore
    def loadLoginCreds(self):
        self.mainWindow.inputEmail.setPlainText("kelkor664455@gmail.com")
        self.mainWindow.inputPassword.setText("123456789")
        self.mainWindow.world.setPlainText("https://ts8.x1.arabics.travian.com/")


    def connectMethodsToUI():
        pass

#class resourcesWindow:
  #  def __init__(self,maindWindow):
  #      self.mainWindow = maindWindow
  #      self.setupUi()
        #define elements positions  and sizes  here
   #     pass
   # def setupUi(self):
      #  self.mainWindow.setStyleSheet("QMainWindow { padding 0px;background-color:  rgb(65, 99, 46); }")
      #  resourcesLayout = QGridLayout()
      #  label = QLabel()
      #  pixmap = QPixmap("src/img/bgResources")
      #  scaled_pixmap = pixmap.scaled(self.mainWindow.size(), aspectRatioMode=Qt.KeepAspectRatioByExpanding)
      #  label.setPixmap(scaled_pixmap)
      #  label.setAlignment(Qt.AlignCenter)
      #  button1 = QPushButton('Button 1')
     #   button2 = QPushButton('Button 2')
      #  button3 = QPushButton('Button 3')

        # Add the buttons to the grid layout
         # button1 at row 0, column 0
        #resourcesLayout.addWidget(button2, 0, 1)  # button2 at row 0, column 1
        #resourcesLayout.addWidget(button3, 1, 0, 1, 2)  # button3 spans 1 row and 2 columns, starting at row 1, column 0
       

    #    resourcesLayout.addWidget(label,0, 0)
        #resourcesLayout.addWidget(button1, 0, 0,0.005,0.05)
      #  spacer = QSpacerItem(20, 20)  # Create a spacer item with a fixed size
  #      resourcesLayout.addItem(spacer, 0, 0)  # Add the spacer to a specific cell
   #     self.mainWindow.centralWidget().setLayout(resourcesLayout)


 #       pass

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #MainWindow
        self.mainWindowInitsize = {'x':800,'y':800}
        
        #this does not belong to the main winsow
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



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = mainWindow()
    controller = AppController(mainWindow)
    mainWindow.show()
    
    sys.exit(app.exec_())
