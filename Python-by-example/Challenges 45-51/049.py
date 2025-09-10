compnum = 50
attempt = 0
num = int(input("Enter a number: "))

while compnum != num:
    if num < compnum:
        print("too low")
        num = int(input("Enter a number: "))
        attempt = attempt + 1
    else:
        print("too high")
        num = int(input("Enter a number: "))
        attempt = attempt + 1
        
attempt = attempt + 1
print("Well done, you took", attempt, "attempts.")
