import allure

import urls
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestPersonalAccount:
    @allure.title("Переход в личный кабинет")
    @allure.description(
        "Проверяем переход в личный кабинет по клику на «Личный Кабинет»"
    )
    def test_transition_to_personal_account(self, authorized_driver):
        profile_page = ProfilePage(authorized_driver)

        profile_page.open()

        assert profile_page.get_current_url() == urls.PROFILE_PAGE
        assert profile_page.is_profile_page()

    @allure.title("Переход из личного кабинета в конструктор")
    @allure.description(
        "Проверяем переход в конструктор по клику на «Конструктор» из личного кабинета"
    )
    def test_transition_to_constructor_from_profile(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        profile_page = ProfilePage(authorized_driver)

        profile_page.open()
        main_page.click_constructor_link()

        assert main_page.get_current_url() == urls.MAIN_PAGE

    @allure.title("Переход из личного кабинета в конструктор по логотипу")
    @allure.description(
        "Проверяем переход в конструктор по клику на логотип из личного кабинета"
    )
    def test_transition_to_constructor_by_logo(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        profile_page = ProfilePage(authorized_driver)

        profile_page.open()
        main_page.click_logo()

        assert main_page.get_current_url() == urls.MAIN_PAGE

    @allure.title("Переход в раздел «История заказов»")
    @allure.description(
        "Проверяем переход в раздел «История заказов» по клику на соответствующий пункт"
    )
    def test_transition_to_order_history(self, authorized_driver):
        profile_page = ProfilePage(authorized_driver)

        profile_page.open()
        profile_page.click_order_history_link()

        assert profile_page.get_current_url() == urls.ORDER_HISTORY_PAGE

    @allure.title("Выход из аккаунта")
    @allure.description(
        "Проверяем выход из аккаунта по кнопке «Выход» в личном кабинете"
    )
    def test_logout(self, authorized_driver):
        profile_page = ProfilePage(authorized_driver)

        profile_page.open()
        profile_page.logout()

        assert profile_page.get_current_url() == urls.LOGIN_PAGE
