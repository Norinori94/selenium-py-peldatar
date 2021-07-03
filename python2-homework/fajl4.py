with open("adat.txt", "r", encoding="utf-8") as text_adat:
    text_list = text_adat.readlines()

with open("fajl4.txt", "a", encoding="utf-8") as text_fajl4:
    for t in text_list:
        text_fajl4.write(t)

