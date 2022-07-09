# BMI Calculator

# Take two inputs from user, for weight and height.
# Calculate BMI and filter the result to determine if the user is
# Obese, Overweight, Normal or Underweight. Output the result.

weight = float(input())
height = float(input())
bmi = weight / height**2

if bmi > 30:
    print("Obesity")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")