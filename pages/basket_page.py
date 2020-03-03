from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):

    # Проверка, что корзина пуста
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_ITEMS), \
           "There are items in the basket, but should be not"

    # Проверка, что есть cообщение о том, что корзина пуста
    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasePageLocators.BASKET_MESSAGE), \
           "The basket is not empty, but should be"