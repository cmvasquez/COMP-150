''' Christian Vasquez | 1/21/23 | COMP 150
    Week01 - Mad Lib

    This program separately prompts the user for several
    related words then uses them in a mad lib.
'''

animalOne = input("Enter an animal: ")                                                      # Prompts for animal
animalTwo = input("Enter a second animal: ")                                                # Prompts for second animal
noun = input("Enter a noun (object): ")                                                     # Prompts for object
actionVerb = input("Enter an action verb: ")                                                # Prompts for action verb
print("I was at the zoo yesterday. I really enjoy looking at the animals"                   # Print mad lib
      ", \nespecially the " + animalOne +
      "s. I also got to see the " + animalTwo + "s,"
      " but \nthey didnt seem to like me, one of them was " +
      actionVerb + " all \nover the place, and another one threw a " + noun + " at me!")