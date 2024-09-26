import time
from itertools import count

from select import select
from selenium import webdriver
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#driver = webdriver.Chrome()
#driver.get("https://rahulshettyacademy.com/angularpractice/")
#driver.maximize_window()
#driver.execute_script("window.scrollTo(0,500)")
###### STATIC DROPDOWN(WHICH HAS FIXED OPTION IN IT) CAN BE HANDLED WITH SELECT CLASS AS FOLLOWS ######

#select = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
#select.select_by_index(0)
#time.sleep(2)
#select.select_by_visible_text("Female")
#time.sleep(2)
#driver.close()

######### FOR AUTOSUGGESTIVE OR DYNAMIC DROPDOWN WE CAN USE FOLLOWING METHOD #######
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.XPATH, "//li[@class = 'ui-menu-item']/a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        print("INDIA is selected")
        break


######### FOR GETIING TEXT WHICH IS DYNAMICALLY ADDED USING SCRIPT WE USE FOLLOWING GET ATTRIBUTE METHOD######
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"


time.sleep(2)
driver.close()
