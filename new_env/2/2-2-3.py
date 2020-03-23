from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("num1")
    x2 = x.text
    x3 = int(x2)
    y = browser.find_element_by_id("num2")
    y2 = y.text
    y3 = int(y2)
    z = x3 + y3
    z2 = str(z)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z2)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()