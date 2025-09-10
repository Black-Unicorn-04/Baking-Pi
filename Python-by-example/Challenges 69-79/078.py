list = ["Phineas and Ferb", "Angels", "Dreamgirls", "NatGeo"]

for i in list:
    print(i)

new_show = input("Enter another show: ")
place = int(input("Where do you want it?"))

list.insert(place,new_show)

for i in list:
    print(i)