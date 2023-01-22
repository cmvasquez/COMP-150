''' Christian Vasquez | 1/21/23 | COMP 150
    Lab 3 - 1.10.3 vasquezAdd3.py (p 27 Dr Harrington)

    This program prompts the user for three
    integers, lists all three, then prints their sum.
'''

x = int((input("Enter an integer: ")))                  # Prompts user for first integer
y = int((input("Enter a 2nd integer: ")))               # Prompts user for second integer
z = int((input("Enter a final integer: ")))             # Prompts user for third integer
sum = x + y + z                                         # Adds the three integers together into sum
print('The sum of ' + str(x) + ', ' + str(y) +          # Print result and the integers
      ', and ' + str(z) + ' is ' + str(sum) + '.')