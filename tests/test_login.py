import allure

import urls
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestLogin:
    @allure.title("Вход через кнопку «Войти в аккаунт»")
    @allure.description(
        "Проверяем вход в аккаунт по кнопке «Войти в аккаунт» на главной странице"
    )
    def test_login_via_enter_account_button(self, driver, test_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.click_enter_account_button()
        login_page.login(test_user["email"], test_user["password"])

        assert login_page.get_current_url() == urls.MAIN_PAGE
        assert main_page.is_logged_in()

    @allure.title("Вход через кнопку «Личный Кабинет»")
    @allure.description("Проверяем вход в аккаунт по кнопке «Личный Кабинет» в шапке")
    def test_login_via_personal_account(self, driver, test_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.click_personal_account_link()
        login_page.login(test_user["email"], test_user["password"])

        assert login_page.get_current_url() == urls.MAIN_PAGE
        assert main_page.is_logged_in()

    @allure.title("Вход через форму восстановления пароля")
    @allure.description(
        "Проверяем вход в аккаунт по кнопке «Войти» на странице восстановления пароля"
    )
    def test_login_via_forgot_password(self, driver, test_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.click_enter_account_button()
        login_page.click_forgot_password_link()
        login_page.click_forgot_login_link()
        login_page.login(test_user["email"], test_user["password"])

        assert login_page.get_current_url() == urls.MAIN_PAGE
        assert main_page.is_logged_in()


class TestPasswordRecovery:
    @allure.title("Переход на страницу восстановления пароля")
    @allure.description(
        "Проверяем переход на страницу восстановления пароля по кнопке «Восстановить пароль»"
    )
    def test_go_to_forgot_password_page(self, driver):
        login_page = LoginPage(driver)

        login_page.open()
        login_page.click_forgot_password_link()

        assert login_page.get_current_url() == urls.FORGOT_PASSWORD_PAGE

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    @allure.description(
        "Проверяем переход к восстановлению пароля после ввода почты и клика «Восстановить»"
    )
    def test_restore_password(self, driver):
        login_page = LoginPage(driver)

        login_page.open()
        login_page.click_forgot_password_link()
        login_page.fill_email("test@example.com")
        login_page.click_restore_button()

        assert "/reset-password" in login_page.get_current_url()

    @allure.title("Показ пароля делает поле активным")
    @allure.description(
        "Проверяем, что клик по кнопке показать/скрыть пароль подсвечивает поле пароля"
    )
    def test_password_field_highlighted(self, driver):
        login_page = LoginPage(driver)

        login_page.open()
        login_page.click_forgot_password_link()
        login_page.fill_email("test@example.com")
        login_page.click_restore_button()
        login_page.click_show_password_button()

        assert login_page.is_password_field_active()
