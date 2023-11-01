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
    # chrome_options = Options()
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("start-maximized")
    # chrome_options.add_argument("--disable-infobars")
    # chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument("--headless")

    # s = Service(ChromeDriverManager().install())
    driver = webdriver.Edge()

    # it uses for hard shot down a browser by unforeseen mistakes
    yield driver
    driver.close()
    driver.quit()
