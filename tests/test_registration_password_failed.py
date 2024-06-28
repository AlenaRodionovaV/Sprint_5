import pytest
from faker import Faker
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
from locators import Locators


class TestRegistrationFailed:

    @pytest.mark.usefixtures("driver")
    def test_registration_failed(self, driver):

        fake = Faker()
        name = fake.name()
        email = fake.email()
        password = '123'

        # переходим с главной страницы сайта в личный кабинет по кнопке 'Войти в аккаунт'
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        # ждем появление текста "Вход"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_TEXT))
        # нажимаем кнопку 'Зарегистрироваться'
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        # ждем появление текста "Регистрация"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_TEXT))
        # заполняем поля 'имя', 'email', 'пароль' и нажимаем 'Зарегистрироваться'
        driver.find_element(*Locators.NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.TO_REGISTER_BUTTON).click()
        # ждем появление текста с ошибкой "Некорректный пароль"
        failed_message = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.INCORRECT_PASSWORD))

        assert failed_message.text == 'Некорректный пароль'
