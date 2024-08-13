# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 05:59:31 2024

@author: USER-PC
"""

from turtle import Turtle

class ScoreBoard(Turtle):
    # Initialise the scoreboard class
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    # Function to update the scoreboard after every play
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align= 'center', font= ('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align= 'center', font= ('Courier', 80, 'normal'))

    # Function to update the left paddle score
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    # Function to update the right paddle score
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
