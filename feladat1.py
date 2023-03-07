n=int(input("Hány évig szeretne kamatoztatni: "))
x=int(input("Mekkora összeget szeretne kamatoztatni(Ft): "))
lekotes=int(input("Lekötés kamata: "))

print(n,"év után",round(x*(1+5/100)**n),"Ft-t kaphatunk a betéteink után.")