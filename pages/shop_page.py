from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class ShopPage(BasePage):
    # Временные локаторы из Appium Inspector: instance зависит от дерева экрана.
    FIRST_IMAGE = (AppiumBy.ANDROID_UIAUTOMATOR,
                   'new UiSelector().className("android.widget.ImageView").instance(4)')
    VIEW_GROUP = (AppiumBy.ANDROID_UIAUTOMATOR,
                  'new UiSelector().className("android.view.ViewGroup").instance(34)')
    SECOND_IMAGE = (AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.ImageView").instance(5)')
    ADD_TO_CART = (AppiumBy.ANDROID_UIAUTOMATOR,
                   'new UiSelector().text("Add To Cart")')

    def open_first_image(self):
        self.click(self.FIRST_IMAGE)

    def select_view_group(self):
        self.click(self.VIEW_GROUP)

    def open_second_image(self):
        self.click(self.SECOND_IMAGE)

    def add_to_cart(self):
        self.click(self.ADD_TO_CART)
