#001

"""firstname = input("Please enter your first name: ")
print ("Hello", firstname)"""


#002

"""firstname = input("Please enter your firstname: ")
surname = input("Please enter your surname: ")
print("Name = ", firstname, surname)"""



#003
'''print("What do you call a bear with no teeth?\n A gummy bear!")'''



#004

"""num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))

answer = num1 + num2

print("The answer is", answer)"""



#005

"""num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))
num3 = int(input("Enter a third number: "))

answer = (num1 + num2)*num3

print("The answer is", answer)"""



#006

'''slices_start = int(input("How many slices did you start with? "))
slices_end = int(input("How many slices have you eaten?"))

slices_left = slices_start - slices_end

print("You have", slices_left, "slices left!")'''

#precious was here


#007

'''name = input("What is your name?")

age = int(input("How old are you?"))

age2 = age+1

print (name, ", next birthday you will be",age2)
'''

#008

'''total = int(input("Total price of the bill: "))
diners = int(input("Number of diners: "))

each = total/diners

print(each)'''


#009

'''days = int(input("Enter number of days: "))

hours = days*24 

minutes = hours*60

seconds = minutes*60

print('Those are', hours, 'hours,',minutes, 'minutes', seconds, 'seconds')
'''

#010

'''kg = int(input('weight in kilograms: '))

pound = kg*2204

print(pound, "pounds")'''


#011

'''large = int(input("Enter a number over 100: "))
small = int(input("Enter a number under 10:"))

answer = large/small

print(small,"enters",large, answer, "times")'''


#012

'''num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

if num1 > num2:
    print(num1, num2)

else:
    print(num2, num1)'''

#013

'''number = int(input("Enter a number that is under 20: "))
if number <20:
    print("Thank you")

else:
    print("Too high")
'''
#015

'''color = input("Enter your favorite color: ")


if color == 'red' or color == 'RED' or color == 'Red':
    print("My favorite color is red too!!")
else:
    print("I don't like", color,". I prefer red")'''


#016

'''rain_status = input("Is it raining?")
rain_status = str.lower(rain_status)

if rain_status == 'yes':
    windy_status = input("Is it windy?")
    windy_status = str.lower(windy_status)
  
    if windy_status == 'yes':
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")

else:   
    print("Enjoy your day.")
'''

# 017


'''def age_equate():

    age = int(input("Enter age: "))

    if age >= 18:
        print("You can vote")
    elif age == 17:
        print("You can learn to drive")

    elif age == 16:
        print("You can buy a lottery ticket")

    else:
        print("You can go Trick-or-Treating")


age_equate()'''



#018

'''number = int(input("Enter a number: "))

if number < 10:
    print("Too low")

elif number < 20 and number > 10:
    print("Correct")

else:
    print("Too high")'''


#019

'''number = int(input('Enter either 1,2, or 3: '))

if number == 1:
    print("Thank you")

elif number == 2:
    print("Well done")

elif number ==3:
    print("Correct")

else:
    print("Error message")'''


#020

'''first_name = input("Enter you're first name: ")
name_length = len(first_name)
print(name_length)'''


#021

'''firstname = input("Enter your first name: ")
surname = input("Enter your surname: ")

length1 = len(firstname)
length2 = len(surname)

total_length = length1 + length2

print(firstname +" "+ surname)
print(total_length)'''


#022

'''firstname = input("Enter your first name in lower case: ")
surname = input("Enter you surname in lower case: ")

firstname = firstname.title()
surname = surname.title()

print(firstname, " ", surname)'''

#023

'''line = input("Type in the first line of a nursery rhyme: ")
length = len(line)

print("This line has ", length, "letters")

start_no = int(input("Enter a starting number: "))

end_no = int(input("Enter an ending number: "))

part = (line[start_no:end_no])

print(part)'''

#024

'''word = input("Enter a word: ")
word = word.upper()
print(word)'''

#025

'''first_name = input("Enter your first name: ")

length = len(first_name)

if length < 5:
    surname = input("Enter your surname: ")
    name = first_name + surname
    print(name.upper())

else:
   l_m = first_name.lower()
   print(l_m)'''

#026 (STILL WORKING ON THIS)

'''word = input(Enter a word)

first_letter = word[0]

if first_letter != a and !=e and !=i and != o and != u:
    word_p = word.lower()
    print(word_p + "ay")

else:
    print(word + "way")'''


#045

'''total = 0

while total <= 50:
   num = int(input("Enter a number: "))
   total = total + num
print("The total is", total)'''

#046

'''number = 0

while number <=5:
   number = int(input("Enter a number: "))

print("The last number you entered was a", number)'''


#052

'''import random
num = random.randint(1,100)
print(num)'''

#053

'''import random
fruit = random.choice(["Apples", "Bananas", "Oranges", "Grapes"])
print(fruit)'''

#054

'''import random


def question():


    choice = input("Heads or tails? [input h/t]: ")
    random_choice = random.choice(["h", "t"])

    print("\n Your choice:", choice)
    print("   Correct choice:", random_choice)

    if (random_choice == 'h' and choice == 'h') or (random_choice == 't' and choice == 't'):
        print("\n You win")

    else: 
        print("\n Bad luck")


def main():
    question()
    main()
main()
'''

#059
#################################
#TRY TO INCOPORATE THIS INTO THE CODE
'''def play_again():
    play = input("Would you like to play again? [y/n]")
    
    if play == 'y':
        print("yes")
        
        guess_game()

    else:
        print("GAME ENDED")'''

###################################
'''def guess_game():
    import random
    random_color = random.choice(["green", "blue", "red", "yellow", "orange"])
    tryagain = True

    while tryagain == True:

        color_guess = input("Select a color: ")
        color_guess = color_guess.lower()

        if random_color == color_guess:
            print("Well done.")
            tryagain = False
        
        else:

            if random_color == "green":
                print("You guessed it wrong, but don't be GREEN with envy")
            elif random_color == "blue":
                print("You got it wrong...but don't feel BLUE")
            elif random_color == "red":
                print("Don't go RED with anger...but...you're wrong")
            elif random_color == "yellow":
                print("YELLOOO...you got it wrong")
            elif random_color == "orange":
                print("ORANGE you glad you can guess again?")



def main():
    guess_game()
main ()'''
    
#060
#square
'''import turtle

for i in range(0,4):
    turtle.forward(100)
    turtle.right(90)

turtle.exitonclick()'''

#061
#triangle
'''import turtle

for i in range(0,3):
    turtle.forward(100)
    turtle.right(120)
turtle.exitonclick()'''

#062

#Circle
'''import turtle

for i in range(0,360):
    turtle.forward(1)
    turtle.right(1)



turtle.exitonclick()'''

#067

'''import turtle
import random

for x in range(0,10):
    for i in range (0,8):
        turtle.forward(50)
        turtle.right(45)
    turtle.right(36)

turtle.hideturtle()
turtle.exitonclick()'''


###########

import turtle
import random

turtle.color("purple")
for x in range(0,2):
    for i in range (0,8):
        turtle.forward(80)
        turtle.right(45)

    turtle.right(36)

turtle.color("pink")

for x in range(0,3):
    for i in range (0,8):
        turtle.forward(80)
        turtle.right(45)

    turtle.right(36)


turtle.color("blue")

for x in range(0,3):
    for i in range (0,8):
        turtle.forward(80)
        turtle.right(45)

    turtle.right(36)

turtle.color("violet")

for x in range(0,3):
    for i in range (0,8):
        turtle.forward(80)
        turtle.right(45)

    turtle.right(36)


turtle.hideturtle()
turtle.exitonclick()
#####


