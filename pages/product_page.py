from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    # Добавление товара в корзину.
    def add_product_to_cart(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        button_add_to_basket.click()

    # Вызываем проверки.
    def should_be_correct_add_product_to_cart(self):
        self.should_be_correct_product_name()
        self.should_be_correct_product_price()

    # Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
    def should_be_correct_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MESSAGE).text
        assert product_name == product_name_message, \
            f"The add product name '{product_name_message}' is not correct. Should be '{product_name}"

    # Стоимость корзины совпадает с ценой товара. 
    def should_be_correct_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_MESSAGE).text
        assert product_price == product_price_message, \
            f"The price of add product '{product_price_message}' is not correct. Should be '{product_price}"

    # Проверка, что элемент не появляется на странице
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    # Проверка, что элемент исчезает
    def should_be_out_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is not disappeared, but should be"