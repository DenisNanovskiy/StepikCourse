from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/execute_script.html")

x = int(driver.find_element_by_id("input_value").text)
f = math.log(abs(12 * math.sin(x)), math.e)

answer = driver.find_element_by_id("answer")
answer.send_keys(str(f))

button = driver.find_element_by_tag_name("button")
driver.execute_script("return arguments[0].scrollIntoView(true);", button)

robotCheckbox = driver.find_element_by_id("robotCheckbox")
robotCheckbox.click()

robotsRadioRule = driver.find_element_by_id("robotsRule")
robotsRadioRule.click()

button.click()

time.sleep(10)

driver.quit()
