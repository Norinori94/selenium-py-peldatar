'''
015 Feladat: Selenium adat kinyeréses feladatok

A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet. Ezen a néven fogadható el a megoldás.
Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
A program töltse be a példatárból az http://localhost:9999/todo.html oldalt.
A feladatod, hogy kigyűjtsd az összes jelenleg aktív Todo bejegyzést.
Ha lehet akkor ezt minnél kevesebb selenium lokátorral old meg.
(Tökéletes megoldáshoz csak egy darab find_by hívásra van szükség).
A megoldást egy todos.py nevű fileban kell beadnod.
'''

from selenium import webdriver

path = "C:\\Windows\\chromedriver.exe"
url = "http://localhost:9999/todo.html"

browser = webdriver.Chrome(path)
browser.get(url)
browser.maximize_window()

todos = browser.find_elements_by_xpath('//span[@class = "done-false"]')

for t in todos:
    print(t.text)

browser.quit()