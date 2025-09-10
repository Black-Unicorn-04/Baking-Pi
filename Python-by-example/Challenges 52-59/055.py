import random

cnum = random.randint(1,5)

hnum = int(input("Enter a number: "))

if hnum == cnum:
    print("Well done")
    print("Random int", cnum)



else:
    if hnum < cnum:
        print("Too low; try again")

        hnum2 = int(input("Enter another number: "))

        if hnum2 == cnum:
            print("Correct ")
            print("Random int", cnum)

        else:
            print("Nope")
            print("Random int", cnum)

    if hnum > cnum:
        print("Too high; try again")
        hnum2 = int(input("Enter another number: "))

        if hnum2 == cnum:
            print("Great")
            print("Random int", cnum)
        else:
            print("You Loose")
            print("Random int", cnum)
        

