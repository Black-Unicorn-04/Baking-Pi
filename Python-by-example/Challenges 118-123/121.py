def add():
    name = input("Enter a new name: ")
    names.append(name)
    return names

def view():
    for i in names:
        print(i)
    print()



def menu():
    print("1) Add a name: \n" \
    "2)Change a name: \n" \
    "3) Delete a name: \n" \
    "4) View all names \n" \
    "5) End Program")

    option = int(input("Enter the desired option: "))
    if option == 1:
        add()
    elif option == 2:
        two()
    elif option == 3:
        three()
    elif option == 4:
        view()
    elif option == 5:
        five()
    else:
        print("\nError. Incorrect Entry. Try again.\n")
        menu()

def main():
    menu()
    main()
names = []
main()