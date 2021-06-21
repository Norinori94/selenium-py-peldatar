"""
Írj programot, ami kiírja a kisbetűket, és melléjük az karakter kódjukat!
A kiírás több oszlopos legyen, és legfeljebb 10 soros.

Minta:
a 97 f 102 .....
b 98 g 103
c 99 h 104
d 100 i 105
e 101 j 106

A megoldashoz használd a beépített ord() es chr() függvényeket.
"""

# import string
# alph = list(string.ascii_lowercase)

a = ord("a")
alph = [chr(i) for i in range(a, a + 26)]
index = 0
row = 1

for a in alph:
    if index < 1:
        print(alph[index] + " " + str(ord(alph[index])), alph[index+5] + " " + str(ord(alph[index+5])), alph[index+10] + " " + str(ord(alph[index+10])), alph[index+15] + " " + str(ord(alph[index+15])), alph[index+20] + " " + str(ord(alph[index+20])), alph[index+25] + " " + str(ord(alph[index+25])))
        index += 1
    else:
        print(alph[index] + " " + str(ord(alph[index])), alph[index+5] + " " + str(ord(alph[index+5])), alph[index+10] + " " + str(ord(alph[index+10])), alph[index+15] + " " + str(ord(alph[index+15])), alph[index+20] + " " + str(ord(alph[index+20])))
        index += 1
    row += 1
    if row > 5:
        break

