''' Christian Vasquez | 1/24/2023 | COMP 150
    Lab 2 - vasquezGradeAverageFunction.py

    This program calculates a grade average
    using a function
'''

def gradeAverage():                                                         # Function gradeAverage
    name = input("Enter your name: ")                                       # Input name
    exam = int(input("Enter your exam score: "))                            # Exam score
    lab = int(input("Enter your lab score: "))                              # Lab score
    print('Name: {0:>10s} Exam:  {1}  Lab Score:  {2}  '                    # Print result
          'Average:  {3:.2f}'.format(name, exam, lab, (exam + lab) / 2))


def main():                                                                 # Main method for testing
    gradeAverage()
    gradeAverage()
    gradeAverage()
    gradeAverage()


main()                                                                      # Run program
