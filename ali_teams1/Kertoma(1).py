# William Fabian.

while True:
    n = int(input("Anna luku väliltä 1 ja 10: "))
    if n in range(1, 11):
        break
    else: 
        quit()

kertoma=1

if n < 0:
    print ("Negatiivisille luvuille ei ole kertomaa.")
elif n == 0:
    print ("Nollan kertoma on 1")
else:
    for i in range(1, n+1):
        kertoma = kertoma*i

print ("Annetun numeron kertoma on:", kertoma)