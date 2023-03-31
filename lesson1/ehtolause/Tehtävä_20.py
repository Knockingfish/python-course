# Tehtävä 20
x = int(input ("Give the first integer: "))
y = int(input ("Give the second integer: "))
z = int(input ("Give the third integer: "))

if (x<y and x<z):
    print("First integer is smallest.")
elif (y<x and y<z):
    print("Second integer is smallest.")
elif (z<x and z<y):
    print("Third integer is smallest.")
elif (x==y==z):
    print("All integers are the same.")