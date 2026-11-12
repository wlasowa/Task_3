import allure

import helpers
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.profile_page import ProfilePage


class TestOrderFeed:
    @allure.title("Оформленный заказ появляется в ленте заказов")
    @allure.description(
        "Проверяем, что после оформления заказа его номер появляется в ленте заказов"
    )
    def test_order_appears_in_feed(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        order_page = OrderPage(authorized_driver)

        order_number = main_page.place_order()
        normalized_number = helpers.normalize_order_number(order_number)

        order_page.open()

        assert order_page.is_order_in_feed(normalized_number)

    @allure.title("Увеличение счётчика «Выполнено за все время»")
    @allure.description(
        "Проверяем, что после оформления заказа счётчик «Выполнено за все время» растёт"
    )
    def test_total_counter_increases(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        order_page = OrderPage(authorized_driver)

        order_page.open()
        before = order_page.get_total_counter()

        main_page.click_constructor_link()
        main_page.place_order()

        order_page.open()
        order_page.wait_total_counter_greater_than(before)

        assert order_page.get_total_counter() > before

    @allure.title("Увеличение счётчика «Выполнено за сегодня»")
    @allure.description(
        "Проверяем, что после оформления заказа счётчик «Выполнено за сегодня» растёт"
    )
    def test_today_counter_increases(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        order_page = OrderPage(authorized_driver)

        order_page.open()
        before = order_page.get_today_counter()

        main_page.click_constructor_link()
        main_page.place_order()

        order_page.open()
        order_page.wait_today_counter_greater_than(before)

        assert order_page.get_today_counter() > before

    @allure.title("Открытие попапа с деталями заказа из ленты")
    @allure.description(
        "Проверяем, что по клику на заказ в ленте открывается попап с его номером"
    )
    def test_order_details_popup(self, driver):
        order_page = OrderPage(driver)

        order_page.open()
        order_page.click_first_order()

        assert order_page.get_order_details_number().startswith("#")

    @allure.title("Заказ из истории отображается в ленте")
    @allure.description(
        "Проверяем, что заказ юзера из «Истории заказов» отображается в «Ленте заказов»"
    )
    def test_order_history_shown_in_feed(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        profile_page = ProfilePage(authorized_driver)
        order_page = OrderPage(authorized_driver)

        main_page.place_order()

        profile_page.open()
        profile_page.click_order_history_link()
        history_number = order_page.get_order_card_number()

        order_page.open()

        assert order_page.is_order_number_in_feed_cards(history_number)
