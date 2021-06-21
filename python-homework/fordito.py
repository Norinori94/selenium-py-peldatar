"""
Írj egy Python programot, amely a felhasználótól pozitív számokat kér be mindaddig, amíg a felhasználó nullát nem ad be!
A program az összes értéket tárolja egy listában, majd írja ki a képernyőre a lista elemeit fordított sorrendben!
"""

number = int(input("Kérlek adj meg egy pozitív, egész számot: "))
list = [number]

while list[len(list)-1] != 0:
    number = int(input("Kérlek adj meg egy számot: "))
    list.append(number)

list.reverse()
print("A lista összes eleme:", list)
