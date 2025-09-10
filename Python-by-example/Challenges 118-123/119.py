import random

def pick_numbers():
    low_num = int(input("Enter a low number: "))
    high_num = int(input("Enter a high number: "))

    comp_num = random.randint(low_num, high_num)

    return comp_num


def guess_num():
    print("I am thinking of a number...")
    guess = int(input("Guess the number: "))
    return guess

def check(comp_num,guess):
    while comp_num != guess:
        if guess < comp_num:
            guess =int(input("Too low: "))
        if guess > comp_num:
            print("Too high: ")
    print("Correct, well done!")

def main():
    comp_num = pick_numbers()
    guess = guess_num()
    check(comp_num,guess)

main()