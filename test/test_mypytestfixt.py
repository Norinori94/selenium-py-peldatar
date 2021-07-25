import pytest as pytest
from selenium import webdriver
from selenium.webdriver import ActionChains


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome("C://Windows//chromedriver.exe")
    driver.maximize_window()
    driver.get("http://localhost:9999/alert_playground.html")
    return driver

def test_alert_button_ok(browser):
    browser.find_element_by_xpath('//input[@name="alert"]').click()
    alert_pop = browser.switch_to.alert
    assert alert_pop.text == "I am alert"
    alert_pop.accept()

def test_confirmation_box_ok(browser):
    browser.find_element_by_xpath('//input[@name="confirmation"]').click()
    alert_pop = browser.switch_to.alert
    assert alert_pop.text == "I am confirm"
    alert_pop.accept()

def test_confirmation_box_megse(browser):
    browser.find_element_by_xpath('//input[@name="confirmation"]').click()
    alert_pop = browser.switch_to.alert
    assert alert_pop.text == "I am confirm"
    alert_pop.dismiss()

def test_prompt_megse(browser):
    browser.find_element_by_xpath('//input[@name="prompt"]').click()
    alert_pop = browser.switch_to.alert
    assert (alert_pop.text == "I am prompt")
    alert_pop.send_keys("Teszt")
    alert_pop.dismiss()
    assert browser.find_element_by_id("demo").text == ""

def test_prompt_ok(browser):
    browser.find_element_by_xpath('//input[@name="prompt"]').click()
    alert_pop = browser.switch_to.alert
    alert_pop.send_keys("Teszt")
    alert_pop.accept()
    assert browser.find_element_by_id("demo").text == "You entered: Teszt"

def test_prompt_ok_fail(browser):
    browser.find_element_by_xpath('//input[@name="prompt"]').click()
    alert_pop = browser.switch_to.alert
    alert_pop.send_keys("Teszt")
    alert_pop.accept()
    assert browser.find_element_by_id("demo").text == "You entered: Teszt fail"

def test_double_click_me_ok(browser):
    action = ActionChains(browser)
    action.double_click(on_element=browser.find_element_by_id("double-click"))
    action.perform()
    alert_pop = browser.switch_to.alert
    assert alert_pop.text == "You double clicked me!!!, You got to be kidding me"
    alert_pop.accept()
