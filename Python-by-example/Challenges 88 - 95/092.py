from array import*
import random

full_array = array('i', [])

enums = array('i', [])

rnums = array('i', [])

for i in range(3):
    enum = int(input("Enter a number: "))
    enums.append(enum)

for j in range(5):
    rnum = random.randint(1,100)
    rnums.append(rnum)


full_array.extend(enums)

full_array.extend(rnums)

full_array = sorted(full_array)

for k in full_array:
    print(k)

