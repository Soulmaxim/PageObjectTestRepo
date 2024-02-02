from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            f'Empty basket message is not present for a given timeout'

    def check_text_of_empty_basket_message(self):
        empty_message_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text.split(".")[0]
        assert empty_message_text == "Your basket is empty", f'Empty basket message is not correct. Actual:" {empty_message_text}"'

    def should_not_be_basket_list(self):
        assert self.is_not_element_present(*BasketPageLocators.LIST_OF_PRODUCTS), \
            f'List of products is present'
