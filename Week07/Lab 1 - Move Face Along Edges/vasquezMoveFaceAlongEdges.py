''' Christian Vasquez | COMP 150 | 2/28/23
    Lab 1 - vasquezMoveFaceAlongEdges.py

    This program draws a face in a window
    and moves the face around the 4 edges of
    the window
'''
from graphics import *
import time

def moveAll(shapeList, dx, dy):                                     # Move all shapes in shapeList by (dx, dy)
    for shape in shapeList:
        shape.move(dx, dy)

def moveAllOnLine(shapeList, dx, dy, repetitions, delay):           # Animate the shapes along a line
    for i in range(repetitions):
        moveAll(shapeList, dx, dy)
        time.sleep(delay)

def moveFace(win, faceList):                                        # Move the face along the four edges of the window
    moveAllOnLine(faceList, 5, 0, 40, .05)                          # Move right
    moveAllOnLine(faceList, 0, 5, 30, .05)                          # Move down
    moveAllOnLine(faceList, -5, 0, 40, .05)                         # Move left
    moveAllOnLine(faceList, 0, -5, 30, .05)                         # Move up


def main():
    win = GraphWin('Face', 275, 275)                                # give title and dimensions
    win.yUp()                                                       # make right side up coordinates!

    head = Circle(Point(40,100), 25)                                # set center and radius
    head.setFill("yellow")
    head.draw(win)

    eye1 = Circle(Point(30, 105), 5)
    eye1.setFill('blue')
    eye1.draw(win)

    eye2 = Line(Point(45, 105), Point(55, 105))                     # set endpoints
    eye2.setWidth(3)
    eye2.draw(win)

    mouth = Oval(Point(30, 90), Point(50, 85))                      # set corners of bounding box
    mouth.setFill("red")
    mouth.draw(win)

    label = Text(Point(100, 120), 'A face')                         # Label
    label.draw(win)

    faceList = [head, eye1, eye2, mouth]                            # Create faceList
    moveFace(win, faceList)                                         # Move face along edges

    message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close()

main()                                                              # Run program
