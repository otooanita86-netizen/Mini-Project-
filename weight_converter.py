#Python weight converter
weight =float(input("Enter your weight: "))
unit = input("Kilograms or pounds? (K or L) ")

if unit =="K":
    weight = round(weight * 2.205)
    unit = "Lbs"
elif unit == "L":
    unit = "Kgs"
    weight = round(weight / 2.205)
else:
    print(f"{unit} was not valid ")

print(f"Your weight is : {weight} {unit}")
