''' Christian Vasquez | 1/24/2023 | COMP 150
    Lab 4 - vasquezRevisedBMI.py

    This program prompts the user for
    their height(in) and weight(lbs), and then
    calculates the BMI of the user using
    an equation. Uses two functions
'''


def bmiCalculator(name, weight, height):                    # Function bmiCalculator
    bmi = weight / height**2 * 703                          # Calculates bmi
    print("{}'s BMI is {}".format(name, bmi))               # Print result

def main():
    name = input("Enter your name: ")                       # Prompts for name
    weight = int(input("Enter your weight (lbs): "))        # Prompts for weight (lbs)
    height = int(input("Enter your height (in): "))         # Prompts for height (in)
    bmiCalculator(name, weight, height)                     # Call function bmiCalculator


main()                                                      # Run program