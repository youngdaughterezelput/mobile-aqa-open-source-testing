"""Upper panels on My Demo App"""
from selenium.webdriver.support import expected_conditions as EC

from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class Header(BasePage):
    def visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    def open_menu(self):
        self.click(HeaderLocators.MENU)

    def open_sort(self):
        self.click(HeaderLocators.SORT)

    def open_cart(self):
        self.click(HeaderLocators.CART)

    def open_catalog_from_menu(self):
        self.click(HeaderLocators.CATALOG_ITEM)
