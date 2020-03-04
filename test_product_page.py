import pytest
import time

from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage

# Гость может добавить товар в корзину и проверка корректности добавления товара (название, цена)
@pytest.mark.need_review
@pytest.mark.parametrize("link", ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_cart() # реализовано в product_page.py
    product_page.solve_quiz_and_get_code() # Введение капчи (реализовано в base_page.py)
    product_page.should_be_correct_add_product_to_cart() # реализовано в product_page.py

# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_cart()
    product_page.should_not_be_success_message() # реализовано в product_page.py
 
# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
def test_guest_cant_see_success_message(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message() # реализовано в product_page.py
 
# Проверяем, что нет сообщения об успехе с помощью is_disappeared
@pytest.mark.xfail 
def test_message_disappeared_after_adding_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_cart()
    product_page.should_be_out_success_message() # реализовано в product_page.py

# Гость видит ссылку перехода на страницу логина
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link() # реализовано в base_page.py

# Гость может перейти на страницу логина с любой страницы
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser): 
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page() # реализовано в base_page.py

# Гость открывает главную страницу, переходит в корзину, ожидаем пустую корзину и сообщение об этом 
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_the_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_message_empty_basket() # реализовано в basket_page.py

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # фикстура setup (открывает страницу регистрации, регистрирует нового пользователя, проверяет, что пользователь залогинен
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        user_email = str(time.time()) + "@fakemail.org"
        user_password = str(time.time())
        page.register_new_user(user_email, user_password)
        page.should_be_authorized_user() # реализовано в base_page.py

    # Проверка, что пользователь не видит сообщение об успехе
    def test_user_cant_see_success_message(self, browser): 
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message() # реализовано в product_page.py

    # Проверка, что пользователь может добавить товар в корзину
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_product_to_cart()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_correct_add_product_to_cart() # реализовано в product_page.py