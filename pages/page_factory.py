from components.header import Header
from pages.shop_page import ShopPage


class PageFactory:
    def __init__(self, driver):
        self.driver = driver

    def header(self):
        return Header(self.driver)

    def shop(self):
        return ShopPage(self.driver)
