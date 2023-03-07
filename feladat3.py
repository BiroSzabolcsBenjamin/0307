szam=int(input("írj be egy számot: "))
Lszam=[]
while szam!="":
    Lszam.append(szam)
    print("Számok összege: ",sum(Lszam))
    szam=int(input("írj be egy számot: "))