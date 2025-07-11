from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    LAST_ORDER = (By.XPATH, "(//ul[contains(@class,'OrderFeed_orderList')]//li)[last()]")
    ORDER_IN_PROGRESS_LOCATOR = (
        By.XPATH,
        "//ul[contains(@class, 'OrderFeed_orderList__cByyi')]//li[contains(., '{}')]"
    )

    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[preceding-sibling::p[text()='Выполнено за все время:']]")
    TODAY_COMPLETED_COUNTER = (By.XPATH, "//p[preceding-sibling::p[text()='Выполнено за сегодня:']]")

    ORDER_DETAILS_CONTENT = (By.XPATH, "//div[contains(@class, 'Modal_orderBox')]")
    CLOSE_ORDER_DETAILS_BUTTON = (By.XPATH, "//section[contains(@class,'Modal_modal_opened')]//button[@type='button']")

    ORDER_ID = (By.XPATH, "//h2[contains(@class, 'text_type_digits-large')]")
    ORDER_ID_IN_FEED = (
        By.XPATH, "//ul[contains(@class,'OrderFeed_orderList')]//li//*[contains(text(), '{0}')]"
    )

    LOGIN_AFTER_LOGOUT_BURGER = (By.XPATH, "//a[@href='/login']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[@href='/account/orders']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    PLACE_AN_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")