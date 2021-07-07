'''
008 Feladat: Hibakezelés megvalósítása selenium programban
    Készíts egy Python alkalmazást ami selenium-ot használ.
    Nyisson meg egy Chrome böngészöt és töltsön be egy tetszőleges weblapot az Internetről.
    Az oldalon probáld megtalálni a <div id="nemletezik"></div> mezőt.
    A lényeg, hogy hibát dogjon a driver.find_by_id függvény hívás.
    Feladatot, hogy kezed le ezt a hibát és írj ki valami emberileg olvasható üzenetet.
    Extra feladatként készíts egy saját függvényt, ami bármilyen find_by_id lokátor hívásnál lekezeli a nemlétező elem tipusú hibát.
    A megoldáshoz használj python try except struktúrát.

    A megoldást egy seleniumex.py nevű fileban kell beadnod.
'''
import selenium.common.exceptions
from selenium import webdriver

def find_by_id_hibakezeles(id):
    try:
        browser.find_element_by_id(id)
    except selenium.common.exceptions.NoSuchElementException:
        print("Nem található az általad megadott elem.")

try:
    path = ("C:\\Windows\\chromedriver.exe")
    url = "https://www.google.com/"
    browser = webdriver.Chrome(path)

    browser.get(url)
    browser.maximize_window()
    find_by_id_hibakezeles("nemletezik")
except:
    print("Hiba")
finally:
    browser.quit()
