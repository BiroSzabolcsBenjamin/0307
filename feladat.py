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

#4f

#5f