# import csv

# sy = int(input("start year: "))
# ey = int(input("end year: "))


# file = list(csv.reader(open("Books.csv")))

# tmp = []


# for row in file:
#     tmp.append(row)

# x=0
# for row in tmp:
#     if int(tmp[x][2]) >= sy and int(tmp[x][2]) <= ey:
#         print(tmp[x])
#     x=x+1
#  -------------------------------

# num = sy < num < ey
# for row in file:
#     if num in row:
#         print()
#         print(row)

#     else:
#         print("That author is not included!!!")
    


# ---------------------------------

import csv

start = int(input("Enter a starting year: "))
end = int(input("Enter an end year: "))

file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)

x=0
for row in tmp:
    if int(tmp[x][2]) >= start and int(tmp[x][2]) <=end:
        print(tmp[x])
    x=x+1