#011

lnum = int(input("Enter a number over 100: "))

while lnum <= 100:
    print("invalid input")
    lnum = int(input("Enter a number over 100: "))

snum = int(input("Enter a number under 10: "))

while snum >= 10:
    print("invalid input")
    snum = int(input("Enter a number under 10: "))

print(snum, "fits into", lnum, lnum//snum, "times")