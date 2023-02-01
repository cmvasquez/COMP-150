''' Christian Vasquez | 1/31/23 | COMP 150
    Lab 4 - Mad Lib Revised

    This program separately prompts the user for several
    related words then uses them in a mad lib. Uses dictionaries
'''

storyFormat = '''                                       
A long time ago, I think it was the {season} of {year}, I went on the voyage of a lifetime,
a voyage to {city}. This journey was not for the faint of heart, we encountered many difficulties.
It was day {number} into our journey, and a seaman was looking deep into the water, and he spotted
a wild sea {animal}! It was a whole school of them! Within 2 seconds, the leader {animal} jumped 30
feet out of the water and landed directly on our boat! It had {color} skin, and was oozing blood.
We think it died upon impact, as well as lack of oxygen, as everybody knows that {animal}s are underwater
animals. So we ended up taking it apart and added {animal} meat to our dinner of {food}, which was
absolutely delicious. Thats all the time I have today, thank you.                                                
'''


def tellStory():
    userPicks = dict()
    addPick('animal', userPicks)
    addPick('food', userPicks)
    addPick('city', userPicks)
    addPick('year', userPicks)
    addPick('color', userPicks)
    addPick('number', userPicks)
    addPick('season', userPicks)
    story = storyFormat.format(**userPicks)
    print(story)


def addPick(cue, dictionary):
    '''Prompt for a user response using the cue string,
    and place the cue-response pair in the dictionary.
    '''
    prompt = 'Enter an example for ' + cue + ': '
    response = input(prompt)
    dictionary[cue] = response


tellStory()
