'''
001 Feladat: Python filekezelés feladatok
Készíts egy Python alkalmazást ami selenium-ot használ.
Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
A program töltse be a példatárból az http://localhost:9999 oldalt.
Lokátorral keresd ki az összes linket az oldalról.
Tárold a memóriában egy listában az összes linket.
A list tartalmát írd ki egy fájlba.
Minden link egy új sorba kerüljön.
A kimenetre írd ki hány linket találtál.
'''

from selenium import webdriver

path = 'C://Windows/chromedriver.exe'
url = 'http://localhost:9999'
browser = webdriver.Chrome(path)

try:
    browser.get(url)
    browser.maximize_window()

    links = browser.find_elements_by_xpath('//a')
    link_list = []

    for l in links:
        link_list.append(l.get_attribute("href"))

    with open("links.text", "w", encoding="utf-8") as link_text:
        for l in link_list:
            link_text.write(l + "\n")

    print("Ennyi linket találtam:", str(len(link_list)))
except:
    print("Valami hiba történt.")
finally:
    browser.quit()