import time

from selenium import webdriver

driver = webdriver.Edge()


# #service keyword is used to invoke browser using chromedriver path when ur using VPN
#service_obj = Service("CHROME DRIVER PATH")
#driver = webdriver.Chrome(service = service_obj)
driver.get("https://www.rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(3)
