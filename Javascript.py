import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https:rahulshettyacademy.com/AutomationPractice/")
#EXECUTE SCRIPT MEANS DRIVER WILL EXECUTE THE JAVASCRIPT, YOU CAN ADD TYPES OF JS COMMANDS WITHIN BRACES
driver.execute_script("window.scrollTo(0,500)")

driver.get_screenshot_as_file("screen1.png")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
driver.get_screenshot_as_file("screen.png")
driver.execute_script("window.scrollTo(0, -1000)")
time.sleep(3)
driver.close()
