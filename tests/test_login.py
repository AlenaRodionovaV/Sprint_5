import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
from constants import Constants
from locators import Locators


class TestLoginFromMainPage:
    @pytest.mark.usefixtures("driver")
    def test_login_from_main_page(self, driver):
        # переходим с главной страницы сайта в личный кабинет по кнопке 'Войти в аккаунт'
        driver.find_element(*Locators.ACCOUNT_LOGIN_BUTTON).click()
        # ждем появление текста "Вход"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_TEXT))
        # заполняем поля 'email', 'пароль' и нажимаем 'Войти'
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_IN_ACC).click()
        # ждем переход на главную страницу и появление текста "Соберите бургер"
        success_login_button = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.CONSTRUCT_BURGER))
        assert success_login_button.text == 'Соберите бургер'


class TestLoginFromAccount:
    @pytest.mark.usefixtures("driver")
    def test_login_from_account(self, driver):
        # переходим с главной страницы сайта в личный кабинет по кнопке 'Личный кабинет'
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        # ждем появление текста "Вход"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_TEXT))
        # заполняем поля 'email', 'пароль' и нажимаем 'Войти'
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_IN_ACC).click()
        # ждем переход на главную страницу и появление текста "Соберите бургер"
        success_login_acc = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.CONSTRUCT_BURGER))
        assert success_login_acc.text == 'Соберите бургер'


class TestLoginFromRegistrationForm:
    @pytest.mark.usefixtures("driver")
    def test_login_from_registration_form(self, driver):
        # переходим с главной страницы сайта в личный кабинет по кнопке 'Личный кабинет'
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        # ждем появление текста "Вход"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_TEXT))
        # нажимаем кнопку 'Зарегистрироваться'
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        # ждем появление текста "Регистрация"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_TEXT))
        # нажимаем кнопку 'Войти' под формой заполнения
        driver.find_element(*Locators.LOGIN_BUTTON_ON_REG_FORM).click()
        # ждем появление текста "Вход"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_TEXT))
        # заполняем поля 'email', 'пароль' и нажимаем 'Войти'
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_IN_ACC).click()
        # ждем переход на главную страницу и появление текста "Соберите бургер"
        success_login_from_reg = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.CONSTRUCT_BURGER))

        assert success_login_from_reg.text == 'Соберите бургер'


class TestLoginFromPasswordRecoveryForm:
    @pytest.mark.usefixtures("driver")
    def test_login_from_password_recovery_form(self, driver):
        # переходим с главной страницы сайта в личный кабинет по кнопке 'Личный кабинет'
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        # ждем появление текста "Вход"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_TEXT))
        # нажимаем кнопку 'Восстановить пароль' под формой заполнения
        driver.find_element(*Locators.PASSWORD_RECOVERY_BUTTON).click()
        # ждем появление текста "Восстановление пароля"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PASSWORD_RECOVERY_TEXT))
        # нажимаем кнопку 'Войти' под формой заполнения
        driver.find_element(*Locators.LOGIN_BUTTON_ON_PASSWORD_RECOVERY).click()
        # ждем появление текста "Вход"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LOGIN_TEXT))
        # заполняем поля 'email', 'пароль' и нажимаем 'Войти'
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_IN_ACC).click()
        # ждем переход на главную страницу и появление текста "Соберите бургер"
        success_login_password_rec = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.CONSTRUCT_BURGER))

        assert success_login_password_rec.text == 'Соберите бургер'
