def sequence():

    ans = input("Do you want to count 'up' or 'down'?: ")

    if ans == "up":
        num = int(input("Top number: "))
        for i in range(1,num+1):
            print(i)

    elif ans == "down":
        num = int(input("Bottom number (below 20): "))
        for i in range(20,num-1,-1):
            print(i)
    else:
        print("I don't understand.")
        sequence()


def main():
    sequence()
main()