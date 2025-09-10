file = open("Names.txt", "a")
file.write(input("Enter a name: "))

file = open("Names.txt", "r")
print(file.read())
