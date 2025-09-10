from array import *

import random

nums = array('i', [])

for j in range(5):
    num = random.randint(0,50)
    nums.append(num)


for i in nums:
    print(i)

# from array import*
# import random

# nums = array('i',[])

# for i in range (5):
#     num = random.randint(1,100)
#     nums.append(num)

# for i in nums:
#     print(i)