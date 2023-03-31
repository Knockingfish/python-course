a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c = float(input("Enter 3rd number: "))
sorting = input("Sorting order: N/L: ")
numbers = [a, b, c]
if ((sorting == 'N') or (sorting == 'n')):
	numbers.sort()
	print(numbers)
elif ((sorting == 'L') or (sorting == 'l')):
	numbers.sort(reverse = True)
	print(numbers)
else:
	print('Incorrect sorting order')