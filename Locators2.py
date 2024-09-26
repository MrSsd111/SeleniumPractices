import time

from selenium import webdriver
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("ssd@123")
#WE CAN ADD LOCATORS VALUE IN CSS BY FOLLOWING METHOD (# FOR ID, .(DOT) FOR CLASS)
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("ssd@123")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").clear()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("ssd@123")
time.sleep(2)
driver.find_element(By.XPATH, "//button[text()= 'Save New Password']").click()
time.sleep(2)
driver.close()
print("password changed succefully")



