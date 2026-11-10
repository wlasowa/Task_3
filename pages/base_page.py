import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from locators import main_page_locators as main_loc


class BasePage:
    TIMEOUT = 15

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def format_locator(locator, *args):
        by, value = locator
        return by, value.format(*args)

    def wait_clickable(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            ec.element_to_be_clickable(locator)
        )

    def wait_visible(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            ec.visibility_of_element_located(locator)
        )

    def wait_invisible(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            ec.invisibility_of_element_located(locator)
        )

    def wait_for(self, condition):
        return WebDriverWait(self.driver, self.TIMEOUT).until(condition)

    def is_visible(self, locator):
        try:
            self.wait_visible(locator)
            return True
        except TimeoutException:
            return False

    def is_invisible(self, locator):
        try:
            self.wait_invisible(locator)
            return True
        except TimeoutException:
            return False

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Открыть страницу {url}")
    def open_page(self, url):
        self.driver.get(url)
        self.wait_loading_modal_closed()

    @allure.step("Дождаться закрытия лоадера")
    def wait_loading_modal_closed(self):
        return self.wait_invisible(main_loc.LOADING_MODAL)

    def drag_and_drop(self, source_element, target_element):
        self.driver.execute_script(
            """
            var src = arguments[0];
            var tgt = arguments[1];
            var dt = new DataTransfer();
            src.dispatchEvent(new DragEvent('dragstart', {dataTransfer: dt, bubbles: true, cancelable: true}));
            tgt.dispatchEvent(new DragEvent('dragenter', {dataTransfer: dt, bubbles: true, cancelable: true}));
            tgt.dispatchEvent(new DragEvent('dragover', {dataTransfer: dt, bubbles: true, cancelable: true}));
            tgt.dispatchEvent(new DragEvent('drop', {dataTransfer: dt, bubbles: true, cancelable: true}));
            src.dispatchEvent(new DragEvent('dragend', {dataTransfer: dt, bubbles: true, cancelable: true}));
            """,
            source_element,
            target_element,
        )

    @allure.step("Кликнуть «Конструктор» в шапке")
    def click_constructor_link(self):
        self.wait_clickable(main_loc.CONSTRUCTOR_LINK).click()

    @allure.step("Кликнуть «Лента Заказов» в шапке")
    def click_order_feed_link(self):
        self.wait_clickable(main_loc.ORDER_FEED_LINK).click()

    @allure.step("Кликнуть «Личный Кабинет» в шапке")
    def click_personal_account_link(self):
        self.wait_clickable(main_loc.PERSONAL_ACCOUNT_LINK).click()

    @allure.step("Кликнуть по логотипу")
    def click_logo(self):
        self.wait_clickable(main_loc.LOGO_LINK).click()
