import allure
from selenium.webdriver.support import expected_conditions as ec

import urls
from locators import login_page_locators as login_loc
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step("Открыть страницу входа")
    def open(self):
        self.open_page(urls.LOGIN_PAGE)

    @allure.step("Ввести email {email}")
    def fill_email(self, email):
        self.wait_visible(login_loc.EMAIL_INPUT).send_keys(email)

    @allure.step("Ввести пароль")
    def fill_password(self, password):
        self.wait_visible(login_loc.PASSWORD_INPUT).send_keys(password)

    @allure.step("Кликнуть «Войти»")
    def click_login_button(self):
        self.wait_clickable(login_loc.LOGIN_BUTTON).click()
        self.wait_loading_modal_closed()

    @allure.step("Залогиниться под {email}")
    def login(self, email, password):
        self.fill_email(email)
        self.fill_password(password)
        self.click_login_button()
        self.wait_for(ec.url_to_be(urls.MAIN_PAGE))

    @allure.step("Перейти к восстановлению пароля")
    def click_forgot_password_link(self):
        self.wait_clickable(login_loc.FORGOT_PASSWORD_LINK).click()

    @allure.step("Кликнуть «Восстановить»")
    def click_restore_button(self):
        self.wait_clickable(login_loc.RESTORE_BUTTON).click()
        self.wait_for(ec.url_contains("/reset-password"))

    @allure.step("Кликнуть по кнопке показать/скрыть пароль")
    def click_show_password_button(self):
        self.wait_clickable(login_loc.PASSWORD_SHOW_BUTTON).click()

    @allure.step("Проверить, что поле пароля активно")
    def is_password_field_active(self):
        wrapper_class = self.wait_visible(
            login_loc.PASSWORD_FIELD_WRAPPER
        ).get_attribute("class")
        return "input_status_active" in wrapper_class

    @allure.step("Кликнуть «Войти» на странице восстановления пароля")
    def click_forgot_login_link(self):
        self.wait_clickable(login_loc.FORGOT_LOGIN_LINK).click()
