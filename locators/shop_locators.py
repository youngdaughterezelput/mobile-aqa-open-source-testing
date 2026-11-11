from appium.webdriver.common.appiumby import AppiumBy


class ShopLocators:
    PRODUCTS_SCREEN = (AppiumBy.ACCESSIBILITY_ID, "products screen")
    FIRST_IMAGE = (AppiumBy.ANDROID_UIAUTOMATOR,
                   'new UiSelector().className("android.widget.ImageView").instance(4)')
    VIEW_GROUP = (AppiumBy.ANDROID_UIAUTOMATOR,
                  'new UiSelector().className("android.view.ViewGroup").instance(34)')
    SECOND_IMAGE = (AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.ImageView").instance(5)')
    ADD_TO_CART = (AppiumBy.ANDROID_UIAUTOMATOR,
                   'new UiSelector().text("Add To Cart")')
