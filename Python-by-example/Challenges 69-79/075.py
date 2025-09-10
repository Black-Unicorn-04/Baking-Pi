num_list = [123,456,789,100]

for i in num_list:
    print(i)

num = int(input("Enter a number: "))

if num in num_list:
    print(num_list.index(num))

else:
    print("That is not in the list")