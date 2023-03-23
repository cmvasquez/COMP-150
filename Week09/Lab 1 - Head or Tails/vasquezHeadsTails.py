''' Christian Vasquez | COMP 150 | 3/23/23
    Lab 1 - vasquezHeadsTails.py

    This program simulates a single flip
    of a coin and generates a random sequence
    of 10 heads or tails using a counter while loop
'''
import random                       # Import the random class

def flip():                         # Flips a coin
    if random.randrange(0, 2) == 0: # If the rand num is 0
        print("Heads")              # Print heads
    else:                           # IF the rand num is not 0
        print("Tails")              # Print tails

def main():                         # Main method
    count = 0                       # Initialize counter
    while count < 10:               # While the counter is less than 10
        flip()                      # Flip a coin
        count += 1                  # Increment the counter

main()                              # Run the program