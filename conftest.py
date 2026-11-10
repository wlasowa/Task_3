import pytest
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

import helpers
import urls
from api_client import ApiClient
from locators import main_page_locators as main_loc
from pages.login_page import LoginPage
from pages.main_page import MainPage
from webdriver_factory import WebdriverFactory


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox"],
        help="Браузер для запуска тестов",
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    wd = WebdriverFactory.get_webdriver(browser)
    wd.get(urls.MAIN_PAGE)
    WebDriverWait(wd, 20).until(
        ec.presence_of_element_located(main_loc.CONSTRUCTOR_LINK)
    )
    WebDriverWait(wd, 20).until_not(
        ec.visibility_of_element_located(main_loc.LOADING_MODAL)
    )
    yield wd
    wd.quit()


@pytest.fixture
def test_user():
    api_client = ApiClient()
    user_data = helpers.generate_user_data()
    response = api_client.register(user_data)
    assert response.status_code == 200, f"Не удалось создать юзера: {response.text}"
    user_data["access_token"] = response.json()["accessToken"]
    yield user_data
    api_client.delete_user(user_data["access_token"])


@pytest.fixture
def authorized_driver(driver, test_user):
    main_page = MainPage(driver)
    main_page.click_enter_account_button()
    login_page = LoginPage(driver)
    login_page.login(test_user["email"], test_user["password"])
    return driver
