from .base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from data.data import FEED_URL
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderFeedPage(BasePage):
    def click_last_order(self):
        self.click_to_element(OrderFeedPageLocators.LAST_ORDER)

    def get_order_details_content(self):
        return self.get_text_from_element(OrderFeedPageLocators.ORDER_DETAILS_CONTENT)

    def get_total_orders_counter(self):
        return int(self.get_text_from_element(OrderFeedPageLocators.TOTAL_ORDERS_COUNTER))

    def get_today_completed_counter(self):

        element = self.find_element_with_wait(OrderFeedPageLocators.TODAY_COMPLETED_COUNTER)
        return int(element.text.strip())


    def open_feed_page(self):
        self.navigate_to(FEED_URL)
        self.wait_for_element_visible(OrderFeedPageLocators.FEED_TITLE)

    def click_constructor(self):
        self.click_to_element(OrderFeedPageLocators.CONSTRUCTOR_BUTTON)

    def click_feed(self):
        self.click_when_clickable(OrderFeedPageLocators.ORDER_FEED_BUTTON)

    def click_place_an_order(self):
        self.click_to_element(OrderFeedPageLocators.PLACE_AN_ORDER)


    def click_account_button(self):
        self.click_when_clickable(OrderFeedPageLocators.ACCOUNT_BUTTON)

    def click_order_history_button(self):
        self.click_to_element(OrderFeedPageLocators.ORDER_HISTORY_BUTTON)

    def click_close_order_details(self):
        self.click_when_clickable(OrderFeedPageLocators.CLOSE_ORDER_DETAILS_BUTTON)

    def get_order_id_from_details(self):
        self.find_and_wait_until_text_changes(OrderFeedPageLocators.ORDER_ID, "9999")
        return self.get_text_from_element(OrderFeedPageLocators.ORDER_ID)

    def is_order_id_in_feed(self, order_id):
        formatted_id = f"{int(order_id):07d}"  # Добавляем нули до длины 7
        order_locator = OrderFeedPageLocators.ORDER_ID_IN_FEED
        order_locator = (order_locator[0], order_locator[1].format(formatted_id))
        return self.find_element_with_wait(order_locator)

    def is_order_number_displayed_anywhere(self, order_id: str) -> bool:
        id_str = str(order_id).lstrip('#').lstrip('0')
        locators = [
            (By.XPATH, f"//ul[contains(@class, 'OrderFeed_orderList__cByyi')]//li[contains(., '{id_str}')]"),
            (By.XPATH, f"//ul[contains(@class, 'OrderFeed_orderListReady')]//li[contains(., '{id_str}')]"),
        ]
        for locator in locators:
            try:
                WebDriverWait(self.driver, 7).until(EC.presence_of_element_located(locator))
                return True
            except TimeoutException:
                continue
        return False