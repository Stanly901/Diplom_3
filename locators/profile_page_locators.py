from selenium.webdriver.common.by import By

class ProfilePageLocators:

    ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")  # Кнопка "Личный кабинет"
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")  # Поле ввода почты
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")  # Поле ввода пароля
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.button_button__33qZ0')  # Кнопка "Войти"
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")  # Локатор успешного входа в личный кабинет (кнопка "Выход")
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']")  # Кнопка "История заказов"
    ORDER_COMPLETED = (By.XPATH, "//p[@class='OrderHistory_visible__19YMB text text_type_main-small mb-7']")  # Выполненные заказы в "Историях заказов"
    LOGIN_AFTER_LOGOUT = (By.XPATH, "//h2[contains(text(),'Вход')]") # Локатор успешного выхода из личного кабинет, кнопка "Вход"
    LOGIN_AFTER_LOGOUT_BURGER = (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']") # Локатор успешной авторизации