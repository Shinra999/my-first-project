weight = float(input("Enter your Weight: "))
height = float(input("Enter your Height: "))

bmi = weight / (height / 100) ** 2

print(f"BMI: {bmi:.1f}")

if bmi >= 30:
    print("You are Obese")
elif bmi >= 25:
    print("You are Overweight")
elif bmi >=18.5:
    print("You are Normal")
else:
    print("You are Underweight")