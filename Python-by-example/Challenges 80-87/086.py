p = input("Enter a new password: ")

v = input("Verify the password: ")

if p == v:
    print("Thank you")
elif p.lower() == v.lower():
    print("Must be the same case")
else: 
    print ("incorrect")