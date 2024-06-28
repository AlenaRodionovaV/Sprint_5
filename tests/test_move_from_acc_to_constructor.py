import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
from constants import Constants
from locators import Locators


class TestMoveToConstructor:
    @pytest.mark.usefixtures("driver")
    def test_move_from_acc_to_constructor(self, driver):

        # переходим с главной страницы сайта в личный кабинет по кнопке 'Личный кабинет'
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        # ждем появление текста "Вход"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LOGIN_TEXT))
        # заполняем поля 'email', 'пароль' и нажимаем 'Войти'
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_IN_ACC).click()
        # ждем переход на главную страницу и появление текста "Соберите бургер"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.CONSTRUCT_BURGER))
        # переходим с главной страницы сайта в личный кабинет по кнопке 'Личный кабинет'
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        # ждем появление текста "В этом разделе вы можете изменить свои персональные данные"
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.CHANGE_PERSONAL_DATA_TEXT))
        # нажимаем на кнопку 'Конструктор'
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        # ждем появления текста "Соберите бургер"
        success_move_to_constructor = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.CONSTRUCT_BURGER))

        assert success_move_to_constructor.text == 'Соберите бургер'
