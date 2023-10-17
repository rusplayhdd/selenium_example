"""
Discription
"""	
from selenium.webdriver.common.by import By


def test_example(browser):
	"""
	Description
	"""
	browser.get("https://postcard.qa.studio/")

	browser.find_element(By.ID, value="send")
	assert btn.text == "Отправить", ""


def test_emptyBody(browser):
	"""
	DescriptionF
	"""
	browser.get("https://postcard.qa.studio/")


	lbl = browser.find_element(By.CSS_SELECTOR, 
		value="div.email h2").get_attribute("class")
	assert lbl == "requered", ""

	
	browser.find_element(By.ID, value="send").click()


	lbl = browser.find_element(By.CSS_SELECTOR, 
		value="div.email h2").get_attribute("class")
	assert lbl == "requered error", ""


@pytest.mark.parametrize("x", [(0), (1)])

def test_Sending(browser, x):
	"""
	Description
	"""
	browser.get("https://postcard.qa.studio/")	
	

	browser.find_element(By.ID, value="email").click().
		send_keys("nikolaenkoruslan@mail.ru")
	
	browser.find_element(By.ID, value="textarea").click().
		send_keys("Hello, World!!!")

	browser.find_element(By.CSS_SELECTOR0, value='[class*="photo-parent"]').
		[x]click().
			 send_keys("Hello, World!!!")	

	browser.find_element(By.ID, value="send").click()

	a = browser.find_element(By.ID, value="modal").text
	assert a == "открытка успешно отправлена!"

	# Заглушка 
	# assert True, ""