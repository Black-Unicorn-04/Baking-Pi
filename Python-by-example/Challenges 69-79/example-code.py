# fruit_tuple = ("apple", "banana","strawberry","orange")

# print(fruit_tuple.index("strawberry"))

# print(fruit_tuple[1])




# names_list = ['John', 'Tim', 'Sam']
# print(names_list)

# del names_list[1]

# print(names_list)

# names_list.append(input("Add a name: "))

# print(names_list)

# print(sorted(names_list))

# names_list.append("Johnny")

# names_list.sort()

# print(names_list)


# colours = {1:"red", 2:"blue", 3:"green"}

# print(colours)

# colours[2] = "yellow"

# print(colours)

x = [154,634,892,345,325,23]

print(len(x))

print(x[1:4])

for i in x:
    print(i)

num = int(input("Enter number: "))

# if num in x:
#     print(num,"is in the list")
# else:
#     print("Not in the list")

x.insert(2,420)

x.remove(23)

x.append(999)

print(x)