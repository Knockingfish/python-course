InputFilePath = "DataQualityInput1.txt"

ifh = open(InputFilePath, "r")
List = []
for line in ifh:
	if line == "\n":
		List.append(None)
	else:
		List.append(int(line))
print(List)
#Testataan
Total = len(List)
if Total == 0:
	print("No input")
	quit()
Null = 0; NonNull = 0; Duplicate = 0; Distinct = 0; NonUnique= 0; Unique = 0;
#Testataan
for l in List:
	if l == None:
		Null = Null + 1 #kasvatetaan laskuri
T = []
for l in List:
	if l != None:
		T.append(l)
List = T
print(List)
#Testataan
l1 = len(List)
NonNull = l1
if NonNull != 0:
	Set = set(List)
	l2 = len(Set)
	Distinct = l2
	Duplicate = l1 - l2
	for x in List:
		if List.count(x) == 1:
			Unique = Unique + 1
NonUnique = Distinct - Unique
#Testataan
DQA = "Data Quality Analysis"
T = "Total"
N = "  Null"
Nn = "  NonNull"
Dup = "    Duplicate"
Dis = "    Distinct"
Nunq = "      NonUnique"
Unq = "      Unique"

print(l)
print(f"{DQA:10}'\t{'Count':>5}\t{'%':>5}")
print(f"{T:10}\t\t{Total:5d}\t{(Total/Total)*100:5.0f}")
#Testataan
print(f"{N:10}\t\t{Null:5d}\t{(Null/Total)*100:5.0f}")
print(f"{Nn:10}\t\t{NonNull:5d}\t{(NonNull/Total)*100:5.0f}")
print(f"{Dup:10}\t\t{Duplicate:7d}\t{(Duplicate/Total)*100:7.0f}")
print(f"{Dis:10}\t\t{Distinct:7d}\t{(Distinct/Total)*100:7.0f}")
print(f"{Unq:10}\t\t{Unique:9d}{(Unique/Total)*100:9.0f}")
print(f"{Nunq:10}\t\t{NonUnique:9d}{(NonUnique/Total)*100:9.0f}")

# 1, 2, 3, 4, 5, 6, 7, 8, Null, 1
# Total = Null + NonNull; 10 = 1 + 9
# NonNull = Duplicate + Distinct; 9 = 1 + 8
# Distinct = NonUnique + Unique; 8 = 1 + 7