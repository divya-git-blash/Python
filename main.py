name = input("What is your name? ")

if len(name)>3:
    print(" Length of name should be minimum 3 characters")
elif len(name)>50:
    print(" Length of name should be maximum 50 characters")
else:
    print("Your name is Valid")