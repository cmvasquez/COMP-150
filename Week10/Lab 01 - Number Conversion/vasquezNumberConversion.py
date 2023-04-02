''' Christian Vasquez | COMP 150 | 4/1/23
    Lab 1 - vasquezNumberConversion.py

    This program has methods to convert binary
    to decimal, decimal to binary, and a main
    function with test cases
'''


def binaryToDec(binaryNum):             # Function to turn binary to decimal
    decNum = 0                          # Initialize decimal number to 0
    expo = 0                            # Initialize exponent to 0
    while binaryNum > 0:                # While binary number is greater than 0
        remBit = binaryNum % 10         # Get the remainder when binary number is divided by 10
        binaryNum //= 10                # Remove the last binary digit
        decNum += remBit * 2 ** expo    # Add the digit value (remBit * 2 ** expo) to decimal number
        expo += 1                       # Increase exponent by 1
    return decNum                       # Return the decimal number


def decToBinary(decNum):                # Function to convert integer to binary
    binaryString = ''                   # Initialize binary string to empty string
    if decNum == 0:                     # If decimal number is 0
        binaryString = '0'              # Set binary string to '0'
    else:
        while decNum > 0:               # While decimal number is greater than 0
            remDigit = decNum % 2       # Get the remainder when decimal number is divided by 2
            binaryString = str(remDigit) + binaryString  # Concatenate remainder to the front of binary string
            decNum //= 2                # Divide decimal number by 2 to get new decimal number value
    return binaryString                 # Return binary string as a decimal


def main():
    # Binary to Decimal Conversion Test Cases
    binaryNum1 = 101010
    binaryNum2 = 110111
    binaryNum3 = 111111

    decNum1 = binaryToDec(binaryNum1)
    decNum2 = binaryToDec(binaryNum2)
    decNum3 = binaryToDec(binaryNum3)

    if decNum1 == 42:
        print("Test Case 1 for binaryToDec Passed")
    else:
        print("Test Case 1 for binaryToDec Failed")

    if decNum2 == 55:
        print("Test Case 2 for binaryToDec Passed")
    else:
        print("Test Case 2 for binaryToDec Failed")

    if decNum3 == 63:
        print("Test Case 3 for binaryToDec Passed")
    else:
        print("Test Case 3 for binaryToDec Failed")

    # Decimal to Binary Conversion Test Cases
    decNum4 = 42
    decNum5 = 55
    decNum6 = 63

    binaryStr4 = decToBinary(decNum4)
    binaryStr5 = decToBinary(decNum5)
    binaryStr6 = decToBinary(decNum6)

    if binaryStr4 == '101010':
        print("Test Case 1 for decToBinary Passed")
    else:
        print("Test Case 1 for decToBinary Failed")

    if binaryStr5 == '110111':
        print("Test Case 2 for decToBinary Passed")
    else:
        print("Test Case 2 for decToBinary Failed")

    if binaryStr6 == '111111':
        print("Test Case 3 for decToBinary Passed")
    else:
        print("Test Case 3 for decToBinary Failed")


main()          # Run the program