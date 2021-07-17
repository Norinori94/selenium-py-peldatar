'''
009 Feladat: selenium dátum mezők gyakorlása
A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet. Ezen a néven fogadható el a megoldás.
Készíts egy Python alkalmazást ami selenium-ot használ.
Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
A program töltse be a példatárból az http://localhost:9999/forms.html oldalt.
Koncentrálj a dátum mezőkre.
A célod, hogy ezeket a dátum és idő értékekete selenium segítségével automatikusan beállítsd:
'''
import calendar

from selenium import webdriver
from datetime import datetime, date, timezone, time

path = "C:\\Windows\\chromedriver.exe"
url = "http://localhost:9999/forms.html"

browser = webdriver.Chrome(path)
browser.get(url)
browser.maximize_window()

input_date = browser.find_element_by_id("example-input-date")
input_date_time = browser.find_element_by_id("example-input-date-time")
input_date_time_local = browser.find_element_by_id("example-input-date-time-local")
input_month = browser.find_element_by_id("example-input-month")
input_week = browser.find_element_by_id("example-input-week")
input_time = browser.find_element_by_id("example-input-time")

input_date.send_keys(datetime(2021, 6, 5).strftime("%Y%m%d"))
input_date_time.send_keys(str(datetime(2012, 5, 5, 5, 5, 5, 555).strftime("%Y. %m. %d. %H:%M:%S:")))
input_date_time.send_keys(str(datetime(2012, 5, 5, 5, 5, 5, 555).strftime("%f")[-3:]))
input_date_time_local.send_keys(datetime(2000, 5, 12, 12, 1).strftime("%Y%m%d %H:%M"))
input_month.send_keys(datetime(1995, 12, 5).strftime("%Y:%B"))
input_week.send_keys(datetime(2015, 12, 22).strftime("%V%Y"))
input_time.send_keys(time(12, 25).strftime("%H:%M"))
# browser.quit()