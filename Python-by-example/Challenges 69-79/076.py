# party_list = []

# print("People to invite to your party: ")

# p1 = input("person 1: ")
# party_list.append(p1)

# p2 = input("person 2: ")
# party_list.append(p2)

# p3 = input("person 3: ")
# party_list.append(p3)

# count = 3

# more = input("Do you want to invite more people?: ")

# while more == "yes":
#     name = input("person: ")
#     party_list.append(name)
#     count +=1
#     more = input("Do you want to invite more people?: ")

# print(count, "people are coming")

# for i in party_list:
#     print(i)

name1 = input("Person 1: ")
name2 = input("Person 2: ")
name3 = input("Person 3: ")

party = [name1, name2, name3]
more = input("Do you want to invite more people?: ")

while more == "yes":
    name = input("person: ")
    party.append(name)
    more = input("Do you want to invite more people?: ")

print(len(party))