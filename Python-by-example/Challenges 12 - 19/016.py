rain_status = input("Is it raining?")

rain_status = str.lower(rain_status)

if rain_status == "yes":
    windy = input("Is it windy?")
    windy = str.lower(windy)

    if windy =="yes":
        print("It is too windy for an umbrella.")
    
    else: 
        print("Take an umbrella")

else:
    print("Enjoy your day")