"""
python tests by rusplay 2023 (c)
"""
import os, time, pytest, selenium
from selenium.webdriver.common.by import By
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

    btn = browser.find_element(By.ID, "send")
    assert btn.text == "Отправить", "Wrong Text!!!"
    # assert True, ""


def test_empty_body(browser):
    """
    Description
    """
    browser.get("https://postcard.qa.studio/")

    lbl = browser.find_element(By.CSS_SELECTOR, "div.email h2").get_attribute("class")
    assert lbl == "requered", ""

    lbl_photo = browser.find_element(By.CSS_SELECTOR, ".photo-input__header>h2:nth-child(1)")
    get_class = lbl_photo.get_attribute("class")
    assert get_class == "requered", ""

    lbl_hide_pick = browser.find_element(By.CSS_SELECTOR, "h2.toHide").get_attribute("class")
    assert "toHide" in lbl_hide_pick, "error toHide"

    browser.find_element(By.ID, "send").click()

    lbl = browser.find_element(By.CSS_SELECTOR, "div.email h2").get_attribute("class")
    assert lbl == "requered error", ""

    lbl_photo = browser.find_element(By.CSS_SELECTOR, ".photo-input__header>h2:nth-child(1)")
    get_class = lbl_photo.get_attribute("class")
    assert get_class == "requered error", ""

    lbl_hide_error = browser.find_element(By.CSS_SELECTOR, "h2.toHide").get_attribute("class")
    assert "toHide error" in lbl_hide_error, ""

    cstm_photo = browser.find_element(By.XPATH, "//input[@type='file']")
    cstm_photo.send_keys(os.path.abspath("test_img/OIP.jpg"))
    photo = browser.find_element(By.CSS_SELECTOR, ".photo-input__photo-plus").get_attribute("class")
    assert "hidden" in photo, "wrong class value"


@pytest.mark.xfail(reason="waiting for bug fix...")
@pytest.mark.parametrize("x", [1, 2])
def test_sending(browser, x):
    """
    Description
    """
    # browser = webdriver.Chrome()
    browser.get("https://postcard.qa.studio/")

    ent_em = browser.find_element(By.ID, "email")
    ent_em.click()
    ent_em.send_keys("nikolaenkoruslan011@gmail.com")

    ent_text = browser.find_element(By.ID, "textarea")
    ent_text.click()
    ent_text.send_keys("Hello, World!!!")

    chs_photo = browser.find_element(By.CSS_SELECTOR, f'#photoContainer>div:nth-child({x})')
    chs_photo.click()

    browser.find_element(By.ID, "send").click()

    a = browser.find_element(By.XPATH, "//h3[contains(text(), 'успешно')]").text
    assert a == "Открытка успешно отправлена!"

# 	# Заглушка
# 	# assert True, ""
