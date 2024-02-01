from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


# class MainPageLocators():


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")


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
