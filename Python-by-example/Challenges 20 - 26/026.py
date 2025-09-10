word = input("Enter a word to be converted to Pig Latin: ")

if word[0] == "a":
    converted = word + "way"
    print(converted.lower())

elif word[0] == "e":
    converted = word + "way"
    print(converted.lower())

elif word[0] == "i":
    converted = word + "way"
    print(converted.lower())

elif word[0] == "o":
    converted = word + "way"
    print(converted.lower())

elif word[0] == "u":
    converted = word + "way"
    print(converted.lower())


else: 
    converted2 = word[1:]+word[0]+"ay"
    print(converted2.lower())