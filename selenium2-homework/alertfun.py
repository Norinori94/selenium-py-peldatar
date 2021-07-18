'''
015 Feladat: felugró ablakok és tabok kezelése
Készíts egy Python alkalmazást ami selenium-ot használ.
Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
A program töltse be a példatárból az http://localhost:9999/alert_playground.html oldalt.
A tanultak alapján az összes alert funkcióra írj selenium kódot.
A prompt-nál teszteld le a be, hogy a beírt érték megjelenik-e egy paragraf tagben, miután eltűnt az alert.
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


def alert(button):
    button.click()
    return browser.switch_to.alert


path = "C://Windows//chromedriver.exe"
url = "http://localhost:9999/alert_playground.html"
browser = webdriver.Chrome(path)

try:
    browser.get(url)
    browser.maximize_window()

    button_alert = browser.find_element_by_xpath('//input[@name="alert"]')
    button_confirmation = browser.find_element_by_xpath('//input[@name="confirmation"]')
    button_prompt = browser.find_element_by_xpath('//input[@name="prompt"]')
    button_double_click = browser.find_element_by_id("double-click")
    div_text = browser.find_element_by_id("demo")

    # Alert button - OK
    alert_pop = alert(button_alert)
    assert (alert_pop.text == "I am alert")
    alert_pop.accept()

    # Confirmation Box - OK
    alert_pop = alert(button_confirmation)
    assert (alert_pop.text == "I am confirm")
    alert_pop.accept()

    # Confirmation Box - Mégse
    alert_pop = alert(button_confirmation)
    assert (alert_pop.text == "I am confirm")
    alert_pop.dismiss()

    # Prompt - Mégse
    alert_pop = alert(button_prompt)
    assert (alert_pop.text == "I am prompt")
    alert_pop.send_keys("Teszt")
    alert_pop.dismiss()
    assert (div_text.text == "")

    # Prompt - OK
    alert_pop = alert(button_prompt)
    assert (alert_pop.text == "I am prompt")
    alert_pop.send_keys("Teszt")
    alert_pop.accept()
    assert (div_text.text == "You entered: Teszt")

    # Double Click Me - OK
    action = ActionChains(browser)
    action.double_click(on_element=button_double_click)
    action.perform()
    alert_pop = browser.switch_to.alert
    assert (alert_pop.text == "You double clicked me!!!, You got to be kidding me")
    alert_pop.accept()
except:
    print("Something went wrong.")
finally:
    browser.quit()
