''' Christian Vasquez | 1/31/2023 | COMP 150
    HW 1 - vasquezMaxMinMortgage.py

    This program calculates and outputs the maximum
    and minimum monthly mortgage payment based on
    user inputs of gross monthly income and monthly
    debt payments. Uses two global variables and 3
    functions
'''

maxMortgageRate = 0.36                                                            # Global max mortgage rate
minMortgageRate = 0.28                                                            # Global min mortgage rate

def inputIncomeAndDebt():                                                         # Method to get user input
    monthlyGross = int(input('Enter your gross monthly income: $'))               # First input
    monthlyDebt = int(input('Enter your monthly debt payment: $'))                # Second input
    return monthlyGross, monthlyDebt                                              # Return both inputs


def mortgageCalculation(monthlyGross, monthlyDebt):                               # Method to calculate max/min mortgage
    maxMortgage = float((monthlyGross - monthlyDebt) * maxMortgageRate)           # Compute maximum amount
    minMortgage = (monthlyGross - monthlyDebt) * minMortgageRate                  # Compute minimum amount
    return maxMortgage, minMortgage                                               # Return both results


def main():                                                                       # Main function to call functions
    monthlyGross, monthlyDebt = inputIncomeAndDebt()                              # Assign vars to result of inputs
    maxMortgage, minMortgage = mortgageCalculation(monthlyGross, monthlyDebt)     # Assign vars to result of mortgage
    print('Gross Monthly Income: ${0:4d}\nMonthly Debt Payments: ${1:3d} '        # Print results
          '\nMaximum Monthly Mortgage: ${2:3.2f} \nMinimum Monthly Mortgage: '
          '${3:4.2f}'.format(monthlyGross, monthlyDebt, maxMortgage, minMortgage), end='')


main()                                                                            # Run program

