# word = input("Enter: ")

# length = len(word)
# num=1

# for i in word:
#     position = length - num
#     l = word[position]
#     print(l)
#     num +=1

word = input("Enter a word: ")


for i in word[::-1]:
    print(i)