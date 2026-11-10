from selenium.webdriver.common.by import By

CONSTRUCTOR_LINK = (
    By.XPATH,
    "//a[contains(@class, 'AppHeader_header__link') and @href='/']",
)
ORDER_FEED_LINK = (By.XPATH, "//a[@href='/feed']")
PERSONAL_ACCOUNT_LINK = (By.XPATH, "//a[@href='/account']")
LOGO_LINK = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]/a")

ENTER_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
CHECKOUT_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
CONSTRUCTOR_HEADING = (By.XPATH, "//h1[text()='Соберите бургер']")

BASKET = (By.CSS_SELECTOR, ".BurgerConstructor_basket__29Cd7")

INGREDIENT_CARD = (
    By.XPATH,
    (
        "//a[contains(@class, 'BurgerIngredient_ingredient')"
        " and .//p[contains(@class, 'ingredient__text') and text()='{}']]"
    ),
)
INGREDIENT_NAME = (
    By.XPATH,
    "//p[contains(@class, 'ingredient__text') and text()='{}']",
)

INGREDIENT_COUNTER = (
    By.XPATH,
    (
        "//a[contains(@class, 'BurgerIngredient_ingredient')"
        " and .//p[contains(@class, 'ingredient__text') and text()='{}']]"
        "//p[contains(@class, 'counter_counter__num')]"
    ),
)

MODAL_TITLE = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")
ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow')]")
MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
LOADING_MODAL = (By.XPATH, "//img[contains(@class, 'Modal_modal__loading')]")
