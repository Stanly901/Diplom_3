import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    @allure.step("Нажимаем на кнопку 'Конструктор'")
    def click_constructor(self):
        self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Нажимаем на кнопку 'Оформить заказ'")
    def click_place_an_order(self):
        self.click_to_element(MainPageLocators.PLACE_AN_ORDER)

    @allure.step("Проверяем, что секция 'Собери бургер' отображается")
    def is_burger_constructor_visible(self):
        return self.find_element_with_wait(MainPageLocators.BURGER_CONSTRUCTOR_SECTION).is_displayed()

    @allure.step("Нажимаем на кнопку 'Лента заказов'")
    def click_order_feed(self):
        self.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Проверяем, что отображается счетчик заказов")
    def is_order_feed_counter_visible(self):
        return self.find_element_with_wait(MainPageLocators.COMPLETED_ORDERS).is_displayed()

    @allure.step("Кликаем по ингредиенту R2D3")
    def click_ingredient(self):
        self.click_to_element(MainPageLocators.INGREDIENT_R2D3_BUN)

    @allure.step("Проверяем, что открыто окно деталей ингредиента")
    def is_ingredient_details_visible(self):
        return self.is_element_displayed(MainPageLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)

    @allure.step("Закрываем окно с деталями ингредиента")
    def close_ingredient_details(self):
        self.click_to_element(MainPageLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)

    @allure.step("Добавляем ингредиент через кнопку 'Добавить'")
    def add_ingredient_to_order(self):
        self.click_to_element(MainPageLocators.ADD_INGREDIENT_BUTTON)

    @allure.step("Получаем текущее значение счётчика ингредиента")
    def get_ingredient_counter(self):
        return int(self.get_text_from_element(MainPageLocators.INGREDIENT_COUNTER))

    @allure.step("Перетаскиваем ингредиент в заказ")
    def drag_and_drop_ingredient(self):
        ingredient_locator = MainPageLocators.INGREDIENT_R2D3_BUN
        target_locator = MainPageLocators.ORDER_TARGET_TOP
        self.drag_and_drop(ingredient_locator, target_locator)

    @allure.step("Получаем сообщение об успешном оформлении заказа")
    def get_order_success_message(self):
        return self.get_text_from_element(MainPageLocators.ORDER_SUCCESS_MESSAGE)