''' Christian Vasquez | COMP 150 | 4/16/23
    Lab 1 - vasquezNumberConversionV3.py

    This is an updated version of vasquezNumberConversion.py
    which implements a half adder function as well as a
    full adder function using 3 half adders.
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

def decToHex(decNum):
    hexDigits = "0123456789ABCDEF"      # String of hex digits
    hexNum = ''                         # Empty string to hold return value
    while decNum > 0:                   # While there are still digits to count
        remainder = decNum % 16         # Compute remainder when dividing by 16
        hexDigit = hexDigits[remainder] # Get hex digit for this remainder
        hexNum = hexDigit + hexNum      # Add the hex digit to the beginning of hexNum
        decNum //= 16                   # Update decNum to remove LSD
    return hexNum or '0'                # Return hex, or 0 if input is 0


def halfAdder(a, b):
    sum = a ^ b                         # a XOR b
    carry = a & b                       # a AND b
    return sum, carry                   # return


def fullAdder(a, b, cIn):
    sum1, carry1 = halfAdder(a, b)
    sum2, carry2 = halfAdder(sum1, cIn)
    sum3, carry3 = halfAdder(carry1, carry2)
    overFlow = carry3
    return sum3, overFlow, carry2


def main():
    # Half Adder test cases
    a = 0
    b = 0
    expectedSum = 0
    expectedCarry = 0
    sum, carry = halfAdder(a, b)
    if sum == expectedSum and carry == expectedCarry:
        print("Test Case 1 for halfAdder Passed")
        print("a = ", a, "b = ", b, "\nSum = ", sum, "\nCarry = ", carry, "\n\n")
    else:
        print("Test Case 1 for halfAdder Failed")
        print("a = ", a, "b = ", b, "\nSum = ", sum, "\nCarry = ", carry, "\n\n")

    a = 0
    b = 1
    expectedSum = 1
    expectedCarry = 0
    sum, carry = halfAdder(a, b)
    if sum == expectedSum and carry == expectedCarry:
        print("Test Case 2 for halfAdder Passed")
        print("a = ", a, "b = ", b, "\nSum = ", sum, "\nCarry = ", carry, "\n\n")
    else:
        print("Test Case 2 for halfAdder Failed")
        print("a = ", a, "b = ", b, "\nSum = ", sum, "\nCarry = ", carry, "\n\n")

    a = 1
    b = 0
    expectedSum = 1
    expectedCarry = 0
    sum, carry = halfAdder(a, b)
    if sum == expectedSum and carry == expectedCarry:
        print("Test Case 3 for halfAdder Passed")
        print("a = ", a, "b = ", b, "\nSum = ", sum, "\nCarry = ", carry, "\n\n")
    else:
        print("Test Case 3 for halfAdder Failed")
        print("a = ", a, "b = ", b, "\nSum = ", sum, "\nCarry = ", carry, "\n\n")

    a = 1
    b = 1
    expectedSum = 0
    expectedCarry = 1
    sum, carry = halfAdder(a, b)
    if sum == expectedSum and carry == expectedCarry:
        print("Test Case 4 for halfAdder Passed")
        print("a = ", a, "b = ", b, "\nSum = ", sum, "\nCarry = ", carry, "\n\n")
    else:
        print("Test Case 4 for halfAdder Failed")
        print("a = ", a, "b = ", b, "\nSum = ", sum, "\nCarry = ", carry, "\n\n")

    '''
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

    # Decimal to Hexadecimal Conversion Test Cases
    decimalNum1 = 42
    decimalNum2 = 255
    decimalNum3 = 4096
    decimalNum4 = 65535

    hexNum1 = decToHex(decimalNum1)
    hexNum2 = decToHex(decimalNum2)
    hexNum3 = decToHex(decimalNum3)
    hexNum4 = decToHex(decimalNum4)

    if hexNum1 == '2A':
        print("Test Case 1 for decToHex Passed")
    else:
        print("Test Case 1 for decToHex Failed")

    if hexNum2 == 'FF':
        print("Test Case 2 for decToHex Passed")
    else:
        print("Test Case 2 for decToHex Failed")

    if hexNum3 == '1000':
        print("Test Case 3 for decToHex Passed")
    else:
        print("Test Case 3 for decToHex Failed")

    if hexNum4 == 'FFFF':
        print("Test Case 4 for decToHex Passed")
    else:
        print("Test Case 4 for decToHex Failed") '''

main()          # Run the program