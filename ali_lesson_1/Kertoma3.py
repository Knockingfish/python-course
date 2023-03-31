def Factorial(n):
	if n == 0:
		return 1
	else:
		return n * Factorial(n-1)

Luku = int(input("Luku: "))
K = Factorial(Luku)
print(K)