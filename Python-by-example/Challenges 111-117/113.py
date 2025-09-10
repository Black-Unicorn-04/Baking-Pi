import csv

file = open("Books.csv", "a")
num = int(input("How many records would you like to add: "))


for i in range(num):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = input("Enter the year: ")
    nr = title + "," + author + "," + year + "\n"
    file.write(nr)

file = open("Books.csv", "r")
la = input("Which author: ") #lookup-author

for row in file:
    if la in row:
        print()
        print(row)

    else:
        print("That author is not included!!!")
    

