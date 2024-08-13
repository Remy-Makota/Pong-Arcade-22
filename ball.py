# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 05:46:14 2024

@author: USER-PC
"""

from turtle import Turtle

# Creating a ball class

class Ball(Turtle):
    # Initialise the variables in the class
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # Function to move the ball
    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Function to move the ball in the y direction
    def bounce_y(self):
        self.y_move *= -1

    # Function to move the ball in the x direction
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    # Function to reset after missing the paddle
    def reset_position(self):
        self.home()
        self.move_speed = 0.1
        self.bounce_x()
