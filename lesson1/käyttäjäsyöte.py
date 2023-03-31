word = input ("What would you like to print? ")
print (word)

while True:
    try:
        num = int(input ("Type a number: "))
        print (num)
        break
    except ValueError:
        print ("Please input a number: ")
