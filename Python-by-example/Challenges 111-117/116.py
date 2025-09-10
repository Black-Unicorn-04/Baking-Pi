# import csv

# file = open("Books.csv","r")
# tem = []

# for row in file:
#     tem.append(row)
#     print()

# print(tem)

# q = int(input("Which row would you like to delete? : "))

# d_row = tem[q]

# tem.remove(d_row)

# print(tem)

# r = int(input("Which data do you want to change? Enter the row"))
# c = int(input("Which data do you want to change? Enter the column"))

# print(tem[r][c])

# new_value = input("Enter the new value: ")

# tem.write(new_value[r][c])


import csv

file = list(csv.reader(open("Books.csv")))
Booklist = []

for row in file:
    Booklist.append(row)

x=0
for row in Booklist:
    display = x,Booklist[x]
    print(display)
    x= x + 1
getrid = int(input("Enter a row number to delete: "))
del Booklist[getrid]

x=0
for row in Booklist:
    display = x, Booklist[x]
    print(display)
    x=x+1
alter = int(input("Enter a row number to alter: "))

x=0
for row in Booklist[alter]:
    display = x,Booklist[alter][x]
    print(display)
    x=x+1
part = int(input("Which part do you want to change? "))
newdata = input("Enter new data: ")
Booklist[alter][part] = newdata
print(Booklist[alter])

file = open("Books.csv", "w")
x=0
for row in Booklist:
    newrecord = Booklist[x][0] + "," + Booklist[x][1] + "," + Booklist[x][2] + "\n"
    file.write(newrecord)
    x =x+1
file.close()