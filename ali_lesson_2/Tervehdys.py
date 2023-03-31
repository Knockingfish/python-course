import MyFunctions as mf
Name = input("Name: ")
Luku1 = int(input("Luku1: "))
Luku2 = int(input("Luku2: "))
Tervehdys = mf.Greeting(Name)
Summa = mf.LaskeYhteen(Luku1, Luku2)
print(Tervehdys, Summa)