import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
from constants import Constants
from locators import Locators


class TestConstructorBuns:
    @pytest.mark.usefixtures("driver")
    def test_constructor_buns_section(self, driver):
        # переходим в личный кабинет
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.LOGIN_TEXT))
        # логинимся
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_IN_ACC).click()
        # ждем переход на главную страницу
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.CONSTRUCT_BURGER))
        # скроллим до появления раздела 'Булки'
        last_element = driver.find_element(*Locators.BUNS_TEXT)
        driver.execute_script("arguments[0].scrollIntoView();", last_element)

        assert last_element.text == 'Булки'


class TestConstructorSauces:
    @pytest.mark.usefixtures("driver")
    def test_constructor_sauces_section(self, driver):
        # переходим в личный кабинет
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.LOGIN_TEXT))
        # логинимся
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_IN_ACC).click()
        # ждем переход на главную страницу
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.CONSTRUCT_BURGER))
        # скроллим до появления раздела 'Соусы'
        last_element = driver.find_element(*Locators.SAUCES_TEXT)
        driver.execute_script("arguments[0].scrollIntoView();", last_element)

        assert last_element.text == 'Соусы'


class TestConstructorFillings:
    @pytest.mark.usefixtures("driver")
    def test_constructor_fillings_section(self, driver):
        # переходим в личный кабинет
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.LOGIN_TEXT))
        #логинимся
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_IN_ACC).click()
        # ждем переход на главную страницу
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.CONSTRUCT_BURGER))
        # скроллим дл появления раздела 'Начинки'
        last_element = driver.find_element(*Locators.FILLINGS_TEXT)
        driver.execute_script("arguments[0].scrollIntoView();", last_element)

        assert last_element.text == 'Начинки'
