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
