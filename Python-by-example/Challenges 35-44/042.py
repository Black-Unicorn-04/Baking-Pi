total = 0

for i in range(5):
    num = int(input("Enter a number: "))
    ans = input("Do you want to include this number? ")
    if ans.lower() == "yes":
        total = total + num

print("-------------")
print(total)
