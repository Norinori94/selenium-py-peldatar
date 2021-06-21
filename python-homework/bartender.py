"""
Kérd be a felhasználó életkorát, és kérdezd meg, mit iszik.
Kétféle italt ismerünk: sör és kóla.
Ha a felhasználó kiskorú, és sört kér, akkor közöld vele, hogy sajnos nem adhatsz neki.
Ha a felhasználó 60 feletti, és kólát kér, akkor közöld vele, hogy a koffein megemelheti a vérnyomását.
Ha ismeretlen italt adott meg, akkor írd ki, hogy csak sört és kólát tudunk adni.
Minden más esetben szolgáld ki.
(Írd ki pl. "Parancsoljon, a söre." vagy "Parancsoljon,a kólája.")
"""

age = int(input("Hány éves vagy? "))
drink = input("Mit szeretnél inni? " )

if age < 18 and (drink == "sört" or drink == "Sört"):
    print("Mivel kiskorú vagy, sajnos nem kaphatsz sört.")
elif age >= 60 and (drink == "kólát" or drink == "Kólát"):
    print("A koffein megemelheti a vérnyomásod.")
elif drink != "sört" and drink != "Sört" and drink != "kólát" and drink != "Kólát":
    print("Csak sört és kólát tudunk adni.")
else:
    if drink == "sört" or drink == "Sört":
        print("Parancsolj, a söröd.")
    else:
        print("Parancsolj, a kólád.")