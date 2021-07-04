import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))




# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/get_attribute.html')

x_element = driver.find_element_by_id("treasure")
x = x_element.get_attribute("valuex")
y = calc(x)
driver.find_element_by_id("answer").send_keys(y)
driver.find_element_by_id("robotCheckbox").click()
driver.find_element_by_id("robotsRule").click()
driver.find_element_by_css_selector("button[type=submit]").click()
driver.fin
time.sleep(5)
driver.quit()
