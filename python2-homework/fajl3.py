with open("adat.txt", "r", encoding="utf-8") as text_adat:
    text_list = text_adat.readlines()

with open("fajl3.txt", "a", encoding="utf-8") as text_fajl3:
    text_fajl3.write(str(text_list))

