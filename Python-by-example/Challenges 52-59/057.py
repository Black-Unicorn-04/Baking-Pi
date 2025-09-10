import random

rnum = random.randint(1,10)

correct = False

count = 1

while correct == False:
    guess = int(input("Enter a number: "))
    if guess < rnum:
        print("Too low")
        count = count+1
    elif guess > rnum:
        print("too high")
        count = count+1
    elif guess == rnum:
        correct = True

if count == 1:
    print("Good Job!!!", count, "try!")


else:
    print("Good Job!!!", count, "tries!")

