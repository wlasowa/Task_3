import allure
from selenium.webdriver.support import expected_conditions as ec

import urls
from locators import profile_page_locators as profile_loc
from pages.base_page import BasePage


class ProfilePage(BasePage):
    @allure.step("Перейти в личный кабинет")
    def open(self):
        self.click_personal_account_link()
        self.wait_visible(profile_loc.PROFILE_TEXT)
        self.wait_loading_modal_closed()

    @allure.step("Перейти в раздел «История заказов»")
    def click_order_history_link(self):
        self.wait_clickable(profile_loc.ORDER_HISTORY_LINK).click()
        self.wait_for(ec.url_to_be(urls.ORDER_HISTORY_PAGE))
        self.wait_loading_modal_closed()

    @allure.step("Проверить, что открыт личный кабинет")
    def is_profile_page(self):
        return self.wait_visible(profile_loc.PROFILE_TEXT).is_displayed()

    @allure.step("Выйти из аккаунта")
    def logout(self):
        self.wait_clickable(profile_loc.LOGOUT_BUTTON).click()
        self.wait_for(ec.url_to_be(urls.LOGIN_PAGE))
