num1 = int(input("Enter a number: "))

num2 = int(input("Enter a second number: "))

total = num1+num2

print(num1, "+", num2, "=", total)

ans = input("Do you want to add another number?")

while ans == "y":
    num_x = int(input("Enter a number: "))
    total = total+num_x
    ans = input("Do you want to add another number?")

print("Total:", total)

