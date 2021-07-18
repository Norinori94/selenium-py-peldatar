'''
021 Feladat: Lapozó kontrol feladatok
Készíts egy Python alkalmazást ami selenium-ot használ.
Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
A program töltse be a példatárból az http://localhost:9999/pagination.html oldalt.
Mentsd le az összes kontaktot az oldalról akinek a keresztneve (First Name) A betüvel kezdődik.
A kiválasztott kontaktok összes adatát mentsd le memóriába egy szotár (dict) struktúrába.
Amikor megvagy az összes adatot mentsd ki egy CSV file-ba.
'''
import csv

from selenium import webdriver

path = "C://Windows//chromedriver.exe"
url = "http://localhost:9999/pagination.html"
browser = webdriver.Chrome(path)

try:
    browser.get(url)
    browser.maximize_window()

    result_list = []

    while True:
        table = browser.find_element_by_xpath('//table[@id="contacts-table"]/tbody')
        rows = browser.find_elements_by_xpath('//table[@id="contacts-table"]/tbody/tr')
        for r in rows:
            row = {}
            cells = r.find_elements_by_tag_name("td")

            if cells[1].text[0] == "A":
                row["id"] = cells[0].text
                row["First name"] = cells[1].text
                row["Second name"] = cells[2].text
                row["Surname"] = cells[3].text
                row["Second Surname"] = cells[4].text
                row["Birth date"] = cells[5].text
                result_list.append(row)

        button_next = browser.find_element_by_id("next")
        if button_next.is_enabled():
            button_next.click()
        else:
            break
    try:
        with open("pagination.csv", "w", encoding="utf-8") as csv_file:
            csv_header = ["id", "First name", "Second name", "Surname", "Second Surname", "Birth date"]
            writer = csv.DictWriter(csv_file, fieldnames=csv_header)
            writer.writeheader()
            for r in result_list:
                writer.writerow(r)
    except:
        print("Something wrong.")
except:
    print("Somehing wrong.")
finally:
    browser.quit()
