Kieli = int(input("1. Suomi, 2. English, 3. Español: "))
PromptiLista = ["Kokonaisluku: ", "Integer: ", "Numero Entero: "]
ViestiLista = ["Summa on ", "The sum is ", "La suma es "]
n1 = int(input('1. ' + PromptiLista[Kieli-1]))
n2 = int(input('2. ' + PromptiLista[Kieli-1]))
n3 = int(input('3. ' + PromptiLista[Kieli-1]))
s = n1 + n2 + n3
print(ViestiLista[Kieli-1] + str(s) + ".")