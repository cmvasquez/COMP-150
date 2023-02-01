''' Christian Vasquez | 1/31/2023 | COMP 150
    HW 1 - vasquezRevisedReturnBMI.py

    This program prompts the user for
    their height(in) and weight(lbs), and then
    calculates the BMI of the user using
    an equation. Uses two functions and returns
'''


def bmiCalculator(weight, height):                                    # Function bmiCalculator
    bmi = weight / height ** 2 * 703                                  # Calculates bmi
    return bmi                                                        # Return variable


def main():
    name = input("Enter your name: ")                                 # Prompts for name
    weight = int(input("Enter your weight (lbs): "))                  # Prompts for weight (lbs)
    height = int(input("Enter your height (in): "))                   # Prompts for height (in)
    print(name + '\'s BMI is ' + str(bmiCalculator(weight, height)))  # Print result


main()                                                                # Run program
