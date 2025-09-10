from array import*

nums = array('i', [12, 14, 16, 16, 17])

print(nums)


selected = int(input("Pick a number from the array: "))

if nums.count(selected) == 1:
    print(selected,"...in the list once")
else:
    print(selected, "is in the list", nums.count(selected), "times")

# from array import*

# nums = array('i', [5,7,9,2,9])

# for i in nums:
#     print(i)

# num = int(input("Enter a number: "))

# if nums.count(num) == 1:
#     print(num, "is in the list once")
# else:
#     print(num, "is in the list", nums.count(num),"times")