import time

from selenium import webdriver

#HERE IS THE PROCESS HOW ONE CAN USE CHROMEOPTIONS IN SELENIUM
chromeop = webdriver.ChromeOptions()
chromeop.add_argument("--start-maximized") #THESE ARE THE METHODS TO ADD ARGUMENT TO THE CHROMEOPTIONS
chromeop.add_argument("headless")   #YOU CAN ACCESS BROWSER IN HEADLESS MODE
chromeop.add_argument("--ignore-certificate-errors")


# YOU HAVE TO ADD CHROMEOPTIONS OBJECT HERE
driver = webdriver.Chrome(options= chromeop)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
print("sucessfully loaded")
time.sleep(3)