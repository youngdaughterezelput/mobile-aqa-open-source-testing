import os

import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions


@pytest.fixture
def driver():
    capabilities = {
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:deviceName": os.getenv("APPIUM_DEVICE_NAME", "Android Emulator"),
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True,
        "appium:noReset": True,
        "appium:forceAppLaunch": True,
    }
    for variable, capability in (
        ("APPIUM_APP", "appium:app"),
        ("APPIUM_APP_PACKAGE", "appium:appPackage"),
        ("APPIUM_APP_ACTIVITY", "appium:appActivity"),
        ("APPIUM_UDID", "appium:udid"),):
        if value := os.getenv(variable):
            capabilities[capability] = value

    if not os.getenv("APPIUM_APP") and not os.getenv("APPIUM_APP_PACKAGE"):
        capabilities["appium:appPackage"] = "com.saucelabs.mydemoapp.rn"

    options = AppiumOptions().load_capabilities(capabilities)
    session = webdriver.Remote(os.getenv("APPIUM_URL", "http://127.0.0.1:4723"), options=options)
    try:
        yield session
    finally:
        session.quit()

@pytest.fixture
def pages(driver):
    from pages.page_factory import PageFactory

    return PageFactory(driver)
