from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_fake_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")
    BASKET_LINK_INVALID = (By.CSS_SELECTOR, "#basket_fake_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


# class MainPageLocators():


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")
    REGISTRATION_EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='registration-email']")
    REGISTRATION_PASSWORD1_INPUT = (By.CSS_SELECTOR, "input[name='registration-password1']")
    REGISTRATION_PASSWORD2_INPUT = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON_LINK = (By.CSS_SELECTOR, "#add_to_basket_form>button")
    BASKET_TOTAL_HEADER = (By.CSS_SELECTOR, ".basket-mini")
    BOOK_NAME_ADDED_MESSAGE = (By.CSS_SELECTOR, "#messages>div:first-child strong")
    QUALIFIES_FOR_BENEFIT_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(2) div")
    ADDED_TO_BASKET_FULL_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(3) p:first-child")
    SUCCESS_MESSAGE_AFTER_ADD_TO_BASKET = (By.CSS_SELECTOR, ".alert-success:first-child")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(3) p:first-child>strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p:nth-child(2)")


class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")
    LIST_OF_PRODUCTS = (By.CSS_SELECTOR, ".content_inner")
