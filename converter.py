km = input("How many kilometers did you run today?\n")

# print("Okay, you said " + km);

km_to_mi = float(km) * 0.621371
km_to_mi = round(km_to_mi, 2)

print(f"Your {km}km run was {km_to_mi}mi")