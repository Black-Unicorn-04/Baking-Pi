list = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

r = int(input("Select a row: "))

print(list[r])

c = int(input("Select a column: "))

print(list[r][c])


q = input("Do you want to change the value? ")

if q == "yes":
    nv = int(input("What value would you like to replace it with?: "))
    list[r][c] = nv
    print(list[r])
else:
    print()


