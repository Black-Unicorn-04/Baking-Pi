from array import*

nums = array('i', [])
for i in range(5):
    num = int(input("Enter a number: "))
    nums.append(num)

print(nums)

nums = sorted(nums)
nums.reverse()


print(nums)