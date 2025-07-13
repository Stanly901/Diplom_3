import allure
from .base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators
from data.urls import LOGIN_URL

class ProfilePage(BasePage):

    @allure.step("Нажимаем на кнопку 'Личный кабинет'")
    def click_account_button(self):
        self.wait_for_element_visible(ProfilePageLocators.LOGIN_AFTER_LOGOUT_BURGER)
        self.click_when_clickable(ProfilePageLocators.ACCOUNT_BUTTON)

    @allure.step("Переходим в 'Историю заказов'")
    def click_order_history_button(self):
        self.click_to_element(ProfilePageLocators.ORDER_HISTORY_BUTTON)

    @allure.step("Нажимаем на кнопку 'Выход'")
    def click_logout_button(self):
        self.click_to_element(ProfilePageLocators.LOGOUT_BUTTON)

    @allure.step("Проверяем, что кнопка 'Выход' видна")
    def is_logout_button_visible(self):
        return self.is_element_visible(ProfilePageLocators.LOGOUT_BUTTON)

    @allure.step("Проверяем, что заказ завершён")
    def is_order_completed(self):
        return self.get_text_from_element(ProfilePageLocators.ORDER_COMPLETED) == "Выполнен"

    @allure.step("Проверяем, что отображается кнопка 'Вход'")
    def is_login_button_visible_after_logout(self):
        return self.get_text_from_element(ProfilePageLocators.LOGIN_AFTER_LOGOUT) == "Вход"

    @allure.step("Открываем страницу входа")
    def open_login_page(self):
        self.navigate_to(LOGIN_URL)

    @allure.step("Выполняем вход в аккаунт с email: {email}")
    def login(self, email, password):
        self.open_login_page()
        self.add_text_to_element(ProfilePageLocators.EMAIL_INPUT, email)
        self.add_text_to_element(ProfilePageLocators.PASSWORD_INPUT, password)
        self.click_with_js(ProfilePageLocators.LOGIN_BUTTON)