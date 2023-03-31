while True:
    try:
        x = int(input ("Type a number: "))
        y = int(input ("Type a second number: "))
        break
    except ValueError:
        print ("Please input a number: ")

import random
rand=random.randint(0, 100)

sum=x+y
difference=abs(x-y)
division=int(x/y)
multiplication=x*y
subtraction=sum-rand

#tehtävä8
print("The sum of the given integers:")
print(sum)

#tehtävä9
print("The difference between the given integers:")
print(difference)

#tehtävä10
print("The two integers in their given order:")
print(x, y)

#tehtävä11
print("The first integer divided by the second:")
print(division)

#tehtävä 12
print("The second integer multiplied by the first:")
print(multiplication)

#tehtävä 13
print("The two integers are added, and then a third integer is subtracted from the sum")
print(subtraction)
print("The randomly generated third integer:")
print(rand)