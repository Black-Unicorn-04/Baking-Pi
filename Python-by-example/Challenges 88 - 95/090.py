from array import*

nums = array('i', [])
count = 0
while count < 5:
    num = int(input("Enter a number: "))

    if 10<num<20:
        nums.append(num)
        count +=1
    else:
        print("Outside the range")

print("Thank you")

for i in nums:
    print(i)