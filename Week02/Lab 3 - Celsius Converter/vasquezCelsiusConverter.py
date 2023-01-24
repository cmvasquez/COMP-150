''' Christian Vasquez | 1/24/2023 | COMP 150
    Lab 3 - vasquezCelsiusConverter.py

    This program takes an integer (Fahrenheit)
    from the user and returns the Celsius conversion
'''


def fahToCel(f):            # function fahToCel
    c = (f-32)*(5.0/9)      # celsius
    print('{0:.2f} degrees Fahrenheit is the same as {1:.2f} degrees Celsius.'.format(f, c)) # result

# Testing below
fahToCel(32)
fahToCel(98.45)
fahToCel(-23.2)