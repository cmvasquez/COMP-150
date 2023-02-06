''' Christian Vasquez | 2/6/23 | COMP 150
    Lab 3 - Square the List

    This program displays the numbers in a list
    and their sum, as well as the square of each
    element in the list and sum using for loops
    and two functions
'''


def sumOriginal(numList):                           # Function to display and sum the original list
    sumOrig = 0                                     # Initialize variable to hold sum at 0
    for element in range(0, len(numList)):          # For loop to iterate through the list
        sumOrig += numList[element]                 # Add the current element to sumOrig, continue until none left
    return numList + [sumOrig]                      # Return the list with sumOrig added to end of the list

def sumSquared(numList):                            # Function to square the list and display it and its sum
    squaredList = []                                # Initialize the list to hold squared elements as empty
    for element in range(0, len(numList)):          # For loop to iterate through the original list
        squaredList.append(numList[element]**2)     # Square current element and add to end of new list
    sumSqrd = 0                                     # Initialize variable to hold sum at 0
    for element in range(0, len(squaredList)):      # For loop to iterate through the squared list
        sumSqrd += squaredList[element]             # Add the current element to sumSqrd, continue until none left
    return squaredList + [sumSqrd]                  # Return the new list with sumSqrd added to end of the list

def main():                                         # Main function to call above functions
    numList1 = [5, 2, 4]                            # Num List test 1
    print(sumOriginal(numList1))                    # Print the original list and sum
    print(sumSquared(numList1))                     # Print the squared list and sum
    numList2 = [0, 1, 2, 3, 4, 5]                   # Num List test 2
    print(sumOriginal(numList2))                    # Print the original list and sum
    print(sumSquared(numList2))                     # Print the squared list and sum


main()                                              # Run the program