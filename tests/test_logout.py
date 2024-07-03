import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
from constants import Constants
from locators import Locators


class TestLogoutFromAcc:
    @pytest.mark.usefixtures("driver")
    def test_logout_from_acc(self, driver):
        # переходим с главной страницы сайта в личный кабинет по кнопке 'Личный кабинет'
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        # ждем появление текста "Вход"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_TEXT))
        # заполняем поля 'email', 'пароль', нажимаем кнопку 'Войти'
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_IN_ACC).click()
        # ждем переход на главную страницу и появление текста "Соберите бургер"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.CONSTRUCT_BURGER))
        # после перехода на главную страницу нажимаем кнопку 'Личный кабинет'
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        # ждем появление текста "В этом разделе вы можете изменить свои персональные данные"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.CHANGE_PERSONAL_DATA_TEXT))
        # нажимаем на кнопку "Выход"
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        # ждем появление текста "Вход"
        success_logout = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.LOGIN_TEXT))

        assert success_logout.text == 'Вход'
