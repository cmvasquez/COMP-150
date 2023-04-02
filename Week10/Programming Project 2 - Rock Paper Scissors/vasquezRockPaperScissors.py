''' Christian Vasquez | COMP 150 | 4/2/23
    Programming Project 2 - vasquezRockPaperScissors.py


'''
from graphics import *
import random

# Define window and button dimensions
win = GraphWin("Rock-Paper-Scissors", 400, 300)
win.setCoords(0, 0, 4, 3)

# Draw buttons
rock_button = Rectangle(Point(0.5, 0.5), Point(1.5, 1.5))
rock_button.setFill("gray")
rock_button.draw(win)
rock_label = Text(Point(1, 1), "ROCK")
rock_label.draw(win)

paper_button = Rectangle(Point(1.5, 0.5), Point(2.5, 1.5))
paper_button.setFill("blue")
paper_button.draw(win)
paper_label = Text(Point(2, 1), "PAPER")
paper_label.draw(win)

scissors_button = Rectangle(Point(2.5, 0.5), Point(3.5, 1.5))
scissors_button.setFill("orange")
scissors_button.draw(win)
scissors_label = Text(Point(3, 1), "SCISSORS")
scissors_label.draw(win)

quit_button = Rectangle(Point(1.5, 2), Point(2.5, 2.5))
quit_button.setFill("red")
quit_button.draw(win)
quit_label = Text(Point(2, 2.25), "QUIT")
quit_label.setTextColor("white")
quit_label.draw(win)

# Define score variables
player_score = 0
computer_score = 0

# Define function to get player choice
def get_player_choice():
    while True:
        click_point = win.getMouse()
        if click_point.getX() >= 0.5 and click_point.getX() <= 1.5 and click_point.getY() >= 0.5 and click_point.getY() <= 1.5:
            return "ROCK"
        elif click_point.getX() >= 1.5 and click_point.getX() <= 2.5 and click_point.getY() >= 0.5 and click_point.getY() <= 1.5:
            return "PAPER"
        elif click_point.getX() >= 2.5 and click_point.getX() <= 3.5 and click_point.getY() >= 0.5 and click_point.getY() <= 1.5:
            return "SCISSORS"
        elif click_point.getX() >= 1.5 and click_point.getX() <= 2.5 and click_point.getY() >= 2 and click_point.getY() <= 2.5:
            return "quit"
            break

# Define function to get computer choice
def get_computer_choice():
    choices = ["ROCK", "PAPER", "SCISSORS"]
    return random.choice(choices)

# Define function to determine winner
def determine_winner(player_choice, computer_choice):
    global player_score, computer_score

    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "ROCK" and computer_choice == "SCISSORS") or (
            player_choice == "PAPER" and computer_choice == "ROCK") or (
            player_choice == "SCISSORS" and computer_choice == "PAPER"):
        player_score += 1
        return "player"
    else:
        computer_score += 1
        return "computer"

def update_score_display():
    global player_score_label, computer_score_label

    if player_score_label:
        player_score_label.setText("Player: " + str(player_score))
    else:
        player_score_label = Text(Point(1.5, 2.75), "Player: " + str(player_score))
        player_score_label.draw(win)

    if computer_score_label:
        computer_score_label.setText("Computer: " + str(computer_score))
    else:
        computer_score_label = Text(Point(2.5, 2.75), "Computer: " + str(computer_score))
        computer_score_label.draw(win)

def main():
    global player_score, computer_score, player_score_label, computer_score_label

    # Draw initial score display
    player_score_label = Text(Point(1.5, 2.75), "Player: " + str(player_score))
    player_score_label.draw(win)
    computer_score_label = Text(Point(2.5, 2.75), "Computer: " + str(computer_score))
    computer_score_label.draw(win)

    player_choice = ""

    while True:
        # Get player choice
        player_choice = get_player_choice()

        # Get computer choice
        computer_choice = get_computer_choice()

        # Determine winner
        winner = determine_winner(player_choice, computer_choice)

        # Update score display
        update_score_display()

        # Display choices and winner
        player_choice_label = Text(Point(.75, 2), "You: " + (player_choice))
        player_choice_label.draw(win)

        computer_choice_label = Text(Point(3.25, 2), "CPU: " + computer_choice)
        computer_choice_label.draw(win)

        if player_choice == "quit":
            break
        elif winner == "tie":
            result_label = Text(Point(2, 1.8), "It's a tie!")
        elif winner == "player":
            result_label = Text(Point(2, 1.8), "You win!")
        else:
            result_label = Text(Point(2, 1.8), "Computer wins!")
        result_label.draw(win)

        # Wait for click before continuing
        click_point = win.getMouse()

        # Clear labels and score display
        player_choice_label.undraw()
        computer_choice_label.undraw()
        result_label.undraw()

    player_score_label.undraw()
    computer_score_label.undraw()
    win.close()


main()