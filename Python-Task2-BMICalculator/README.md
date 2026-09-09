# BMI Calculator

A simple command-line BMI (Body Mass Index) Calculator developed in Python as part of the Oasis Infobyte Python Programming Internship.

## 📌 Project Overview

This program calculates a user's Body Mass Index (BMI) based on their weight and height. It then classifies the result into a standard BMI category.

The project was developed using basic Python concepts such as user input, arithmetic operations, conditional statements, exception handling, and input validation.

## ✨ Features

- Accepts weight in kilograms (kg)
- Accepts height in meters (m)
- Calculates BMI using the standard formula
- Displays BMI rounded to 2 decimal places
- Classifies BMI into:
  - Underweight
  - Normal
  - Overweight
  - Obese
- Validates numeric input
- Rejects zero and negative values
- Provides helpful error messages

## 🧮 BMI Formula

```text
BMI = weight / (height²)
Where:

Weight is measured in kilograms
Height is measured in meters
📊 BMI Categories
BMI Range	Category
Below 18.5	Underweight
18.5 – 24.9	Normal
25 – 29.9	Overweight
30 or above	Obese
🛠️ Technologies Used
Python
input()
Conditional statements
try-except exception handling
Basic arithmetic operations
▶️ How to Run
1. Clone the repository
git clone https://github.com/sanskrutipatle22-collab/OIBSIP.git
2. Navigate to the project folder
cd OIBSIP/Task_2_BMI_Calculator
3. Run the program
python BMI.py
💻 Example
===== BMI Calculator =====
Enter your weight in kg: 67
Enter your height in meters: 1.70

Your BMI is: 23.18
Category: Normal
⚠️ Input Validation

The program handles invalid input such as:

abc

Output:

Error: Please enter numbers only.

It also rejects zero and negative values:

Error: Weight and height must be positive values.
📁 Project Structure
Task_2_BMI_Calculator/
├── BMI.py
├── README.md
└── .gitignore
🎯 Internship Task

Oasis Infobyte — Python Programming Internship

Task 2: BMI Calculator

Author

Sanskruti Patle
screenshots/bmi-calculator.png

