from locators.shop_locators import ShopLocators
from pages.base_page import BasePage


class ShopPage(BasePage):
    def open_first_image(self):
        self.click(ShopLocators.FIRST_IMAGE)

    def select_view_group(self):
        self.click(ShopLocators.VIEW_GROUP)

    def open_second_image(self):
        self.click(ShopLocators.SECOND_IMAGE)

    def add_to_cart(self):
        self.click(ShopLocators.ADD_TO_CART)
