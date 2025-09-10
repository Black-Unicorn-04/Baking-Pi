num = int(input("Enter a number between 10 and 20: "))

while num != 20:
    if num < 20:
        print("Too low")
    else:
        print("Too high")
    num = int(input("Enter a number between 10 and 20: "))

print("Thank you")
