import travlord as trav
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep
import threading 


class App:

    def InitializeUI():
        
        pass

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
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = trav.Ui_TravLegendsWarLord()
    
    ui.setupUi(MainWindow)
    ui.buttonlogin.clicked.connect(lambda: App.loginclicked(ui))

    #app = App()
   
    
    MainWindow.show()
    
    sys.exit(app.exec_())