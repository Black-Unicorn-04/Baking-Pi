list = {}

for i in range(4):
    name = input("Name: ")
    age = int(input("Age: "))
    shoe = int(input("Shoe size: "))
    list[name] = {"Age":age, "Shoe": shoe}

print(list)

rem = input("Who do you want to remove?: ")

del list[rem]

print(list)