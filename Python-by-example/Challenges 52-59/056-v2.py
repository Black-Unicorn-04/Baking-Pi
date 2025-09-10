import random

rnum = random.randint(1,10)
correct = False
while correct == False:
    num = int(input("Enter a number: "))
    if num == rnum:
        correct = True
        print(rnum)