from math import sqrt

szam=int(input("Írj be egy számot: "))


if szam<=0:
    print("pozitív számmal dolgozz!")
    szam=int(input("Írj be egy új számot: "))
else:
    print("A megadott szám négyzetgyöke: ",round(sqrt(szam),2))