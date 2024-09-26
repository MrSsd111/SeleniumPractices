import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.maximize_window()
driver.implicitly_wait(5)
driver.execute_script("window.scrollTo(0,1200)")

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
time.sleep(2)
#action.context_click(driver.find_element(By.XPATH, "//div[@class = 'mouse-hover-content']/a[1]")).perform()
driver.find_element(By.XPATH, "//div[@class = 'mouse-hover-content']/a[2]").click()
time.sleep(2)