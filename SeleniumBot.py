from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://ttq.x2.arabics.travian.com/")
emailxpath = "//input[@name='name']"  # Replace with your desired XPath
passwordxpath = "//input[@name='password']"

wait = WebDriverWait(driver, 10)

element = wait.until(EC.visibility_of_element_located((By.XPATH, emailxpath)))
element.send_keys("kelkor664455@gmail.com")
element = wait.until(EC.visibility_of_element_located((By.XPATH, passwordxpath)))
element.send_keys("123456789")
