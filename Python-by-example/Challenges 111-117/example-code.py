import csv
# file = open("People.csv","w")
# newRecord = "Brian,19,Exodus\n"
# file.write(str(newRecord))
# file.close()


# file = open("People.csv","a")
# name = input("Enter name: ")
# age = input("Enter age: ")
# star = input("Enter a Bible books: ")

# newRecord = name + "," + age + "," + star + "\n"
# file.write(str(newRecord))
# file.close()


# file = open("People.csv","r")
# # for row in file:
# #     print(row)
# reader = csv.reader(file)
# rows = list(reader)
# print(rows[1])

# file = open("People.csv", "r")
# search = input("Enter the data you are searching for: ")
# reader = csv.reader(file)
# for i in file:
#     if search in str(i):
#         print(i)

file = list(csv.reader(open("People.csv")))
tmp = []
for row in file:
    tmp.append(row)

print(tmp)

file = open("NewPeople.csv", "w")
x=0
for row in tmp:
    newRec =tmp[x][0] + "," + tmp[x][1] + "," + tmp[x][2] + "\n"
    file.write(newRec)
    x = x+1
file.close()