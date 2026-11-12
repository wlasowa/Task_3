import allure

import data
from locators import main_page_locators as main_loc
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Дождаться заголовка конструктора")
    def wait_constructor_heading(self):
        self.wait_visible(main_loc.CONSTRUCTOR_HEADING)

    @allure.step("Кликнуть «Войти в аккаунт»")
    def click_enter_account_button(self):
        self.wait_clickable(main_loc.ENTER_ACCOUNT_BUTTON).click()

    @allure.step("Кликнуть по ингредиенту «{name}»")
    def click_ingredient(self, name):
        self.wait_clickable(self.format_locator(main_loc.INGREDIENT_NAME, name)).click()

    @allure.step("Получить заголовок модального окна")
    def get_modal_title(self):
        return self.wait_visible(main_loc.MODAL_TITLE).text

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.wait_clickable(main_loc.MODAL_CLOSE_BUTTON).click()

    @allure.step("Проверить, что модальное окно закрыто")
    def is_modal_closed(self):
        return self.is_invisible(main_loc.MODAL_TITLE)

    @allure.step("Перетащить ингредиент «{name}» в корзину")
    def drag_ingredient(self, name):
        source = self.wait_visible(self.format_locator(main_loc.INGREDIENT_CARD, name))
        target = self.wait_visible(main_loc.BASKET)
        self.drag_and_drop(source, target)

    @allure.step("Собрать бургер для заказа")
    def build_default_burger(self):
        self.drag_ingredient(data.INGREDIENT_BUN)
        self.drag_ingredient(data.INGREDIENT_FILLING)

    @allure.step("Получить каунтер ингредиента «{name}»")
    def get_ingredient_counter(self, name):
        return int(
            self.wait_visible(
                self.format_locator(main_loc.INGREDIENT_COUNTER, name)
            ).text
        )

    @allure.step("Дождаться, пока каунтер ингредиента «{name}» станет {value}")
    def wait_ingredient_counter(self, name, value):
        def _predicate(_driver):
            text = self.find_element(
                self.format_locator(main_loc.INGREDIENT_COUNTER, name)
            ).text
            return text.isdigit() and int(text) == value

        self.wait_for(_predicate)

    @allure.step("Кликнуть «Оформить заказ»")
    def click_checkout_button(self):
        self.wait_clickable(main_loc.CHECKOUT_BUTTON).click()
        self.wait_loading_modal_closed()

    @allure.step("Получить номер оформленного заказа")
    def get_order_number(self):
        def _predicate(_driver):
            text = self.find_element(main_loc.ORDER_NUMBER).text
            return text if text.isdigit() and text != "9999" else False

        return self.wait_for(_predicate)

    @allure.step("Оформить заказ и получить его номер")
    def place_order(self):
        self.build_default_burger()
        self.click_checkout_button()
        number = self.get_order_number()
        self.close_modal()
        self.is_modal_closed()
        return number

    @allure.step("Проверить, что юзер авторизован")
    def is_logged_in(self):
        return self.is_visible(main_loc.CHECKOUT_BUTTON)
