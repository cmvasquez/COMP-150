'''
Name: Christian Vasquez | 2/13/23 | COMP 150
Lab exercise primeNumbers:  Write three for
loops and fill in the blanks in each of the
functions below. You must implement range as condition
'''


# 1
def displayPrime(primeList):
    # for loop to output every element of primeList. Add a space or comma to separate numbers
    for idx in range(len(primeList)):
        print(primeList[idx], end=' ')
    print("\n")


# 2
def sumPrimeList(primeList):
    sum = 0
    # for loop to add all elements of primeList into sum
    for num in primeList:
        sum += num
    return sum


# 3
def displayReversePrime(primeList):
    # for loop to output every element of primeList in reverse. Add a space to separate numbers
    for idx in range(len(primeList) - 1, -1, -1):
        print(primeList[idx], end=' ')
    print("\n")


def main():
    primeList = [2, 3, 5, 7, 11, 13, 17, 19]
    displayPrime(primeList)
    print('The sum of all numbers in primeList is', sumPrimeList(primeList))  # invoke sumPrimeList
    print("\n")  # line break for second test cas
    displayReversePrime(primeList)  # invoke displayReversePrime


main()
