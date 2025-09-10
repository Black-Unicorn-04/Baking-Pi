food_dictionary = {}

food1 = input("Enter a food you like: ")
food_dictionary[1] = food1

food2 = input("Enter a second food you like: ")
food_dictionary[2] = food2

food3 = input("Enter a third food you like: ")
food_dictionary[3] = food3

food4 = input("Enter a fourth...: ")
food_dictionary[4] = food4


print(food_dictionary)


nope = int(input("Which one do you want to get rid of?: "))
del food_dictionary[nope]

print(sorted(food_dictionary.values()))


# delete one
# sort dictionary