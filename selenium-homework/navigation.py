'''
017 Feladat: Navigációs feladatok

A feladatokat külön python fileban oldd meg.
Minden feladat tartalmazza az elvárt filenevet. Ezen a néven fogadható el a megoldás.
Készíts egy Python alkalmazást ami selenium-ot használ.
Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
A program töltse be a példatárból az http://localhost:9999/general.html oldalt.
A feladatod, hogy végiglátogassd az összes linket ezen az oldalon.
Egy link meglátogatása akkor érvényes, ha a hozzá tartozó a html elemre rákattintottál, a megjelent új oldalnak ellenrőizted,
hogy eggyezik az urlje az előzőleg használt a tag href-jével és sikeresen vissza navigáltál a főoldalra.
(A tökéletes megoldás nem tartalmaz sor ismétléseket. Ezt mondjuk függvények írásával is elő tudod idézni.)

A megoldást egy navigation.py nevű fileban kell beadnod.
'''

from selenium import webdriver

path = "C:\\Windows\\chromedriver.exe"
url = "http://localhost:9999/general.html"

browser = webdriver.Chrome(path)
browser.get(url)
browser.maximize_window()

anchors = browser.find_elements_by_xpath('//header//small//a')

for a in anchors:
    a.click()

    if a.get_attribute("href").lower() in browser.current_url:
        print("Jó a link.")
    else:
        print("Rossz a link.")

browser.quit()