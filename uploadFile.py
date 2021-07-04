import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/file_input.html")

with open("test.txt", "w") as file:
    content = file.write("automationbypython")  # create test.txt file

fileLink = os.path.dirname(__file__) + r"\test.txt"

inputs = driver.find_elements_by_tag_name("input")
# inputs.pop(0).send_keys("Имя")
# inputs.pop(0).send_keys("Фамилия")
# inputs.pop(0).send_keys("мыло")
for i in inputs[0:3]:
    i.send_keys("test")

inputs[3].send_keys(fileLink)

button = driver.find_element_by_tag_name("button")
button.click()

alert = driver.switch_to.alert
alertText = alert.text
alert.accept()
print(alertText)

time.sleep(20)


driver.quit()
