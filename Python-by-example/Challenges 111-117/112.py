import csv
file = open("Books.csv", "a")

title = input("Enter title: ")
author = input("Enter the author's name: ")
year = input("Enter year released: ")

new = title+","+author+","+year+"\n"
file.write(new)

file = open("Books.csv", "r")

for row in file:
    print(row)
    # print()

file.close()