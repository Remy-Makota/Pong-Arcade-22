# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 04:56:58 2024

@author: USER-PC
"""

from turtle import Turtle

# Creating a paddle class

class Paddle(Turtle):
    # Initialise the variables in the class
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid= 5, stretch_len= 1)
        self.penup()
        self.goto(position)

    # Initiate the variables/ keystrokes to move the paddle
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

        