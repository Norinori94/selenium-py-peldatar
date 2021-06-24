'''
Feladat: Selenium weboldal menyitás gyakorlása

A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet. Ezen a néven fogadható el a megoldás.

    Készíts egy Python alkalmazást ami selenium-ot használ. Nyisson meg egy Chrome böngészöt és töltsön be egy tetszőleges weblapot az Internetről.

        A megoldást egy start.py nevű fileban kell beadnod.
'''

from selenium import webdriver

path = "C:\\Windows\\chromedriver.exe"
url = "https://www.google.com/"
browser = webdriver.Chrome(path)

browser.get(url)
browser.quit()

