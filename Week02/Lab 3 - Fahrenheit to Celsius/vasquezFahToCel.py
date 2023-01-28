''' Christian Vasquez | 1/24/2023 | COMP 150
    Lab 3 - vasquezFahToCel.py

    This program takes an integer (Fahrenheit)
    from the user and returns the Celsius conversion
'''

def fahToCel(f):                                                # Function fahToCel
    c = (f-32)*(5.0/9)                                          # Equation to convert F to C
    print('{0:.2f} degrees Fahrenheit is the '                  # Print result
          'same as {1:.2f} degrees Celsius.'.format(f, c))

def main():                                                     # Main method for testing
    fahToCel(32)
    fahToCel(98.45)
    fahToCel(-23.2)


main()                                                          # Run program