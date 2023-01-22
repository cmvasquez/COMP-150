# Welcome
# This program takes user input for their first and last names,
# and it prints a welcome statement using their full name.
# Written by Christian Vasquez COMP 150 1/21/23


firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
greetingOne = "Hello there "
greetingTwo = ", it is nice to meet you! I am simply a program, so by the time" \
              " \nyou are reading this I will have ceased to exist."
print(greetingOne + firstName, lastName + greetingTwo)