# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 04:45:49 2024

@author: USER-PC
"""

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# Inititating a screen instance
screen = Screen()
screen.screensize(canvheight= 600, canvwidth= 800)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
# To control the right paddle
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')

# To control the left paddle
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

# Create the ball & scoreboard class
ball = Ball()
results = ScoreBoard()

# To manually update the content of the screen
game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    
    # Detect a collision with the wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
        
    # Detect a collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    # Detect a right paddle miss
    if ball.xcor() > 360 :
        ball.reset_position()
        results.l_point()
        
    # Detect a left paddle miss
    if ball.xcor() < -360 :
        ball.reset_position()  
        results.r_point()
        
# Exit prompt
screen.exitonclick()