import time
from argparse import Action

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.execute_script("window.scrollTo(0,1000)")
driver.switch_to.frame("courses-iframe")
driver.execute_script("window.scrollTo(0,200)")

driver.find_element(By.XPATH,"//a[@class = 'dropdown-toggle']").click()
driver.find_element(By.XPATH,"//a[text() = 'Contact'][1]").click()
driver.find_element(By.ID, "username").send_keys("shubham")
driver.find_element(By.ID, "mobileno").send_keys("9145764904")
driver.find_element(By.ID, "country").send_keys("India")
driver.find_element(By.ID, "email").send_keys("ssg@gmail.com")
select = Select(driver.find_element(By.ID, "subject"))
select.select_by_value("Online Courses")
driver.find_element(By.ID, "message").send_keys("Want to enquire about the selenium course")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.element_to_be_clickable(driver.find_element(By.XPATH,"//button[@type = 'submit']")))
driver.find_element(By.XPATH,"//button[@type = 'submit']").click()

print(driver.find_element(By.TAG_NAME, "p").text)
time.sleep(2)
driver.find_element(By.XPATH, "//button[@type= 'button'][text() = 'Close']").click()
driver.switch_to.default_content()


radio = driver.find_element(By.NAME,"radioButton")
radio.click()
assert radio.is_selected()
time.sleep(3)
