''' Christian Vasquez | 2/6/23 | COMP 150
    Lab 2 - Animal Mad Lib Revised v3

    This program separately prompts the user for several
    related words then uses them in a mad lib. Uses dictionaries
'''

storyFormat = '''                                       
A long time ago, I think it was the {season} of {year}, I went on the voyage of a lifetime,
a voyage to {city}. On our voyage, we brought {another food} to eat and I even brought my pet
{another animal}. This journey was not for the faint of heart, we encountered many difficulties.
It was day {number} into our journey, and a seaman was looking deep into the water, and he spotted
a wild sea {animal}! It was a whole school of them! Within 2 seconds, the leader {animal} jumped 30
feet out of the water and landed directly on our boat! It had {color} skin, and was oozing blood.
We think it died upon impact, as well as lack of oxygen, as everybody knows that {animal}s are underwater
animals. So we ended up taking it apart and added {animal} meat to our dinner of {food}, which was
absolutely delicious. Thats all the time I have today, thank you.                                                
'''


def tellStory():                                    # Function to put together dictionary and tell story
    userPicks = dict()                              # Define the dictionary we are going to use
    addPick('animal', userPicks)                    # Add a word
    addPick('another animal', userPicks)            # Add a word
    addPick('food', userPicks)                      # Add a word
    addPick('another food', userPicks)              # Add a word
    addPick('city', userPicks)                      # Add a word
    addPick('year', userPicks)                      # Add a word
    addPick('color', userPicks)                     # Add a word
    addPick('number', userPicks)                    # Add a word
    addPick('season', userPicks)                    # Add a word
    story = storyFormat.format(**userPicks)         # Format the story
    print(story)                                    # Print the story


def addPick(cue, dictionary):                       # Function to prompt user for words
    prompt = 'Enter an example for ' + cue + ': '   # Prompt message
    response = input(prompt)                        # Store input in variable response
    dictionary[cue] = response                      # Add the specified response to the dictionary


tellStory()                                         # Run the program
