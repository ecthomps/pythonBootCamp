age = int(input("What is your age\n"))

if age >= 18 and age <= 21:
    print("You can enter, but need a wristband!")
elif age > 21:
    print("You are good to enter and can drink!")
else:
    print("You can't come in, little one! :(")
    