from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import math

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")


WebDriverWait(browser, 12).until(
    expected_conditions.text_to_be_present_in_element((By.ID, "price"), "100"))

button = browser.find_element_by_id("book")
button.click()

x = int(browser.find_element_by_id("input_value").text)
f = math.log(abs(12 * math.sin(x)), math.e)

answer = browser.find_element_by_id("answer")
answer.send_keys(str(f))

buttonSubmit = browser.find_element_by_id("solve")
buttonSubmit.click()

alert = browser.switch_to.alert
response = alert.text
print(response)

browser.quit()