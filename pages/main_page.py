from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage

# В классе MainPage у нас не осталось никаких методов, поэтому добавим заглушку
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)