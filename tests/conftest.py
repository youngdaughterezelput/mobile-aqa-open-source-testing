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
    }
    # При необходимости явно укажите установленное приложение или путь к APK.
    for variable, capability in (
        ("APPIUM_APP", "appium:app"),
        ("APPIUM_APP_PACKAGE", "appium:appPackage"),
        ("APPIUM_APP_ACTIVITY", "appium:appActivity"),
        ("APPIUM_UDID", "appium:udid"),
    ):
        if value := os.getenv(variable):
            capabilities[capability] = value

    options = AppiumOptions().load_capabilities(capabilities)
    session = webdriver.Remote(os.getenv("APPIUM_URL", "http://127.0.0.1:4723"), options=options)
    try:
        yield session
    finally:
        session.quit()
