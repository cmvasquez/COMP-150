# BMI Input
# This program prompts the user for
# their height and weight, and then
# calculates the BMI of the user.
# Written by Christian Vasquez COMP 150 1/21/23

name = input("Enter your name: ")
weight = int(input("Enter your weight (lbs): "))
height = int(input("Enter your height (in): "))
bmi = weight / height**2 * 703
print(name + "'s BMI is " + str(bmi))
