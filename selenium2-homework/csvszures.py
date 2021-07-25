'''
003 Feladat: Python CSV filekezelés
A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet. Ezen a néven fogadható el a megoldás.
Adott az alábbi csv tartalom
Name,Email,DoB,Phone
Kiss Péter,peter.kiss@sel.hu,1988-12-12,06361 455899
Nagy Ervin,ervin.nagy@sel.hu,1977-01-01,06361 555555
Bella Eszter, eszter.bella@sel.hu,2003-07-07, 06555 555555
Kis Franciska, franciska.kiss@sel.hu,1999-01-20, 06666 666666
Metsd ezt el egy table_in.csv szöveges állományba. Ezzel fogsz dolgozni.

Készíts egy python programot ami a fenti adatfileból készít egy másik adatfájl-t ami csak az emailím és név oszlopokat tartalmazza. Tehát például:
Email,Name
peter.kiss@sel.hu,Kiss Péter
ervin.nagy@sel.hu,Nagy Ervin
....
'''
import csv

with open("table_in.csv", "r", encoding="utf-8") as file_table_in:
    row = csv.reader(file_table_in, delimiter=",")
    for r in row:
        with open("email_and_name.csv", "a", encoding="utf-8") as file_email_and_name:
            file_email_and_name.write(f"{r[1]},{r[0]}\n")