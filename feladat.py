import random

#1f

#2f
tipp=str(input("fej vagy írás? : "))
erme=["Fej","Írás","fej","írás"]
erme2=erme[random.randint(0,3)]
print("Érme: ",erme2)
if tipp == erme :
    print("Eltaláltad.")
else:
    print("Ez nem talált.")
#3f
szam=int(input("írj be egy számot: "))
Lszam=[]
while szam!="":
    Lszam.append(szam)
    print("Számok összege: ",sum(Lszam))
    szam=int(input("írj be egy számot: "))

#4f

#5f