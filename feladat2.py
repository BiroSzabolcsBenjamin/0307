import random

tipp=str(input("Fej vagy Írás? (nagy kezdőbetűvel írja be): "))
nagy=tipp.upper()
erme=["FEJ","ÍRÁS"]
erme2=erme[random.randint(0,1)]
print("Érme: ",erme2)
if nagy == erme2:
    print("Eltaláltad.")
else:
    print("Ez nem talált.")