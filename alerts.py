import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/alert_accept.html")


button = driver.find_element_by_tag_name("button")
button.click()

confirm = driver.switch_to.alert
confirm.accept()

x = int(driver.find_element_by_id("input_value").text)
f = math.log(abs(12 * math.sin(x)), math.e)

answer = driver.find_element_by_id("answer")
answer.send_keys(str(f))

buttonSubmit = driver.find_element_by_tag_name("button")
buttonSubmit.click()

alert = driver.switch_to.alert
response = alert.text
print(response)



time.sleep(2)


driver.quit()
