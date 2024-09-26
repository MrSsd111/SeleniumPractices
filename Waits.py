import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
time.sleep(2)


list1 = []
elist = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg' ,'Strawberry - 1/4 Kg']





berry = driver.find_elements(By.XPATH, "//div[@class= 'products']/div")
print(len(berry))
assert  len(berry) > 0

for result in berry:
    driver.find_element(By.XPATH,"//button[text() = 'ADD TO CART']").click()
    #list1.append(result.find_element(By.XPATH, "h4").text)

a1 = driver.find_elements(By.XPATH, "//h4[@class = 'product-name']")
for a in a1:
    list1.append(a.text)

print(list1)
assert list1 == elist


driver.find_element(By.XPATH,"//img[@src = 'https://rahulshettyacademy.com/seleniumPractise/images/bag.png']").click()
driver.find_element(By.XPATH, "//button[@type = 'button']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//input[@type = 'text']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[@class = 'promoBtn']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//span[@class = 'promoInfo']" )))
print(driver.find_element(By.XPATH, "//span[@class = 'promoInfo']").text)
prices = driver.find_elements(By.XPATH,"//td[5]/p[@class = 'amount']")

discount = float(driver.find_element(By.XPATH, "//span[@class = 'discountAmt']").text)


sum = 0
for price in prices:
    sum = sum + int(price.text)

print(sum)

total = int(driver.find_element(By.XPATH,"//span[@class = 'totAmt']").text)
assert sum == total

assert total > discount
time.sleep(3)




