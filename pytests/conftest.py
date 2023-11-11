"""
fixture
"""
import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    """
    basic fixture
    """
    chrome_options = webdriver.FirefoxOptions()
    chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument("--headless")

    # s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(780, 710)
    
    # it uses for hard shot down a browser by unforeseen mistakes
    yield driver
    driver.close()
    driver.quit()
