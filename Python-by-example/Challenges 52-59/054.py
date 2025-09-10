import random

ra = random.choice(["h","t"]) #random answer

ha = input("Heads or tails? (h or t): ") #human answer


if ra == ha:
    print("You win")

else:
    print("Bad Luck \n -------------")


print("Computer: ", ra)
print("You: ", ha)