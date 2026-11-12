import allure

import data
import urls
from pages.main_page import MainPage


class TestMainPage:
    @allure.title("Переход в конструктор по клику на «Конструктор»")
    @allure.description(
        "Проверяем переход в конструктор по клику на «Конструктор» из ленты заказов"
    )
    def test_transition_to_constructor(self, driver):
        main_page = MainPage(driver)

        main_page.click_order_feed_link()
        main_page.click_constructor_link()

        assert main_page.get_current_url() == urls.MAIN_PAGE
        main_page.wait_constructor_heading()

    @allure.title("Переход в ленту заказов по клику на «Лента Заказов»")
    @allure.description(
        "Проверяем переход в ленту заказов по клику на «Лента Заказов» в шапке"
    )
    def test_transition_to_order_feed(self, driver):
        main_page = MainPage(driver)

        main_page.click_order_feed_link()

        assert main_page.get_current_url() == urls.FEED_PAGE

    @allure.title("Открытие попапа с деталями ингредиента")
    @allure.description(
        "Проверяем, что по клику на ингредиент открывается попап «Детали ингредиента»"
    )
    def test_ingredient_details_popup(self, driver):
        main_page = MainPage(driver)

        main_page.click_ingredient("Краторная булка N-200i")

        assert main_page.get_modal_title() == "Детали ингредиента"

    @allure.title("Закрытие попапа с деталями ингредиента")
    @allure.description(
        "Проверяем, что попап «Детали ингредиента» закрывается по крестику"
    )
    def test_ingredient_details_popup_close(self, driver):
        main_page = MainPage(driver)

        main_page.click_ingredient("Флюоресцентная булка R2-D3")
        main_page.close_modal()

        assert main_page.is_modal_closed()

    @allure.title("Увеличение каунтера ингредиента")
    @allure.description(
        "Проверяем, что при добавлении ингредиента в заказ увеличивается его каунтер"
    )
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        name = data.INGREDIENT_FILLING

        assert main_page.get_ingredient_counter(name) == 0

        main_page.drag_ingredient(name)
        main_page.wait_ingredient_counter(name, 1)

        assert main_page.get_ingredient_counter(name) == 1

    @allure.title("Оформление заказа залогиненным юзером")
    @allure.description("Проверяем, что залогиненный юзер может оформить заказ")
    def test_logged_in_user_can_place_order(self, authorized_driver):
        main_page = MainPage(authorized_driver)

        order_number = main_page.place_order()

        assert order_number.isdigit()
