''' Christian Vasquez | COMP 150 | 3/14/23
    Lab 2 - vasquezLetterGrade.py

    Takes exam(60%) and lab(40%) scores from the user and
    returns the letter of both combined
'''

def getScores():                                            # Method to take user input
    exam = float(input("Enter your exam score: "))          # Get exam score
    lab = float(input("Enter your lab score: "))            # Get lab score
    return exam, lab                                        # Return exam and lab scores

def calculateGrade(exam, lab):                              # Method to calculate grade
    total = 0.6 * exam + 0.4 * lab                          # Exam worth 60%, Lab worth 40%
    if total >= 90:                                         # If >= 90
        return "A"                                          # Return A
    elif total >= 80:                                       # Else if >= 80
        return "B"                                          # Return B
    elif total >= 70:                                       # Else if >= 70
        return "C"                                          # Return C
    elif total >= 60:                                       # Else if >= 60
        return "D"                                          # Return D
    else:                                                   # Else (none of the options above)
        return "F"                                          # Return F

def main():                                                 # Main function
    exam, lab = getScores()                                 # Take user input for exam and lab scores
    grade = calculateGrade(exam, lab)                       # New var grade holds the letter grade from calculateGrade
    print("Exam score: ", exam)                             # Print exam score
    print("Lab score: ", lab)                               # Print Lab score
    print("Letter grade: ", grade)                          # Print letter grade


main()                                                      # Run program
