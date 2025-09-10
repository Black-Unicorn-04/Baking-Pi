import random

colour = random.choice(["red", "orange", "green", "pink", "blue"])


print("Colour options: red, orange, green, pink, and blue")

print(colour)

answer = input("Pick one!: ")


if answer == colour:
    print("Well Done!")

while answer != colour:

    if colour == "red":
        print("Don't be red with anger, try again")
        

    elif colour == "orange":
        print("Orange you glad you tried?")

    elif colour == "blue":
        print("Don't be blue, try again")

    elif colour == "green":
        print("Don't be green with envy, try again")    


    elif colour == "pink":
        print("Well I'm tickled pink that you tried...but try again")    

    elif colour == "blue":
        print("Don't be blue, try again")

    answer = input("Pick one!: ")


print("Corrreeect!!")