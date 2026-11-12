from selenium.webdriver.common.by import By

FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")

TOTAL_COUNTER = (
    By.XPATH,
    (
        "//p[text()='Выполнено за все время:']"
        "/following-sibling::p[contains(@class, 'OrderFeed_number')]"
    ),
)
TODAY_COUNTER = (
    By.XPATH,
    (
        "//p[text()='Выполнено за сегодня:']"
        "/following-sibling::p[contains(@class, 'OrderFeed_number')]"
    ),
)

ORDER_CARD = (By.XPATH, "//a[contains(@class, 'OrderHistory_link')]")
ORDER_CARD_NUMBER = (
    By.XPATH,
    (
        "//a[contains(@class, 'OrderHistory_link')]"
        "//p[contains(@class, 'text_type_digits-default') and contains(text(), '#')]"
    ),
)
ORDER_NUMBER_IN_CARDS = (
    By.XPATH,
    (
        "//a[contains(@class, 'OrderHistory_link')]"
        "//p[contains(@class, 'text_type_digits-default') and normalize-space()='{}']"
    ),
)
ORDER_DETAILS_NUMBER = (
    By.XPATH,
    (
        "//div[contains(@class, 'Modal_orderBox')]"
        "//p[contains(@class, 'text_type_digits-default') and contains(text(), '#')]"
    ),
)
ORDER_NUMBER_IN_FEED = (
    By.XPATH,
    "//ul[contains(@class, 'OrderFeed_orderList')]/li[normalize-space()='{}']",
)
