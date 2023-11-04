"""
Discription
"""
import os
from selenium.webdriver.common.by import By
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


# @pytest.mark.xfail(reason="waiting for bug fix...")
def test_example(browser):
    """
    Description
    """
    browser.get("https://postcard.qa.studio/")

    btn = browser.find_element(By.ID, value="send")
    assert btn.text == "Отправить", "Wrong Text!!!"
    # assert True, ""


def test_empty_body(browser):
    """
    Description
    """
    browser.get("https://postcard.qa.studio/")

    lbl = browser.find_element(By.CSS_SELECTOR, value="div.email h2").get_attribute("class")
    assert lbl == "requered", ""
    browser.find_element(By.ID, value="send").click()
    lbl = browser.find_element(By.CSS_SELECTOR, value="div.email h2").get_attribute("class")
    assert lbl == "requered error", ""

    cstm_photo = browser.find_element(By.XPATH, value="//input[@type='file']")
    cstm_photo.send_keys(f"{os.getcwd()}/OIP.jpg")
    photo = browser.find_element(By.CSS_SELECTOR, value=".photo-input__photo-plus").get_attribute("class")
    assert photo == "photo-input__photo photo-input__photo-plus toHide hidden", "wrong class value"


@pytest.mark.xfail(reason="waiting for bug fix...")
@pytest.mark.parametrize("x", [1, 2])
def test_sending(browser, x):
    """
    Description
    """
    # browser = webdriver.Chrome()
    browser.get("https://postcard.qa.studio/")

    ent_em = browser.find_element(By.ID, value="email")
    ent_em.click()
    ent_em.send_keys("nikolaenkoruslan011@gmail.com")

    ent_text = browser.find_element(By.ID, value="textarea")
    ent_text.click()
    ent_text.send_keys("Hello, World!!!")

    chs_photo = browser.find_element(By.CSS_SELECTOR, value=f'#photoContainer>div:nth-child({x})')
    chs_photo.click()

    browser.find_element(By.ID, value="send").click()

    a = browser.find_element(By.XPATH, value="//h3[contains(text(), 'успешно')]").text
    assert a == "Открытка успешно отправлена!"

# 	# Заглушка
# 	# assert True, ""
