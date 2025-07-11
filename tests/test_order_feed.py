import allure
from pages.order_feed_page import OrderFeedPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from data.data import EMAIL, PASSWORD

@allure.feature('Лента заказов')
@allure.story('Тесты функционала ленты заказов')
class TestOrderPage:

    @allure.title('При создании нового заказа счётчик «Выполнено за всё время» увеличивается')
    def test_total_orders_counter_increases_after_new_order(self, driver):
        order_feed_page = OrderFeedPage(driver)
        main_page = MainPage(driver)
        account_page = ProfilePage(driver)

        with allure.step('Выполняем вход в аккаунт'):
            account_page.login(EMAIL, PASSWORD)

        with allure.step('Открываем ленту заказов'):
            order_feed_page.click_feed()

        with allure.step('Получаем начальный счётчик заказов'):
            initial_total_orders = order_feed_page.get_total_orders_counter()

        with allure.step('Создаем новый заказ'):
            order_feed_page.click_constructor()
            main_page.drag_and_drop_ingredient()
            order_feed_page.click_place_an_order()

            order_feed_page.get_order_id_from_details()
            order_feed_page.click_close_order_details()

        with allure.step('Проверяем, что общий счётчик заказов увеличился'):
            order_feed_page.open_feed_page()
            updated_total_orders = order_feed_page.get_total_orders_counter()
            assert updated_total_orders > initial_total_orders, \
                f"Ожидалось увеличение счетчика. Было: {initial_total_orders}, стало: {updated_total_orders}"

    @allure.title('При создании нового заказа счётчик «Выполнено за сегодня» увеличивается')
    def test_today_orders_counter_increases_after_new_order(self, driver):
        order_feed_page = OrderFeedPage(driver)
        main_page = MainPage(driver)
        account_page = ProfilePage(driver)

        with allure.step('Выполняем вход в аккаунт'):
            account_page.login(EMAIL, PASSWORD)

        with allure.step('Открываем ленту заказов'):
            order_feed_page.click_feed()

        with allure.step('Получаем начальный счётчик заказов за сегодня'):
            initial_today_orders = order_feed_page.get_today_completed_counter()

            order_feed_page.click_constructor()

        with allure.step('Создаем новый заказ'):
            order_feed_page.click_constructor()
            main_page.drag_and_drop_ingredient()

            order_feed_page.click_place_an_order()

            order_feed_page.get_order_id_from_details()


        with allure.step('Закрываем детали заказа и открываем ленту заказов'):
            order_feed_page.click_close_order_details()
            order_feed_page.click_feed()

        with allure.step('Проверяем, что счётчик заказов за сегодня увеличился'):
            updated_today_orders = order_feed_page.get_today_completed_counter()
            assert updated_today_orders > initial_today_orders, \
                f"Ожидалось увеличение счетчика на 1. Было: {initial_today_orders}, стало: {updated_today_orders}"

    @allure.title('После оформления заказа его номер появляется в разделе «В работе»')
    def test_order_number_appears_in_in_progress_after_order_placement(self, driver):
        order_feed_page = OrderFeedPage(driver)
        main_page = MainPage(driver)
        account_page = ProfilePage(driver)

        with allure.step('Выполняем вход в аккаунт'):
            account_page.login(EMAIL, PASSWORD)

        with allure.step('Создаем новый заказ'):
            order_feed_page.click_constructor()
            main_page.drag_and_drop_ingredient()
            order_feed_page.click_place_an_order()

        with allure.step('Получаем идентификатор заказа'):
            order_id = order_feed_page.get_order_id_from_details()

        with allure.step('Закрываем модальное окно и проверяем раздел "В работе"'):
            order_feed_page.click_close_order_details()
            order_feed_page.click_feed()

        with allure.step('Проверяем, что номер заказа появился в ленте'):
            assert order_feed_page.is_order_number_displayed_anywhere(order_id), \
                f"Номер заказа {order_id} не появился ни в 'В работе', ни в 'Готовы'"