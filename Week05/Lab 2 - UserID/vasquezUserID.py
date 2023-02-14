''' Christian Vasquez | 2/14/23 | COMP 150
    Lab 2 - User ID

    This program takes user input for a first and last
    name, and then creates a user id using the first
    letter of the first name and the first 6 (or all if
    less) letters of the last name, all in lowercase.
'''

def nameInput():                                            # Function to take user input
    firstName = input("Please enter your first name: ")     # Input first name
    lastName = input("Please enter your last name: ")       # Input last name
    return firstName, lastName                              # Return both


def createID(firstName, lastName):                          # Method to create user ID using first and last
    userID = firstName[0].lower() + lastName[:6].lower()    # Concatenate user ID
    return userID                                           # Return user ID


def main():                                                 # Main function to invoke other functions
    firstName, lastName = nameInput()                       # Set firstName and lastName locally in main
    userID = createID(firstName, lastName)                  # Get userID from firstName and lastName
    print(f"Name: {firstName} {lastName}")                  # Print original name
    print(f"User ID: {userID}")                             # Print user ID

main()                                                      # Run the program

