from .base_page import BasePage

# В классе MainPage у нас не осталось никаких методов, поэтому добавим заглушку
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

# Метод __init__ вызывается при создании объекта. Конструктор выше с ключевым словом super только вызывает конструктор класса предка и передает ему все те аргументы, которые мы передали в конструктор MainPage.