# William Fabian.

numero = input("Antaa kolme numeroa: ")
laji = input("Anna lajittelu tyypi nouseva (N) tai laskeva (L): ")

sarja = numero.split()
sarja.sort()

if laji=="N":
    sarja.sort()
    print ("Annetut numerot pienimmästä suurimpaan", sarja)
elif laji=="L":
    sarja.sort(reverse=True)
    print ("Annetut numerot suurimmasta pienimpään:", sarja)