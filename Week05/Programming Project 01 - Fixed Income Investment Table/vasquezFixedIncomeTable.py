''' Christian Vasquez | 2/13/23 | COMP 150
    Programming Project 1 - Fixed Income Table

    The program uses a simple compound interest 
    rate in which interest income is computed annually
    and earned interest income is added onto the total 
    amount, which becomes the base amount for next year calculation.
    It generates a formatted report showing yearly starting balance,
    earned income, and ending balance.
'''

def investInput():  # Method to acquire user inputs
    investment = float(input("Please enter your starting investment amount: $"))  # User input - investment
    interest = float(input("Please enter the annual interest rate (%): "))  # User input - interest
    term = input("Please enter the length of the investment term (number of years): ")  # User input - term
    return investment, interest, term  # Return tuple


def investCalc(investment, interest, term):  # Method to calculate interest
    interestRate = float(interest) / 100  # Convert user interest to decimal
    interestFinal = investment  # New variable to return
    for i in range(int(term)):  # For loop to iterate years
        interestEarned = interestRate * interestFinal  # Multiply interestRate and interestFinal
        interestFinal += interestEarned  # Add interestEarned to interestFinal
    return interestFinal  # Return interestFinal


def formatTable(investment, interest, term):  # Method to format table
    print("\n\nYear\tStarting Balance\tAnnual Income\tEnding Balance")  # Formatting
    print("----\t----------------\t------------\t-------------")  # Formatting
    year = 1  # Initialize year to 1
    balance = investment  # Set balance to investment amt
    while year <= int(term):  # While loop to print each iteration
        interestEarned = balance * interest / 100  # Calculate interestEarned
        endingBalance = balance + interestEarned  # Calculate endingBalance
        print("%d\t\t$%.2f\t\t\t$%.2f\t\t\t$%.2f" % (year, balance, interestEarned, endingBalance))  # Print
        balance = endingBalance  # Set balance to endingBalance
        year += 1  # Increment year


def main():  # Main function to invoke methods
    investment, interest, term = investInput()  # Set variables from investInput
    formatTable(investment, interest, term)  # Format the table
    finalAmount = investCalc(investment, interest, term)  # Store final amount
    print("\nYour initial investment was $%.2f." % investment)  # Print initial investment
    print("Your final investment amount is $%.2f" % investCalc(investment, interest, term))  # Print final investment
    print("Your net profit is $%.2f." % (finalAmount - investment))  # Print net profit


main()  # Run the program
