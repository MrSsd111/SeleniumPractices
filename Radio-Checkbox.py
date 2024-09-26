import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice")
list = driver.find_elements(By.XPATH, "//input[@type ='checkbox']")
print("CHECKBOX = ", len(list))

for checkbox in list:
    e = checkbox.get_attribute("value")
    if e == "option2":
        checkbox.click()
    # WE USE ASSERTION TO CHECK WHETHER CHECKBOX IS SELECTED OR NOT
        assert checkbox.is_selected()
        break

radio = driver.find_elements(By.CSS_SELECTOR,"input[type = 'radio']")
print("RADIO = ", len(radio))

for option in radio:
    if option.get_attribute("value") == "radio2":
        option.click()
        assert option.is_selected()

time.sleep(2)
driver.execute_script("window.scrollTo(0,500)")
time.sleep(2)
assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()

assert not driver.find_element(By.ID,"displayed-text").is_displayed()

time.sleep(2)
driver.close()