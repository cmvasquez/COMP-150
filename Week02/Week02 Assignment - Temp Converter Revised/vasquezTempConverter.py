''' Christian Vasquez | 1/24/2023 | COMP 150
    Week02 Assignment - vasquezTempConverter.py

    This program has two methods, one for converting
    an integer from Fahrenheit to Celsius, and one for
    converting an integer from Celsius to Fahrenheit.
    The main method tests them with 3 method calls each.
'''

def fahToCel(f):                                                # Function fahToCel
    c = (f-32)*(5.0/9)                                          # Equation to convert F to C
    print('{0:.2f} degrees Fahrenheit is the '                  # Print result
          'same as {1:.2f} degrees Celsius.'.format(f, c))

def celToFah(c):                                                # Function celToFah
    f = (c*(9/5))+32                                            # Equation to convert C to F
    print('{0:.2f} degrees Celsius is the same'                 # Print result
          ' as {1:.2f} degrees Fahrenheit.'.format(c, f))

def main():                                                     # Main method for testing
    fahToCel(32)
    fahToCel(98.45)
    fahToCel(-23.2)
    celToFah(0)
    celToFah(12)
    celToFah(-32)


main()                                                          # Run program