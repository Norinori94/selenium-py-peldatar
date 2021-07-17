'''
Készíts egy Python alkalmazást ami selenium-ot használ.
Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
A program töltse be a példatárból az http://localhost:9999/editable-table.html oldalt.
A megjelenő táblázatban az alábbi feladatokat kell végrehajtanod:
a) Addj hozzá még két teljsen kitöltött sort. Ellenőrizd, hogy tényleg hozzáadódtak-e a sorok.
b) Ellenőrizd a kereső funkciót.
c) írd át a táblázat egyes celláit és ellenőrizd, hogy megfelelően frissült-e a DOM struktúra.
'''

from selenium import webdriver

def find_table_rows():
    return browser.find_elements_by_xpath('//table/tbody/tr')

def count_table_rows(elements):
    return len(elements)

def fill_row(name, price, quantity, category):
    table_rows = find_table_rows()
    last_row = table_rows[count_table_rows(table_rows) - 1]
    cells = last_row.find_elements_by_xpath('td/input')
    cells[0].send_keys(name)
    cells[1].send_keys(price)
    cells[2].clear()
    cells[2].send_keys(quantity)
    cells[3].send_keys(category)


path = "C://Windows//chromedriver.exe"
url = "http://localhost:9999/editable-table.html"

browser = webdriver.Chrome(path)
browser.get(url)
browser.maximize_window()

table = browser.find_element_by_xpath('//table')
table_rows = find_table_rows()
button_add = browser.find_element_by_xpath('//button[text()="Add"]')
input_name = browser

number_of_rows_default = count_table_rows(table_rows)
button_add.click()
fill_row("test01", "255.49", 10, "TEST")
button_add.click()
fill_row("test02", "45.01", 4, "TEST")

table_rows = find_table_rows()
number_of_rows_after_add = count_table_rows(table_rows)

assert number_of_rows_default <= number_of_rows_after_add

