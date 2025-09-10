#NOTES
# 
# Once a tuple is defined you cannot change what is stored in it.

#The contents of a list can be changed while the program is 
# running and lists are one of the most common ways to store a
# collection of data under one variable name in Python.


#The contents of a dictionary can also be changed while the program is running.

#EXAMPLE CODE
'''

fruit_tuple = ("apple", "banana", "strawberry", "orange")

print(fruit_tuple.index("strawberry"))

print(fruit_tuple[2])

names_list = ["John", "Tim", "Sam"]

del names_list[1]

names_list.append(input("Add a name: "))

print(names_list)

names_list.append(input("Enter another name: "))

print("Names in alphabetical order:", sorted(names_list))

colours = {1: "red", 2:"blue", 3:"green"}

colours[2] = "yellow"

print(colours)

'''

#LIST EXAMPLES

x = [154, 234, 865, 583, 4536]

print(len(x))

print(x[1:4])

for i in x:
    print(i)

num = int(input("Enter a number: "))
if num in x:
    print(num, "is in the list")

else:
    print("Not in the list")

x.insert(2, 420)

x.remove(583)

x.append(993)

print(x)