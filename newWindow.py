import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


# Переключение на вкладку browser.switch_to.window(window_name) PS новое окно = ровная вкладка
# new_window = browser.window_handles[1]
# first_window = browser.window_handles[0]

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/redirect_accept.html")


button = driver.find_element_by_tag_name("button")
button.click()

new_window = driver.window_handles[1]
driver.switch_to.window(new_window)


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
