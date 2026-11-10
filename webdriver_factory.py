from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class WebdriverFactory:
    @staticmethod
    def get_webdriver(browser_name):
        browser_name = browser_name.lower()
        if browser_name == "chrome":
            options = ChromeOptions()
            options.add_argument("--window-size=1440,1200")
            return webdriver.Chrome(options=options)
        if browser_name == "firefox":
            options = FirefoxOptions()
            return webdriver.Firefox(options=options)
        raise ValueError(f"Неподдерживаемый браузер: {browser_name}")
