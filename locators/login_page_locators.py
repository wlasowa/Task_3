from selenium.webdriver.common.by import By

EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")

RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
FORGOT_LOGIN_LINK = (By.XPATH, "//a[@href='/login']")

PASSWORD_FIELD_WRAPPER = (By.XPATH, "//input[@name='Введите новый пароль']/..")
PASSWORD_SHOW_BUTTON = (By.CSS_SELECTOR, "div.input__icon-action")
