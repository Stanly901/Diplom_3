import pytest
from selenium import webdriver

class WebdriverFactory:
    @staticmethod
    def get_webdriver(browser_name):
        if browser_name == "firefox":
            return webdriver.Firefox()
        elif browser_name == "chrome":
            return webdriver.Chrome()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Выбор браузера: 'chrome' или 'firefox'."
    )

@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    driver = WebdriverFactory.get_webdriver(browser_name)
    driver.maximize_window()
    yield driver
    driver.quit()
