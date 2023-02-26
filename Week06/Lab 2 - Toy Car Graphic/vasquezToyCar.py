''' Christian Vasquez | COMP 150 | 2/26/23
    Lab 2 - vasquezToyCar.py

    This program draws a car using rectangles
    and circles and places it at the far left of
    the canvas.
'''
from graphics import *

def drawToyCar():
    win = GraphWin("Toy Car", 400, 400)                    # Create window object and set size

    # Draw car body
    body = Rectangle(Point(10, 150), Point(160, 100))      # Create rectangle object
    body.setFill('firebrick2')                             # Color of fill
    body.setOutline('black')                               # Color of outline
    body.setWidth(2)                                       # Set width of outline
    body.draw(win)                                         # Draw into the window

    # Draw car roof
    roof = Rectangle(Point(35, 100), Point(135, 75))       # Create rectangle object
    roof.setFill('deeppink4')                              # Color of fill
    roof.setOutline('black')                               # Color of outline
    roof.setWidth(2)                                       # Set width of outline
    roof.draw(win)                                         # Draw into the window

    # Draw car wheels
    wheel1 = Circle(Point(35, 150), 20)                    # Create circle object
    wheel1.setFill('black')                                # Color of fill
    wheel1.setOutline('black')                             # Color of outline
    wheel1.setWidth(2)                                     # Width of outline
    wheel1.draw(win)                                       # Draw into the window

    wheel2 = Circle(Point(135, 150), 20)                   # Create circle object
    wheel2.setFill('black')                                # Color of fill
    wheel2.setOutline('black')                             # Color of outline
    wheel2.setWidth(2)                                     # Width of outline
    wheel2.draw(win)                                       # Draw into the window

    win.getMouse()                                         # Wait for a mouse click
    win.close()                                            # Close the window

drawToyCar()                                               # Run program
