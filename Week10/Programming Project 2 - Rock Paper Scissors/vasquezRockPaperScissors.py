''' Christian Vasquez | COMP 150 | 4/2/23
    Programming Project 2 - vasquezRockPaperScissors.py

    This program allows the user to play rock paper scissors
    against a computer opponent making use of random choices.
    It keeps track of score, and allows the user to quit at any
    time by pressing the quit button. The game is played in a
    graphic window.
'''
from graphics import *
import random

# Define window and button dimensions
win = GraphWin("Rock-Paper-Scissors", 400, 300)
win.setCoords(0, 0, 4, 3)

# Draw rock button
rockButton = Rectangle(Point(0.5, 0.5), Point(1.5, 1.5))
rockButton.setFill("gray")
rockButton.draw(win)
rockLabel = Text(Point(1, 1), "ROCK")
rockLabel.draw(win)

# Draw paper button
paperButton = Rectangle(Point(1.5, 0.5), Point(2.5, 1.5))
paperButton.setFill("blue")
paperButton.draw(win)
paperLabel = Text(Point(2, 1), "PAPER")
paperLabel.draw(win)

# Draw scissors button
scissorsButton = Rectangle(Point(2.5, 0.5), Point(3.5, 1.5))
scissorsButton.setFill("orange")
scissorsButton.draw(win)
scissorsLabel = Text(Point(3, 1), "SCISSORS")
scissorsLabel.draw(win)

# Draw quit button
quitButton = Rectangle(Point(1.5, 2), Point(2.5, 2.5))
quitButton.setFill("red")
quitButton.draw(win)
quitLabel = Text(Point(2, 2.25), "QUIT")
quitLabel.setTextColor("white")
quitLabel.draw(win)

# Define score variables
playerScore = 0
computerScore = 0


def getPlayerChoice():  # Function to get player's choice
    while True:  # While the player has not made a choice
        clickPoint = win.getMouse()  # Get the point the mouse clicks on
        if 0.5 <= clickPoint.getX() <= 1.5 and 0.5 <= clickPoint.getY() <= 1.5:  # Rock button
            return "ROCK"
        elif 2.5 >= clickPoint.getX() >= 1.5 >= clickPoint.getY() >= 0.5:  # Paper button
            return "PAPER"
        elif 2.5 <= clickPoint.getX() <= 3.5 and 0.5 <= clickPoint.getY() <= 1.5:  # Scissors button
            return "SCISSORS"
        elif 1.5 <= clickPoint.getX() <= 2.5 and 2 <= clickPoint.getY() <= 2.5:  # Quit button
            return "quit"


def getComputerChoice():  # Function to get computer choice
    choices = ["ROCK", "PAPER", "SCISSORS"]  # Either rock, paper, or scissors
    return random.choice(choices)  # Pick a random one, return


def determineWinner(playerChoice, computerChoice):  # Function to determine the winner
    global playerScore, computerScore  # Global variables to access across program

    if playerChoice == computerChoice:  # If both player and cpu choose same
        return "tie"  # It's a tie
    elif (playerChoice == "ROCK" and computerChoice == "SCISSORS") or (  # If player beats computer
            playerChoice == "PAPER" and computerChoice == "ROCK") or (
            playerChoice == "SCISSORS" and computerChoice == "PAPER"):
        playerScore += 1  # Increase player score
        return "player"  # Player wins
    else:  # If not,
        computerScore += 1  # Increase computer score
        return "computer"  # Computer wins


def updateScoreDisplay():  # Function to update scoreboard
    global playerScoreLabel, computerScoreLabel  # Global variables to access across program

    if playerScoreLabel:
        playerScoreLabel.setText("Player: " + str(playerScore))
    else:
        playerScoreLabel = Text(Point(1.5, 2.75), "Player: " + str(playerScore))
        playerScoreLabel.draw(win)

    if computerScoreLabel:
        computerScoreLabel.setText("Computer: " + str(computerScore))
    else:
        computerScoreLabel = Text(Point(2.5, 2.75), "Computer: " + str(computerScore))
        computerScoreLabel.draw(win)


def main():  # Main function to run the program
    global playerScore, computerScore, playerScoreLabel, computerScoreLabel  # Global variables to access across pgm

    # Draw initial score display
    playerScoreLabel = Text(Point(1.5, 2.75), "Player: " + str(playerScore))
    playerScoreLabel.draw(win)
    computerScoreLabel = Text(Point(2.5, 2.75), "Computer: " + str(computerScore))
    computerScoreLabel.draw(win)

    while True:
        playerChoice = getPlayerChoice()  # Get player choice

        computerChoice = getComputerChoice()  # Get computer choice

        winner = determineWinner(playerChoice, computerChoice)  # Determine winner

        updateScoreDisplay()  # Update score display

        # Display choices and winner
        playerChoiceLabel = Text(Point(.75, 2), "You: " + (playerChoice))
        playerChoiceLabel.draw(win)
        computerChoiceLabel = Text(Point(3.25, 2), "CPU: " + computerChoice)
        computerChoiceLabel.draw(win)

        if playerChoice == "quit":      # If player clicked quit
            break                       # Close program
        elif winner == "tie":           # If it's a tie
            resultLabel = Text(Point(2, 1.8), "It's a tie!")
        elif winner == "player":        # If player wins
            resultLabel = Text(Point(2, 1.8), "You win!")
        else:                           # If computer wins
            resultLabel = Text(Point(2, 1.8), "Computer wins!")
        resultLabel.draw(win)           # Draw the result label

        # Wait for click before continuing
        nextGameLabel = Text(Point(2, .25), "Click anywhere to play again")
        nextGameLabel.draw(win)
        clickPoint = win.getMouse()
        nextGameLabel.undraw()

        # Clear labels and score display
        playerChoiceLabel.undraw()
        computerChoiceLabel.undraw()
        resultLabel.undraw()

    playerScoreLabel.undraw()
    computerScoreLabel.undraw()
    win.close()


main()  # Run the program
