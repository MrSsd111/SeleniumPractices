import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(7)
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.find_element(By.XPATH, "//a[@target = '_blank'][text() = 'Click Here']").click()

handle = driver.window_handles
driver.switch_to.window(handle[1])
print(driver.find_element(By.XPATH, "//h3").text)

assert  driver.find_element(By.XPATH, "//h3").text == "New Window"
time.sleep(2)
