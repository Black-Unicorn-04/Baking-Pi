def get_number():
    num = int(input("Enter a number: "))
    return num

def count_to_num(num):
    count = 1
    while count != num:
        print(count)
        count +=1

def main():
    num = get_number()
    count_to_num(num)
main()
