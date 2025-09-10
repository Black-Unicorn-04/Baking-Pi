import random


def one():
    num_1 = random.randint(5,20)
    num_2 = random.randint(5,20)

    print("What is", num_1, "+", num_2, "=")
    add_ans = int(input("Your answer: "))
    correct_add_ans =num_1+num_2
    addition_data_tuple = (add_ans, correct_add_ans)
    return addition_data_tuple

def two():
    num1 = random.randint(25,50)
    num2 = random.randint(1,25)

    print("What is", num1, "-", num2, "=")
    sub_ans = int(input("Your answer: "))
    correct_sub_ans = num1-num2

    subtraction_data_tuple = (sub_ans, correct_sub_ans)
    return subtraction_data_tuple

def check_add(add_ans, correct_add_ans):
    if add_ans == correct_add_ans:
        print("Correct!")
    else:
        print("Incorrect, the answer is", correct_add_ans)

def check_sub(sub_ans, correct_sub_ans):
    if sub_ans == correct_sub_ans:
        print("Correct!")
    else:
        print("Incotrrect, the answer is", correct_sub_ans)

def menu():
    ans = int(input("1) Addition \n2) Subtraction \nEnter 1 or 2:"))

    if ans == 1:
        add_ans, correct_add_ans =  one()
        check_add(add_ans, correct_add_ans)
    if ans == 2:
        sub_ans, correct_sub_ans = two() 
        check_sub(sub_ans, correct_sub_ans)


def main():
    menu()
    main()
main()

# def check():
    
