import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.ID,"autocomplete").send_keys("Ind")
country = driver.find_elements(By.XPATH, "//li[@class = 'ui-menu-item']")

for c in country:
    if c.text == "India":
        c.click()
        break


print(driver.find_element(By.ID, "autocomplete").get_attribute("value"))