'''
013 Feladat: Lokátorok gyakorlása
    Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
    A program töltse be a példatárból az http://localhost:9999/kitchensink.html oldalt.
    Gyakorlás képpen keress ki elemekt a képernyőről az alábbi kritériumoknak megfelelően:
        ID alapján
        NAME alapján
        XPath kifejezésse
    Minden megtalált elemnek irassd ki a text értékét, vagy egy attribútum értékét.
    A megoldást egy locators.py nevű fileban kell beadnod.
'''


from selenium import webdriver

path = "C:\\Windows\\chromedriver.exe"
url = "http://localhost:9999/kitchensink.html"

browser = webdriver.Chrome(path)
browser.maximize_window()
browser.get(url)

radio_button_bmw = browser.find_element_by_id("bmwradio")
input_hide_show = browser.find_element_by_name("show-hide")
button_mouse_hover = browser.find_element_by_xpath('//button[@id="mousehover"]')
button_open_window = browser.find_element_by_id("openwindow")
radio_button_honda = browser.find_elements_by_xpath('//input')[2]

print(radio_button_bmw.get_attribute("value"))
print(radio_button_bmw.get_attribute("name"))
print(radio_button_bmw.get_attribute("type"))
print("")
print(input_hide_show.get_attribute("name"))
print(input_hide_show.get_attribute("class"))
print(input_hide_show.get_attribute("placeholder"))
print(input_hide_show.get_attribute("type"))
print("")
print(button_mouse_hover.get_attribute("class"))
print(button_mouse_hover.text)
print("")
print(button_open_window.get_attribute("class"))
print(button_open_window.get_attribute("onclick"))
print(button_open_window.text)
print("")
print(radio_button_bmw.get_attribute("value"))
print(radio_button_bmw.get_attribute("name"))
print(radio_button_bmw.get_attribute("type"))

browser.quit()