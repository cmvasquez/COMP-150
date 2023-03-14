''' Christian Vasquez | COMP 150 | 3/14/23
    Lab 1 - vasquezTeenList.py

    Returns a list of all numbers from 13 to 19
    from the masterList
'''


def makeTeenList(numberList):                   # Function to extract teens from masterList
    teenList = []                               # New empty list
    for num in numberList:                      # Iterate through the masterList
        if num >= 13 and num <= 19:             # If the number is a teen
            teenList.append(num)                # Add to the list
    return teenList                             # Return the list


def main():                                     # Main function
    masterList = [0, 20, 14, 9, 17, 15, 12]     # Master list
    teenNums = makeTeenList(masterList)         # New variable teenNums holds the list from makeTeenList
    for num in teenNums:                        # Iterate through the teenNums list
        print(num)                              # Print


main()                                          # Run program
