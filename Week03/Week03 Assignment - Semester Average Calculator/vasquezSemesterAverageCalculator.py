''' Christian Vasquez | 1/31/2023 | COMP 150
    Week03 Assignment - vasquezSemesterAverageCalculator.py

    This program takes user inputs for a final grade and midterm grade
    both weighted differently, and calculates your semester average
'''

midtermWeight = 0.4                                                        # Global midterm weight
finalWeight = 0.6                                                          # Global final weight

def inputMidtermAndFinal():                                                # Function to request user input and return
    midterm = float(input("Enter your midterm grade (worth 40%): "))       # Input midterm grade
    final = float(input("Enter your final grade (worth 60%): "))           # Input final grade
    return midterm, final                                                  # Return both inputs


def calculateSemesterAverage(midterm, final):                              # Function to calculate semester average
    return (midterm * midtermWeight) + (final * finalWeight)               # Calculate semester average and return


def main():                                                                # Main function to call functions
    midterm, final = inputMidtermAndFinal()                                # Assign vars to return of input
    print("Midterm grade: {0}%\nFinal grade: {1}%\nSemester "              # Print result
          "Average: {2:.2f}%".format(midterm, final,
                                     calculateSemesterAverage(midterm, final)))


main()                                                                     # Run program

