''' Christian Vasquez | 1/21/23 | COMP 150
    Lab 2 - Welcome

    This program takes user input for their first and last names,
    and it prints a welcome statement using their full name.
'''


firstName = input("Enter your first name: ")                                        # Prompts for first name
lastName = input("Enter your last name: ")                                          # Prompts for last name
greetingOne = "Hello there "                                                        # First part of greeting
greetingTwo = ", it is nice to meet you!"                                           # Second part of greeting
print(greetingOne + firstName, lastName + greetingTwo)                              # Print whole sentence