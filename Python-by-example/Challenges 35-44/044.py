num = int(input("Enter the number of people you want to invite to a party: "))

if num < 10:
    for i in range (num):
        en = input("Enter Name: ")
        print(en, "has been invited")

else:
    print("Too many people")