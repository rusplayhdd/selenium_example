"""
fixture by rusplay 2023 (c)
"""
import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    """
    basic fixture
    """
    yml_file = open(".github/workflows/Selenium_auto_tests.yaml")

    if "setup-edge@" in yml_file.read():
        chrome_options = webdriver.FirefoxOptions()
    elif "setup-firefox@" in yml_file.read():
        chrome_options = webdriver.EdgeOptions()
    else:
        print("Browser setup ERROR in yml!!!!!!!!!!!")
    yml_file.close()

    chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--headless")

    # p = webdriver.FirefoxService(executable_path="/snap/bin/geckodriver")

    # s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(670, 745)

    # it uses for hard shutdown a browser by unforeseen mistakes
    yield driver
    driver.close()
    driver.quit()
