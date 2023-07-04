import resourceswindow as Rwindow
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel
from time import sleep
from datetime import datetime, timedelta
import time

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

class FieldsDataObject(QObject):
    field_signal1 = pyqtSignal(str,str)
    field_signal2 = pyqtSignal(str,str)
    field_signal3 = pyqtSignal(str,str)
    field_signal4 = pyqtSignal(str,str)
    field_signal5 = pyqtSignal(str,str)
    field_signal6 = pyqtSignal(str,str)
    field_signal7 = pyqtSignal(str,str)
    field_signal8= pyqtSignal(str,str)
    field_signal9 = pyqtSignal(str,str)
    field_signal10 = pyqtSignal(str,str)
    field_signal11 = pyqtSignal(str,str)
    field_signal12 = pyqtSignal(str,str)
    field_signal13 = pyqtSignal(str,str)
    field_signal14 = pyqtSignal(str,str)
    field_signal15 = pyqtSignal(str,str)
    field_signal16 = pyqtSignal(str,str)
    field_signal17 = pyqtSignal(str,str)
    field_signal18 = pyqtSignal(str,str)

  
    def __init__(self):
        super().__init__()
        for i in range(1,19):
            setattr(self, f"_field{i}","")
    @property
    def field(self,i):
        return getattr(self, f"_field{i}")

    def setfield(self, value,i):
        setattr(self, f"_field{i}",value) 
        #self._field = value
        getattr(self, f"field_signal{i}").emit(value,f"{i}")
    
    

class AppController:

    def __init__(self,mainWindow):   
        #TODO this feels like it doesn't belong here 
        self.resourcesViewLocator = "//a[contains(@class,'village resourceView')]"
        self.resources_data_object = ResourcesDataObject()
        self.fields_data_object = FieldsDataObject()
        #TODO fix this (changes with world)
        self.lumberStrogeLocator ="//div[@id='l1']"
        self.clayStorageLocator ="//div[@id='l2']"
        self.ironStorageLocator ="//div[@id='l3']"
        self.cropsStorageLocator ="//div[@id='l4']"
        self.isLoggedIn= False
        self.driver = None
        self.wait = None
        self.resourcesWindow = None
        self.currentTab = "resources"
        self.mainWindow = mainWindow
        self.thread__buildingList= None
        self.thread__updateField= None
        mainWindow.buttonlogin.clicked.connect(lambda: self.loginclicked(mainWindow))
        self.loadLoginCreds()
        
        
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
            if(self.currentTab=="resources"):
                self.resources_data_object.lumber = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.lumberStrogeLocator))).text
                self.resources_data_object.clay = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.clayStorageLocator))).text
                self.resources_data_object.iron = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.ironStorageLocator))).text
                self.resources_data_object.crops = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.cropsStorageLocator))).text
                sleep(3)
            #TODO set self data signal thingies here
    def thread_getFieldsDriver(self):
        for i in range(1,19):
            fieldlocator=f"//a[@href='/build.php?id={i}']"
            self.fields_data_object.setfield(self.wait.until(EC.visibility_of_element_located((By.XPATH, fieldlocator))).text,i)

            #self.resources_data_object = self.wait.until(EC.visibility_of_element_located((By.XPATH, fieldlocator))).text
            #setattr(self.fields_data_object, f"field{i}",self.wait.until(EC.visibility_of_element_located((By.XPATH, fieldlocator))).text)
    def thread_getBuildingListDriver(self):
        try:
            timer ="//div[@class='buildingList']//ul//span[@class='timer']"
            print(timer)
            time_str = self.wait.until(EC.visibility_of_element_located((By.XPATH, timer))).text
            print(time_str)
            initial_time = datetime.strptime(time_str, "%H:%M:%S")
            zero_time = datetime.strptime("0:00:00", "%H:%M:%S")
            item = QtWidgets.QTableWidgetItem()
            self.resourcesWindow.tableWidget.setItem(0, 1, item)
            
            while initial_time > zero_time:
                
                # Format and print the current time

                
                
                # Decrement the time by 1 second
                initial_time -= timedelta(seconds=1)

                # Pause for 1 second before the next iteration
                time.sleep(1)
                self.resourcesWindow.tableWidget.item(0, 1).setText(initial_time.strftime("%H:%M:%S"))
                self.resourcesWindow.tableWidget.viewport().update()
                #print(initial_time.strftime("%H:%M:%S"))
             
        except:
            print("no buildings")


    def GUI_updateLumber(self,amount):
        self.resourcesWindow.label_10.setText(amount)
    def GUI_updateClay(self,amount):
        self.resourcesWindow.label_11.setText(amount)
    def GUI_updateCrops(self,amount):
        self.resourcesWindow.label_12.setText(amount)
    def GUI_updateIron(self,amount):
        self.resourcesWindow.label_13.setText(amount)
    def GUI_updateField(self,level,i):
        #setattr(self.resourcesWindow,f"fieldlabel{i}",amount)
        getattr(self.resourcesWindow,f"fieldlabel{i}").setText(f"{level}")
       
       # self.resourcesWindow.fieldlabel.setText(amount)
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
      
            for i in range(1,19):
                getattr(self.resourcesWindow,f"pushButton_fieldlabel{i}").clicked.connect(self.updateFieldDriver(f"{i}"))
            
            self.resources_data_object.lumber_signal.connect(self.GUI_updateLumber)
            self.resources_data_object.clay_signal.connect(self.GUI_updateClay)
            self.resources_data_object.iron_signal.connect(self.GUI_updateIron)
            self.resources_data_object.crops_signal.connect(self.GUI_updateCrops)
            for i in range(1,19):
                getattr(self.fields_data_object, f"field_signal{i}").connect(lambda level, fieldnumber: self.GUI_updateField(level,fieldnumber))
            #TODO use files for memory to load in queue

            self.resourcesWindow.tableWidget.setRowCount(1)
            
            thread__getResources = threading.Thread(target=self.thread__getResourcesDriver)
            thread__getResources.start()
            self.thread__updateField = threading.Thread(target=self.thread_getFieldsDriver)
            self.thread__updateField.start()
            """if(self.thread__buildingList):
                self.thread__buildingList.terminate()
                self.thread__buildingList = threading.Thread(target=self.thread_getBuildingListDriver)
                self.thread__buildingList.start()"""

    def Navigate_Resources(self):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.resourcesViewLocator)))
        element.click()
        if(self.thread__buildingList):
               self.thread__buildingList.terminate()
        thread_getBuildingList = threading.Thread(target=self.thread_getBuildingListDriver)
        thread_getBuildingList.start()

        thread_getFieldsDriver = threading.Thread(target=self.thread_getFieldsDriver)
        thread_getFieldsDriver.start()
    #TODO change into an .env file and add it to git ignore
    def loadLoginCreds(self):
        self.mainWindow.inputEmail.setPlainText("kelkor664455@gmail.com")
        self.mainWindow.inputPassword.setText("123456789")
        self.mainWindow.world.setPlainText("https://ts2.x1.international.travian.com/")

    def thread__updatFieldDriver(self,i):
        print(i)
        self.currentTab = "field"
        fieldlocator=f"//a[@href='/build.php?id={i}']"
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, fieldlocator)))
        element.click()
        buildbutton="//button[contains(@class,'green build')]"
        try:
            element = self.wait.until(EC.visibility_of_element_located((By.XPATH, buildbutton)))
            element.click()
        except:
            self.Navigate_Resources()
        self.currentTab = "resources"

    def updateFieldDriver(self,i):
        def closure():
            self.thread__updateField = threading.Thread(target=self.thread__updatFieldDriver,args=(i,)) 
            self.thread__updateField.start()
        return closure
    
    
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
