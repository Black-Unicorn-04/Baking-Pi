name = input("Enter your name: ")

if len(name) < 5:
    surname = input("Enter your surname: ")
    fullname = name+surname
    print(fullname.upper())

else:
    print(name.lower())