import time

from selenium import webdriver
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.execute_script("window.scrollTo(0,500)")
driver.find_element(By.NAME, "email").send_keys("ssd@gmial.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123444")
driver.find_element(By.ID, "exampleCheck1").click()
time.sleep(2)

#XPATH --> //tagname[@attribute = 'value']  ---->> //input[@value = 'Submit']
driver.find_element(By.XPATH,"//input[@value = 'Submit']").click()
time.sleep(2)
#CSSSelector --> tagname[attribute = 'value']    ----> input[name = 'name']
driver.find_element(By.CSS_SELECTOR, "input[name = 'name']").send_keys("ssdef")

m = driver.find_element(By.CSS_SELECTOR, "div[class= 'alert alert-success alert-dismissible']").text
print(m)

assert "ucgfgcess" in m