import time

import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('link', ["/?promo=offer0",
                                  "/?promo=offer1",
                                  "/?promo=offer2",
                                  "/?promo=offer3",
                                  "/?promo=offer4",
                                  "/?promo=offer5",
                                  "/?promo=offer6",
                                  pytest.param("/?promo=offer8", marks=pytest.mark.xfail),
                                  "/?promo=offer7",
                                  "/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207{link}'
    page = ProductPage(browser, link)
    page.open()
    current_product_price = page.get_product_price()
    current_product_name = page.get_product_name()
    page.click_to_add_to_busket()
    page.solve_quiz_and_get_code()
    page.check_basket_total_in_header(current_product_price)
    page.check_basket_total_in_message_after_product_added(current_product_price)
    page.check_added_product_name_in_message(current_product_name)
