import time
from selenium import webdriver

path = "C:\\Windows\\chromedriver.exe"
url = "http://localhost:9999/trickyelements.html"
browser = webdriver.Chrome(path)
browser.get(url)
browser.maximize_window()

checkbox_random = browser.find_element_by_id("randomized")
checkbox_difficulty = browser.find_element_by_id("difficulty")
element1 = browser.find_element_by_id("element1")
element2 = browser.find_element_by_id("element2")
element3 = browser.find_element_by_id("element3")
element4 = browser.find_element_by_id("element4")
element5 = browser.find_element_by_id("element5")
label_result = browser.find_element_by_id("result")

try:
    element_click = browser.find_elements_by_xpath('//button')[0]
    element_click.click()

    if label_result.text == ''.join((element_click.text, " was clicked")):
        print("Megfelelő eredmény.")
    else:
        print("Rossz eredmény.")
except:
    print("Az oldal nem tartalmaz gombot.")

time.sleep(2)
browser.quit()
