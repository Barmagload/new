from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button=browser.find_element_by_css_selector("[type=submit]")
    button.click()

    newtab=browser.window_handles[1]
    browser.switch_to.window(newtab)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    answer=browser.find_element_by_id("answer")
    answer.send_keys(y)

    button2 = browser.find_element_by_css_selector("[type='submit']")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()