import allure

from locators import order_page_locators as order_loc
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Открыть ленту заказов")
    def open(self):
        self.click_order_feed_link()
        self.wait_visible(order_loc.FEED_TITLE)
        self.wait_loading_modal_closed()

    @allure.step("Получить счётчик «Выполнено за все время»")
    def get_total_counter(self):
        return int(self.wait_visible(order_loc.TOTAL_COUNTER).text.strip())

    @allure.step("Получить счётчик «Выполнено за сегодня»")
    def get_today_counter(self):
        return int(self.wait_visible(order_loc.TODAY_COUNTER).text.strip())

    def _wait_counter_greater_than(self, locator, value):
        def _predicate(_driver):
            text = self.find_element(locator).text.strip()
            return text.isdigit() and int(text) > value

        return self.wait_for(_predicate)

    @allure.step("Дождаться роста счётчика «Выполнено за все время»")
    def wait_total_counter_greater_than(self, value):
        return self._wait_counter_greater_than(order_loc.TOTAL_COUNTER, value)

    @allure.step("Дождаться роста счётчика «Выполнено за сегодня»")
    def wait_today_counter_greater_than(self, value):
        return self._wait_counter_greater_than(order_loc.TODAY_COUNTER, value)

    @allure.step("Проверить, что заказ {number} появился в ленте")
    def is_order_in_feed(self, number):
        return self.is_visible(
            self.format_locator(order_loc.ORDER_NUMBER_IN_FEED, number)
        )

    @allure.step("Кликнуть по первому заказу в ленте")
    def click_first_order(self):
        self.wait_clickable(order_loc.ORDER_CARD).click()

    @allure.step("Получить номер заказа из карточки в истории")
    def get_order_card_number(self):
        return self.wait_visible(order_loc.ORDER_CARD_NUMBER).text

    @allure.step("Проверить, что заказ {number} отображается в ленте")
    def is_order_number_in_feed_cards(self, number):
        return self.is_visible(
            self.format_locator(order_loc.ORDER_NUMBER_IN_CARDS, number)
        )

    @allure.step("Получить номер заказа из попапа")
    def get_order_details_number(self):
        return self.wait_visible(order_loc.ORDER_DETAILS_NUMBER).text
