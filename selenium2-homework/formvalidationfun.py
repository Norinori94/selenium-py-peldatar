'''
017 Feladat: komplett űrlap tesztelés
Készíts egy Python alkalmazást ami selenium-ot használ.
Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
A program töltse be a példatárból az http://localhost:9999/simplevalidation.html oldalt.
A tanultak alapján teszteld le az űlap mező ellőnőrző funkcióit.
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def input_validation(id):
    element = browser.find_element_by_id(id)
    element.send_keys(Keys.TAB)
    message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH,
                                          f'//input[@id="{id}"]/../../div[@class="validate-input form-field-invalid form-field-invalid-focusout"]'))).get_attribute(
        "textContent")
    assert (message == "Please enter an e-mail")


path = "C://Windows//chromedriver.exe"
url = "http://localhost:9999/simplevalidation.html"
browser = webdriver.Chrome(path)

browser.get(url)
browser.maximize_window()

input_validation("test-email")
input_validation("test-password")
input_validation("test-confirm-password")
input_validation("test-customer-number")
input_validation("test-dealer-number")
input_validation("test-random-field")  # Nem kötelező megadni
input_validation("test-date-field")
input_validation("test-url-field")  # Nem kötelező megadni
input_validation("test-random-textarea")
input_validation("test-card-number")
input_validation("test-card-cvv")
