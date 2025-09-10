nums = []


num1 = int(input("Enter a number: "))
nums.append(num1)

num2 = int(input("Enter a number: "))
nums.append(num2)

num3 = int(input("Enter a number: "))
nums.append(num3)

print (nums)

ans = input("Do you want to keep the last number you entered? ")

if ans == "no":
    nums.remove(num3)

print(nums)

