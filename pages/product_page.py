import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def get_product_name(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return name

    def get_product_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return price

    def click_to_add_to_busket(self):
        add_to_busket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON_LINK)
        add_to_busket_button.click()

    def check_basket_total_in_header(self, expected_money):
        basket_total = \
            self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_HEADER).text.split("\n")[0].split(" ")[-1]
        assert basket_total == expected_money, \
            f'Fact basket total: {basket_total} is not equal to expected money: {expected_money}. Link: {self.browser.current_url}'

    def check_basket_total_in_message_after_product_added(self, expected_money):
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text
        assert basket_total == expected_money, \
            f'Fact basket total: {basket_total} is not equal to expected money: {expected_money}. Link: {self.browser.current_url}'

    def check_added_product_name_in_message(self, expected_name):
        fact_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME_ADDED_MESSAGE).text
        assert fact_name == expected_name, \
            f'Fact product name: {fact_name} is not equal to expected name: {expected_name}. Link: {self.browser.current_url}'

    def should_not_be_success_message(self):
        assert not self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_AFTER_ADD_TO_BASKET), \
            f'Success message is not present for a given timeout'

    def should_be_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_AFTER_ADD_TO_BASKET), \
            f'Success message is not disappeared for a given timeout'
