from selenium import webdriver
import unittest
import time

class TestAbc(unittest.TestCase):
    def test_test1(self):

        link1 = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link1)

        # Ваш код, который заполняет обязательные поля
        input1=browser.find_element_by_css_selector("[placeholder='Input your first name']")
        input1.send_keys("1")
        input2=browser.find_element_by_css_selector("[placeholder='Input your last name']")
        input2.send_keys("2")
        input3=browser.find_element_by_css_selector("[placeholder='Input your email']")
        input3.send_keys("3")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Error1")

    def test_test2(self):

        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1=browser.find_element_by_css_selector("[placeholder='Input your first name']")
        input1.send_keys("1")
        input2=browser.find_element_by_css_selector("[placeholder='Input your last name']")
        input2.send_keys("2")
        input3=browser.find_element_by_css_selector("[placeholder='Input your email']")
        input3.send_keys("3")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Error2")

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")