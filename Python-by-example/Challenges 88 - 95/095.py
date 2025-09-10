from array import*

nums = array('f', [10.22, 43.23, 23.43, 55.55, 67.89])

tryagain = True

while tryagain == True:
    num = int(input("A number between 2 and 5:"))
    if 2<num<5:
        for i in nums:
            print(round((i/2),2))
    else:
        print("ERROR! OUT OF RANGE!")
