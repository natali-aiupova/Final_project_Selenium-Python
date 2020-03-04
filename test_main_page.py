from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

import pytest

# Метка для запуска тестов класса TestLoginFromMainPage. Чтобы запустить эти тесты нужно добавить "-m login_guest".
@pytest.mark.login_guest
class TestLoginFromMainPage():
    # Проверка, что гость может перейти на страницу логина
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        # Проверка корректности url (страница логина), наличия форм регистрации и входа (реализовано в login_page.py)
        login_page.should_be_login_page()

    # Проверка, что гость видит ссылку на страницу логина
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        # Проверка наличия ссылки на логин (реализовано в base_page.py)
        page.should_be_login_link() 

# Гость открывает главную страницу, переходит в корзину, ожидаем пустую корзину и сообщение об этом 
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_the_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_message_empty_basket()