''' Name: Christian Vasquez | 2/26/23 | COMP 150
Lab 1 - vasquezAcronym.py

This program has a function that takes a string as
a param and returns the first letter of each word in
upper-case. It then creates an empty list, converts
the phrase into a list of words, and extracts the
first letter of each word, appending the letter into
acronymList. Converts to uppercase and is returned to main.
'''

def phraseReader():
    phrase = input("Enter a sentence/phrase: ") # Takes user input
    return phrase                               # Returns user input


def getAcronym(phrase):
    words = phrase.split()                      # Split input phrase into list of words
    acronymList = []                            # Create list
    for word in words:                          # For each word
        acronymList.append(word[0].upper())     # Append the first letter of each word to the list
    acronym = ''.join(acronymList)              # Join the letters into a string
    return acronym                              # Return the string


def main():
    phrase = phraseReader()                     # Get input from user
    acronym = getAcronym(phrase)                # Create the acronym
    print("Acronym:", acronym)                  # Print result

main()