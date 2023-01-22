''' Christian Vasquez | 1/21/23 | COMP 150
    Lab 4 - BMI Input

    This program prompts the user for
    their height(in) and weight(lbs), and then
    calculates the BMI of the user using
    the equation bmi = (weight / height^2 * 703)
'''

name = input("Enter your name: ")                       # Prompts for name
weight = int(input("Enter your weight (lbs): "))        # Prompts for weight (lbs)
height = int(input("Enter your height (in): "))         # Prompts for height (in)
bmi = weight / height**2 * 703                          # Calculates bmi
print(name + "'s BMI is " + str(bmi))                   # Print result
