import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('adress', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
#"236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"
def test_guest_should_see_login_link(browser, adress):
    link = f"https://stepik.org/lesson/{adress}/step/1"
    browser.get(link)
    browser.implicitly_wait(100)

    place = browser.find_element_by_css_selector("[placeholder='Напишите ваш ответ здесь...']")
    answer = str(math.log(int(time.time())))
    place.send_keys(answer)

    button = browser.find_element_by_css_selector("[class='submit-submission']")
    button.click()

    result = browser.find_element_by_css_selector("[class='smart-hints__hint']")
    x = result.text
    assert "Correct!" == x, f'Error: {x}'
