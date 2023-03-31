Cars = ["Toyota", "Tesla", "Hyundai"]
print(Cars)
l = len(Cars) # Listan pituus on "len".
print("Listassa on " + str(l) + " autoa")
print("Lisätään Honda listaan")
Cars.append("Honda")
print(Cars)
print("Otetaan pois " + Cars[1])
Cars.pop(1)
print(Cars)
print("Käydän listaa läpi for-loopilla")
for x in Cars:
	print(x)
print(Cars[1])