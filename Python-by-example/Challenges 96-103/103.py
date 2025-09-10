list = {}

for i in range(4):
    name = input("Name: ")
    age = int(input("Age: "))
    shoe = int(input("Shoe size: "))
    list[name] = {"Age":age, "Shoe": shoe}

print(list)

print()


for name in list:
    print(name, list[name]["Age"])