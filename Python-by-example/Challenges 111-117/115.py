import csv

file = open("Books.csv","r")

n = 1

for row in file:
    print("Row:",n," -",row)
    n +=1