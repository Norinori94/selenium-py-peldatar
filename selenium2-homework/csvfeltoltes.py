'''
006 Feladat: Űrlap automatizálás fájlból
Készíts egy Python alkalmazást ami selenium-ot használ.
Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
A program töltse be a példatárból az http://localhost:9999/another_form.html oldalt.
A program segítségével olvassd be a csv tartalmat.
A feladatod, hogy az oldalon található formanyomtatvány segítségével feltöltsd a táblázatot.
Használd a Python CSV könyvtárát.
A feltöltött táblázatot ellenőrizheted ha a probramod letölti a táblázat alatti gomb segítségével az aktuális tartalmat.
Hasonlítsd össze python kódból a kapott file-t, hogy identikus-e az eredetivel.
'''

import csv
import time
from selenium import webdriver

def send_keys(element, string):
    return element.send_keys(string.strip())

path = "C:\\Windows\\chromedriver.exe"
url = "http://localhost:9999/another_form.html"
browser = webdriver.Chrome(path)

try:
    browser.get(url)
    browser.maximize_window()

    input_name = browser.find_element_by_id("fullname")
    input_email = browser.find_element_by_id("email")
    input_DoB = browser.find_element_by_id("dob")
    input_phone = browser.find_element_by_id("phone")
    btn_kuldes = browser.find_element_by_id("submit")

    with open("table_in.csv", "r", encoding="utf-8") as csv_file:
        row = csv.reader(csv_file, delimiter=",")
        next(row)
        for r in row:
            send_keys(input_name, r[0])
            send_keys(input_email, r[1])
            send_keys(input_DoB, r[2])
            send_keys(input_phone, r[3])
            btn_kuldes.click()

            input_name.clear()
            input_email.clear()
            input_DoB.clear()
            input_phone.clear()
except:
    print("Valami hiba történt.")
finally:
    time.sleep(2)
    browser.quit()