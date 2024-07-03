from selenium.webdriver.common.by import By


class Locators:
    # база
    NAME_INPUT = (By.XPATH, '//label[text() = "Имя"]/following-sibling::input') # поле для ввода имени
    EMAIL_INPUT = (By.XPATH, '//label[text() = "Email"]/following-sibling::input') # поле для ввода email
    PASSWORD_INPUT = (By.XPATH, '//label[text() = "Пароль"]/following-sibling::input') # поле для ввода пароля

    # кнопки для входа в личный кабнет
    ACCOUNT_BUTTON = (By.XPATH, '//a[@href = "/account"]/p[text() = "Личный Кабинет"]') # кнопка 'Личный кабинет'
    LOGIN_BUTTON_ON_REG_FORM = (By.XPATH, '//p[text() = "Уже зарегистрированы?"]/a[@href = "/login"]') # кнопка 'Войти' на странице регистрации
    LOGIN_BUTTON_IN_ACC = (By.XPATH, '//button[text() = "Войти"]') # кнопка 'Войти' на странице авторизации
    LOGIN_BUTTON_ON_PASSWORD_RECOVERY = (By.XPATH, '//a[@href = "/login"][text() = "Войти"]') # кнопка 'Войти' на странице восстановления пароля
    ACCOUNT_LOGIN_BUTTON = (By.XPATH, '//button[contains(text(),"Войти в аккаунт")]') # кнопка 'Войти в аккаунт' на главной странице

    # кнопки для регистрации
    REGISTRATION_BUTTON = (By.XPATH, '//a[@href = "/register"][text() = "Зарегистрироваться"]') # кнопка 'Зарегистрироваться' на странице авторизации
    TO_REGISTER_BUTTON = (By.XPATH, '//button[text() = "Зарегистрироваться"]') # кнопка 'Зарегистрироваться' на странице регистрации

    # кнопки для восстановления пароля
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, '//a[@href = "/forgot-password"][text() = "Восстановить пароль"]') # кнопка 'Восстановить пароль' на странице авторизации

    # кнопки для выхода из личного кабинета
    LOGOUT_BUTTON = (By.XPATH, '//button[text() = "Выход"]')

    # кнопки из раздела "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, '//a[@href="/"]/p[text() = "Конструктор"]') # кнопка "Конструктор" на главной странице

    # тексты
    LOGIN_TEXT = (By.XPATH, '//h2[text() = "Вход"]') # текст "Вход" на странице авторизации
    REGISTRATION_TEXT = (By.XPATH, '//h2[text() = "Регистрация"]') # текст "Регистрация" на странице регистрации
    CONSTRUCT_BURGER = (By.XPATH, '//h1[text() = "Соберите бургер"]') # текст "Соберите бургер"
    PASSWORD_RECOVERY_TEXT = (By.XPATH, '//h2[text() = "Восстановление пароля"]') # текст "Восстановление пароля"
    INCORRECT_PASSWORD = (By.XPATH, '//p[text() = "Некорректный пароль"]') # текст с ошибкой "Некорректный пароль"
    CHANGE_PERSONAL_DATA_TEXT = (By.XPATH, '//p[text() = "В этом разделе вы можете изменить свои персональные данные"]') # текст "В этом разделе вы можете изменить свои персональные данные"
    BUNS_TEXT = (By.XPATH, '//h2[text() = "Булки"]')  # текст "Булки" в блоке с конструктором
    SAUCES_TEXT = (By.XPATH, '//h2[text() = "Соусы"]') # текст "Соусы" в блоке с конструктором
    FILLINGS_TEXT = (By.XPATH, '//h2[text() = "Начинки"]') # текст "Начинки" в блоке с конструктором
