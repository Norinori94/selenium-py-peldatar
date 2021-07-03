with open("adat.txt", "r", encoding="utf-8") as text_adat:
    for t in text_adat.read():
        with open("fajl5.txt", "a", encoding="utf-8") as text_fajl5:
            text_fajl5.write(t)