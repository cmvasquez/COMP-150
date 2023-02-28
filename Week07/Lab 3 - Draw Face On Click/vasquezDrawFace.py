''' Christian Vasquez | COMP 150 | 2/28/23
    Lab 3 - vasquezDrawFace.py

    This program allows the user to click in
    a window as many times as they want and
    draws a face using their mouse click as the
    center point
'''

from graphics import *


def main():
    win = GraphWin('Face', 275, 250)                                                # give title and dimensions
    win.yUp()                                                                       # make right side up coordinates!

    message = Text(Point(win.getWidth() / 2, 20), 'Click anywhere to draw a face.') # Click anywhere to draw face
    message.draw(win)                                                               # Add message to window

    while True:                                                                     # While the program is still running
        clickPoint = win.getMouse()                                                 # Get mouse click location
        head = Circle(clickPoint, 25)                                               # set center and radius
        head.setFill("yellow")                                                      # Head color
        head.draw(win)                                                              # Draw head

        eye1 = Circle(Point(clickPoint.getX() - 10, clickPoint.getY() + 5), 5)      # Get eye1 relative to click
        eye1.setFill('blue')                                                        # Eye1 color
        eye1.draw(win)                                                              # Draw eye1

        eye2 = Line(Point(clickPoint.getX() + 5, clickPoint.getY() + 5),            # Get eye2 relative to click
                    Point(clickPoint.getX() + 15, clickPoint.getY() + 5))           # set endpoints
        eye2.setWidth(3)                                                            # Set eye width
        eye2.draw(win)                                                              # Draw eye

        mouth = Oval(Point(clickPoint.getX() - 10, clickPoint.getY() - 10),         # Get mouth relative to click
                     Point(clickPoint.getX() + 10, clickPoint.getY() - 15))         # set corners of bounding box
        mouth.setFill("red")                                                        # Mouth color
        mouth.draw(win)                                                             # Draw mouth

    win.close()

main()
