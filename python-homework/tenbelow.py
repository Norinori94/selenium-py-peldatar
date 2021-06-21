"""
Írj programot, mely addig olvas be számokat a billentyűzetről, ameddig azok kisebbek, mint tíz.
Írja ki ezek után a beolvasott számok összegét!
"""

number = 0
add = 0

while number < 10:
    add += number
    number = int(input("Adj meg egy tíznél kisebb számot: "))

print("\nA belolvasott számok összege:", add)