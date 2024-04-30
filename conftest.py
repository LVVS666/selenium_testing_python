import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options



capabilities = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android',
    "appPackage": "ru.berizaryad.android.staging",
    "appActivity": "ru.berizaryad.android.presentation.main.DrawerMainActivity",
    'language': 'en',
    'noReset': True,
    'locale': 'US'
}


appium_server_url = 'http://localhost:4723'


@pytest.fixture()
def driver():
        app_driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
        yield app_driver
        if driver:
            app_driver.quit()