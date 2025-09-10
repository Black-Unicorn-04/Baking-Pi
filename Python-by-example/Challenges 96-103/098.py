list = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

r = int(input("Select a row: "))


print(list[r])

v = int(input("Enter a value: "))

list[r].append(v)


print(list[r])