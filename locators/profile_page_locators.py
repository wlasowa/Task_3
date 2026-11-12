from selenium.webdriver.common.by import By

ORDER_HISTORY_LINK = (By.XPATH, "//a[@href='/account/order-history']")
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
PROFILE_TEXT = (
    By.XPATH,
    "//p[contains(@class, 'Account_text') and contains(text(), 'В этом разделе')]",
)
