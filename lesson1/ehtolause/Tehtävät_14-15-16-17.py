# Tehtävä 17
while True:
    try:
        x = int(input("Input a positive integer: "))
        if x < 0:
            print ("Input a positive integer.")
            continue
        elif x == 0:
            print ("Input a positive integer.")
            continue
        break
    except:
        print ("The given value is not an integer!")

# Tehtävä 14
if (x % 2) == 0:
    print (("The given integer"), x, ("is even."))
elif (x % 2) > 0:
    print (("The given integer"), x, ("is odd."))

# Tehtävä 15, Tehtävä 16
if x > 10:
    print (("The given integer"), x, ("is greater than 10."))
elif x < 10:
    print (("The given integer"), x, ("is less than 10."))
elif x == 10:
    print ("Täysin kumpi!")