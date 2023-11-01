"""
fixture
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def browser():
    """
    basic fixture
    """
    chromium_options = webdriver.EdgeOptions()
    chromium_options.add_argument("--no-sandbox")
    # chromium_options.add_argument("start-maximized")
    chromium_options.add_argument("--disable-infobars")
    chromium_options.add_argument("--disable-extensions")
    # chromium_options.add_argument("--headless")

    s = Service(ChromeDriverManager().install())
    driver = webdriver.Edge(options=chromium_options)

    # it uses for hard shot down a browser by unforeseen mistakes
    yield driver
    driver.close()
    driver.quit()
