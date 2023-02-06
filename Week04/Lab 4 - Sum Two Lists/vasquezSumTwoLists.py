''' Christian Vasquez | 2/6/23 | COMP 150
    Lab 4 - Sum Two Lists

    This program displays the numbers in a list
    and adds corresponding elements from equally
    sized lists together in a new list and prints
'''


def displayList(numList):                        # Function to display elements of list as if printing them
    output = "["                                 # Set the left bracket in the print variable
    for i in range(len(numList)):                # Iterate through the list using range and len
        if i == len(numList) - 1:                # If current element is the last element in the list
            output += str(numList[i]) + "]"      # Add the current element and right bracket to the print variable
        else:                                    # If current element is NOT the last element in the list
            output += str(numList[i]) + ", "     # Add the current element and a comma to the print variable
    print(output)                                # Print the list


def addLists(numList1, numList2):                # Function to add two lists elements with eachother
    sumList = numList1                           # Copy numList 1 into sumList
    for element in range(len(numList1)):         # Iterate through the list using range and len
        sumList[element] += numList2[element]    # For each element in sumList, add corresponding element from numList2
    displayList(sumList)                         # Print the summed list using displayList function


def main():                                      # Main function to call above functions
    numList1 = [5, 2, 4]                         # Num List 1
    numList2 = [3, 1, 2]                         # Num List 2
    displayList(numList1)                        # Should print [5, 2, 4]
    displayList(numList2)                        # Should print [3, 1, 2]
    addLists(numList1, numList2)                 # Should print [8, 3, 6]


main()                                           # Run the program