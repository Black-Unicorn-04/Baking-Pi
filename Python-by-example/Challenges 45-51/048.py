count = 0
ans = "yes"
while ans =="yes":
    guest = input("Enter the name of a guest: ")
    print(guest,"has now been invited")
    count = count +1
    ans = input("Do you want to invite another guest?")

print(count, "people are coming to the party")