''' Christian Vasquez | 1/31/2023 | COMP 150
    Lab 1 - vasquezDollarConversion.py

    This program prompts the user to input a number
    in US dollars, and then converts them to Pesos
    and Canadian Dollars. Conversion rates captured
    1/31/23 7:24PM UTC from Google Finance
'''

mxnConversionRate = 18.82                                                   # USD to MXN conversion rate (1/31/23)
cadConversionRate = 1.33                                                    # USD to CAD conversion rate (1/31/23)


def usdToMXN(usd):                                                          # Method to convert USD to MXN
    mxn = float(usd * mxnConversionRate)                                    # Conversion equation
    return mxn                                                              # Return variable


def usdToCAD(usd):                                                          # Method to convert USD to CAD
    cad = float(usd * cadConversionRate)                                    # Conversion equation
    return cad                                                              # Return variable


def main():                                                                 # Main function
    usd = float(input('Please enter a dollar amount (2 decimals): $'))      # User input
    print('US Dollars: $%.2f' % usd + '\nMexican Pesos: $%.2f'              # Print results
          % (usdToMXN(usd)) + '\nCanadian Dollars: $%.2f' % usdToCAD(usd))


main()                                                                      # Run program
