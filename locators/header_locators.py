from appium.webdriver.common.appiumby import AppiumBy


class HeaderLocators:
    MENU = (AppiumBy.ACCESSIBILITY_ID, "open menu")
    SORT = (AppiumBy.ACCESSIBILITY_ID, "sort button")
    CART = (AppiumBy.ACCESSIBILITY_ID, "cart badge")
    LOGO = (AppiumBy.ACCESSIBILITY_ID, "longpress reset app")
    CATALOG_ITEM = (AppiumBy.ACCESSIBILITY_ID, "menu item catalog")
    SORT_OPTIONS = {
        "name_ascending": (AppiumBy.ACCESSIBILITY_ID, "nameAsc"),
        "name_descending": (AppiumBy.ACCESSIBILITY_ID, "nameDesc"),
        "price_ascending": (AppiumBy.ACCESSIBILITY_ID, "priceAsc"),
        "price_descending": (AppiumBy.ACCESSIBILITY_ID, "priceDesc"),
    }
