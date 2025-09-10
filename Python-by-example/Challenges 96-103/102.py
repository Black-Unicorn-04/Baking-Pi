list = {}

for i in range(4):
    name = input("Name: ")
    age = int(input("Age: "))
    shoe = int(input("Shoe size: "))
    list[name] = {"Age":age, "Shoe": shoe}

print(list)

ask = input("Name: ")
print(list[ask])