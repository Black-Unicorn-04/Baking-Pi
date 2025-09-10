print("1) Square \n2) Triangle")

ans = int(input("Enter a number: "))

if ans == 1:
    l = int(input("Enter the length of one of the sides: "))
    print("Area = ", l*l)

elif ans ==2:
    b = int(input("Base of the triangle: "))
    h = int(input("Height of the triangle: "))
    print("Area =", 0.5*b*h)

else:
    print("Error! Number out of range")