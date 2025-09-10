from array import*

nums1 = array('i',[])
nums2 = array('i', [])

for i in range(5):
    num = int(input("Enter a number: "))
    nums1.append(num)

nums1 = sorted(nums1)

for i in nums1:
    print(i)

selected = int(input("Enter a number from the list: "))

if selected in nums1:
    nums1.remove(selected)
    nums2.append(selected)


    print(nums1)
    print(nums2)
else:
    print("that isn't in the array")