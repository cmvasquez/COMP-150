''' Christian Vasquez | COMP 150 | 3/14/23
    Lab 4 - vasquezCourseGrade.py

    Tells the student if they passed (70 w/o extra
    credit, 60 w/ extra credit) or if they failed
    (grade < 70)
'''

def courseGrade(average, extraCredit):          # Method to find course grade and tell user if pass/fail
    if extraCredit:                             # If there is extra credit
        adjustedAverage = average + 10          # Adjusted average is the average + 10
    else:                                       # If there is no extra credit
        adjustedAverage = average               # Adjusted average is just the average
    if adjustedAverage >= 70:                   # If adjusted average is >= 70
        return "Pass"                           # User passed
    else:                                       # If adjusted average < 70
        return "Does not meet requirements"     # User does not meet requirements


def main():                                     # Main method for testing
    print(courseGrade(75, False))               # will print “Pass”
    print(courseGrade(65, True))                # will print “Pass”
    print(courseGrade(65, False))               # will print “Does not meet requirements”


main()                                          # Run Program
