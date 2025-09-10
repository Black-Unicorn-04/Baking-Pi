
print("" \
"1) Create a new file\n" \
"2) Display the file\n" \
"3) Add a new item to the file\n" \
"" \
"Make a selection 1,2, or 3:")


ans = int(input("Enter a selection: "))

if ans ==1:
    subject = input("Enter a school subject: ")
    file = open("Subject.txt", "w")
    file.write(subject + "\n")
    file.close()

elif ans ==2:
    file = open("Subject.txt","r")
    print(file.read())

elif ans ==3:
    file = open("Subject.txt", "a")
    ns = input("Enter a new subject")
    file.write(ns + "\n")
    file = open("Subject.txt", "r")
    print(file.read())
else:
    print("ERROR! Number not inclusive")


