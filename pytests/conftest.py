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
	# It's chrome set up
	chrome_options = Options()
	chrome_options.add_argument("--no-sandbox")
	chrome_options.add_argument("start-maximized")
	chrome_options.add_argument("--disable-infobars")
	chrome_options.add_argument("--disable-extensions")
	# chrome_options.add_argument("--headless")
	
	# use for autoupdate the driver:
	service = Service(ChromeDriverManager().install())
	
	# It'll call the browser: 
	driver = webdriver.Chrome(service=service, options=chrome_options)

	# it uses for hard shot down a browser by unforseen mistakes
	yield driver
	driver.quit()
