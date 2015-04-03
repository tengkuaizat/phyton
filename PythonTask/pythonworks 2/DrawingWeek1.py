from graphics import *
from random import randint
import random
import time

# Read in and print out the data in the data file
datafile = open("data.txt",'r')


# Do some simple drawing
window = GraphWin("Visualisation", 400, 400)

i = 0
for line in datafile:
        print(line)
        i += 5
        num = int(float(line))
        txt = Text(Point(300,150),line)
        txt.setFill(color_rgb(num,255,255))
        ball = Circle(Point(300,150),num)
        ball.setFill(color_rgb(num,num,num))
        ball.setWidth(0)
        ball.draw(window)
        txt.draw(window)
        time.sleep(0.1)
        ball.undraw()
        txt.undraw()

        box = Rectangle(Point(i,i), Point(i+5,400))
        box.setFill(color_rgb(num,num,num))
        box.setWidth(0)
        box.draw(window)
        

#box = Rectangle(Point(200,50),Point(250,150))
#box.setOutline(color_rgb(255,0,0))
#box.draw(window)

#line = Line(Point(200,200),Point(250,280))
#line.setWidth(4)
#line.draw(window)

#text = Text(Point(50,200),"Hello")
#text.draw(window)

# Waits until the mouse is clicked before closing the window
#window.getMouse()
