import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


#co = webdriver.ChromeOptions()
#co.add_argument("headless")

driver = webdriver.Chrome()
driver.implicitly_wait(7)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
time.sleep(2)

handle = driver.window_handles
driver.switch_to.window(handle[1])
mailID = driver.find_element(By.LINK_TEXT, "mentor@rahulshettyacademy.com").text
print(mailID)

driver.switch_to.window(handle[0])
driver.find_element(By.ID, "username").send_keys(mailID)
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.XPATH, "//*[@id='login-form']/div[4]/div/label[2]/span[2]").click()
time.sleep(2)
driver.find_element(By.ID, "okayBtn").click()
time.sleep(2)
select= Select(driver.find_element(By.XPATH, "//select[@class = 'form-control']"))
select.select_by_value("consult")
driver.find_element(By.ID, "terms").click()
driver.find_element(By.ID, "signInBtn").click()
time.sleep(2)
print(driver.find_element(By.XPATH, "//div[@class = 'alert alert-danger col-md-12']").text)
time.sleep(2)
