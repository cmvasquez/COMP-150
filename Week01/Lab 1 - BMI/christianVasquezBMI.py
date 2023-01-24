''' Christian Vasquez | 1/21/23 | COMP 150
    Lab 1 - BMI

    This program calculates the BMI of a person
    given their height and weight.
'''

name = "Christian"                      # String variable
weight = 130                            # Int variable (weight)
height = 72                             # Int variable (height)
bmi = weight / height**2 * 703          # Calculating the bmi
print(name + "'s BMI is " + str(bmi))   # Print result