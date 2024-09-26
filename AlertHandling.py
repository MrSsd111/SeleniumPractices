import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.execute_script("window.scrollTo(0,300)")
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("SHUBHAM")
driver.find_element(By.CSS_SELECTOR, "input[id='alertbtn']").click()
time.sleep(2)
alert = driver.switch_to.alert
Atext = alert.text
print(alert.text)
assert "SHUBHAM" in Atext
alert.accept()
driver.close()
