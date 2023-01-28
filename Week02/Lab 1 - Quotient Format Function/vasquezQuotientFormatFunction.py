''' Christian Vasquez | 1/24/2023 | COMP 150
    Lab 1 - vasquezQuotientFormatFunction.py

    This program prompts the user for two integers
    and prints the solution using a function
'''


def quotientFormat():                                                         # function quotientFormat
    dividend = int(input("Enter an integer: "))                               # Asking for integer input
    divisor = int(input("Enter another integer: "))                           # Asking for integer input
    quotient = int(dividend / divisor)                                        # Calculating quotient
    remainder = int(dividend % divisor)                                       # Calculating Remainder
    print('The quotient of {} and {} is {}, with a '                          # Print result
          'remainder of {}'.format(dividend, divisor, quotient, remainder))

def main():                                                                   # Main method for testing
    quotientFormat()
    quotientFormat()
    quotientFormat()
    quotientFormat()



main()                                                                        # Run program