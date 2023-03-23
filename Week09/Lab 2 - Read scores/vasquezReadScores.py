''' Christian Vasquez | COMP 150 | 3/23/23
    Lab 2 - vasquezReadScores.py

    This program calculates the letter grade for
    a student from last week. I added a function to
    calculate the average using a while loop
'''


def calculateAverage():        # Calculate average score of exams
    total = 0                   # Total exam scores
    count = 0                   # Counter
    score = 0                   # Score input

    while score >= 0:           # While a non negative number is entered
        score = float(input("Enter a score (enter a negative number to quit): "))   # Prompt user
        if score >= 0:          # If the entered score is not negative
            total += score      # Add the score to the total
            count += 1          # Increment counter

    if count == 0:              # If the counter is 0 when program finishes
        print("No scores were entered.")    # Tell the user no scores were entered
        return 0                # Return 0
    else:                       # Else
        avg = total / count     # Calculate the average (total / count)
        return avg, count       # Return the average and the counter


def calculateGrade():           # Calculate the grade
    average, count = calculateAverage()    # Get the average from calculateAverage()
    if average is None:                     # If no average
        return                              # Break
    if average >= 90:                       # If average above 90
        grade = "A"                         # Print A
    elif average >= 80:                     # If average above 80, below 90
        grade = "B"                         # Print B
    elif average >= 70:                     # If average above 70, below 80
        grade = "C"                         # Print C
    elif average >= 60:                     # If average above 60, below 70
        grade = "D"                         # Print D
    else:                                   # If average below 60
        grade = "F"                         # Print F
    print("You entered", count, "exam scores.")     # Tell the user the amount of scores they entered
    print("The average score is:", average)         # Tell them the average score
    print("The corresponding letter grade is:", grade)  # Tell them corresponding letter grade

def main():             # Main function
    calculateGrade()    # Calculate the average grade


main()                  # Run program


