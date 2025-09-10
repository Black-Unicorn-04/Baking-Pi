import random

rnum = random.randint(1,10)

num = int(input("Enter a number: "))

while num != rnum:
    num = int(input("Try another number: "))

print("Correct!", rnum)