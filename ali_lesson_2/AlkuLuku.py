import MyFunctions as mf
Luku = input("Anna luku: ")
Luku = int(Luku)

(F, P) = mf.IsPrime(Luku)
print(F)
if P:
	print("Luku", Luku, "on alkuluku.")
else:
	print("Luku", Luku, "ei ole alkuluku.")