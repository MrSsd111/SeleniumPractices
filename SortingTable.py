import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.implicitly_wait(5)
driver.maximize_window()
driver.find_element(By.XPATH, "//span[text() = 'Veg/fruit name']").click()
driver.get_screenshot_as_file("screen.png")
time.sleep(2)
veggie = driver.find_elements(By.XPATH,"//tr/td[1]")
veggiel = []
for v in veggie:
    veggiel.append(v.text)

elist = veggiel.copy()
veggiel.sort()
assert elist == veggiel
time.sleep(2)
driver.close()
