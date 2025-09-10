name1 = input("Person 1: ")
name2 = input("Person 2: ")
name3 = input("Person 3: ")

party = [name1, name2, name3]
more = input("Do you want to invite more people?: ")

while more == "yes":
    name = input("person: ")
    party.append(name)
    more = input("Do you want to invite more people?: ")

print(len(party), "are coming")


for i in party:
    print(i)


star = input("type the name of someone from this list: ")

print(party.index(star))

ans = input("Do you still want that person to come?")

if ans == "no":
    party.remove(star)

print(party)
