# BMI Calculator in Python
name = input("Enter your name: ")
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))
# Calculate BMI
BMI = weight / (height ** 2)
print(BMI)
# Determine category
if BMI > 0:
    if BMI <= 18.5:
        print(f"{name}, you are underweight.")
    elif 18.5 < BMI <= 24.9:
        print(f"{name}, you are normal-weight.")
    elif 25 < BMI <= 29.9:
        print(f"{name}, you are overweight.")
    elif 30 < BMI <= 34.9:
        print(f"{name}, you are obese.")
    elif 35 < BMI <= 39.9:
        print(f"{name}, you are severely obese.")
    else:
        print(f"{name}, you are morbidly obese.")
else:
    print("Please enter a valid height and weight.")
