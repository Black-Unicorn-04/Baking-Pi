
# word = input("Enter a word in uppercase: ")

# while word.islower():
#     word = input("Enter a word in uppercase: ")

# print("Thanks")

word = input("Enter a word in uppercase: ")
tryagain = False

while tryagain == False:
    if word.isupper():
        print("Thanks")
        tryagain = True
    else:
        print("Try again")
        word = input("Enter a word in uppercase: ")