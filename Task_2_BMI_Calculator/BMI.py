print("===== BMI Calculator =====")

try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    if weight <= 0 or height <= 0:
        print("Error: Weight and height must be positive values.")
    else:
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")

except ValueError:
    print("Error: Please enter numbers only.")