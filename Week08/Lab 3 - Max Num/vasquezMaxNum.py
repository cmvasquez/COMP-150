''' Christian Vasquez | COMP 150 | 3/14/23
    Lab 3 - vasquezMaxNum.py

    Finds the largest number out of 3 elements and
    returns/prints
'''


def maxNum(a, b, c):                                            # Find largest number
    if a >= b and a >= c:                                       # If 'a' >= both 'b' and 'c'
        return a                                                # 'a' is the largest
    elif b >= a and b >= c:                                     # Else if 'b' >= both 'a' and 'c'
        return b                                                # 'b' is the largest
    else:                                                       # Else
        return c                                                # 'c' is the largest

def main():                                                     # Main function
    print('The largest number is', maxNum(3, 4, 5))             # prints 5
    print('The largest number is', maxNum(1, 3, 2))             # prints 3
    print('The largest number is', maxNum(7, 3, 2))             # prints 7


main()                                                          # Run program