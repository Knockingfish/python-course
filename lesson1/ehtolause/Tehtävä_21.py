# Tehtävä 21

v1 = input("Do you drink coffee or tea? ")
s1 = int(input("How many sugar cubes do you take? "))

if v1 == "Coffee":
    if s1 <= 2:
        print("Kahvi kyllä piristää!")
    elif s1 >=3:
        print("Kahvi voi olla aika vahva maku...")
elif v1 == "Tea":
    if s1 <= 2:
        print("Tee usein rauhoittaa!")
    elif s1 >= 3:
        print("Taidat pitää teestäsi makeana?")
else:
    print("Ohjelmassa tapahtunut virhe!")