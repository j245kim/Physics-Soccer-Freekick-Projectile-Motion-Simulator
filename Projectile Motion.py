# #----------------------------------------------------------------------------
# # Created By  : Jinwoo Kim
# # Created Date: 05/12/2023
# # version ='1.0'
# # ---------------------------------------------------------------------------

#The code uses turtle, pygame, math, tkinter, if statements, functions, and many variables.
#By using these, the ball's direction is determined and it will move based on projectile motion!

##########################################################################################################

#Part 1: Basic settings before starting the game

import turtle 
from turtle import* 
import tkinter as tk  
from tkinter import*
import pygame 
import math #for trigonometry
  

root=Tk()  
root.title('Free Kick Game') 
canvas = tk.Canvas(root)  
canvas.configure(width=1470,height=770, bg='white')
canvas.pack(side=RIGHT) 

screen = TurtleScreen(canvas)
#register Son's shape
screen.register_shape("son.gif")
screen.addshape("son.gif")

#register goalkeeper
screen.register_shape("lloris.gif")
screen.addshape("lloris.gif")

#register wall
screen.register_shape("wall.gif")
screen.addshape("wall.gif")

#register ball
screen.register_shape("ball.gif")
screen.addshape("ball.gif")

#Intro background 
screen.bgpic("back1.gif")

#Part 2: Function that runs my game
def intro():
  #Remove GUI (button) 
  button1.place_forget()
  button2.place_forget()
  score_pen = turtle.RawTurtle(screen)
  score_pen.ht()
  score_pen.up()
  score_pen.goto (-30,0)
  #Change background
  screen.bgpic("back2.gif")
  score_pen.color("red")
  score_pen.write("Beep!", False, align="left", font=("Times New Roman",30, "normal"))
  pygame.time.wait (2300)
  score_pen.clear()

  score_pen.up()
  score_pen.goto (-400,0)
  score_pen.write("You have earned a chance to take a free kick!", False, align="left", font=("Times New Roman",30, "normal"))
  pygame.time.wait (2300)
  score_pen.clear()

  #Put the player on the screen
  son = turtle.RawTurtle(screen) 
  son.shape("son.gif")
  son.up()    
  son.goto(-400,-70) 

  #Put the gk on the screen
  keeper = turtle.RawTurtle(screen)
  keeper.shape("lloris.gif")
  keeper.up()
  keeper.goto(400,100)

  #Put the wall on the screen
  wall = turtle.RawTurtle(screen)
  wall.shape("wall.gif")
  wall.up()
  wall.goto(0,50)

  #Put the ball on the screen
  ball = turtle.RawTurtle(screen)
  ball.shape("ball.gif")
  ball.up()
  ball.goto(-330,-100)

  pygame.time.wait (1000)

  #Move the player toward the ball
  son.goto(-350,-70) 

  pygame.time.wait (500)

  #Ask for velocity, angle
  velocity =  int(screen.numinput("What velocity are you kicking the ball?", "Enter here in m/s:"))
  angle = int(screen.numinput("What angle are you kicking the ball?", "Enter here:"))
  real_angle = angle * 3.14/180 

  #Formula utilized
  time = (2*(velocity * math.sin(real_angle)))/9.8 
  distance_x = velocity * math.cos(real_angle) * time
  distance_y = velocity * math.sin(real_angle) * time- 0.5*-9.8*time**2

  pygame.time.wait (1000)

  #Where the ball goes is adjusted to ratio of my screen.
  ball.goto(int(distance_x)*6.5,int(distance_y/1.2))

  real_distance_x = distance_x*6.5
  real_distance_y = distance_y/1.2

  #Goal restrictions/conditions
  if real_distance_x > 370 and real_distance_x < 680 and real_distance_y >0 and real_distance_y <250:
    score_pen.write("GOAL!!!", False, align="left", font=("Times New Roman",30, "normal"))
  else:
    score_pen.write("YOU MISSED!!!", False, align="left", font=("Times New Roman",30, "normal"))

  screen.update()
  clock.tick(60)  #Limit the loop to 60 frames per second (my computer can't handle more)

#https://www.youtube.com/watch?v=Y4xlUNfrvow
#https://www.concepts-of-physics.com/mechanics/projectiles.php 

#Part 3: Another function created, when player clicks quit option then the game shuts down.
def quit():
    root.destroy()


#Part 4: side settings that assist my game
# Initialize pygame
pygame.init()

# Set the clock for pygame
clock = pygame.time.Clock()

#GUI location
button1 = tk.Button(master=root, text='Start', bg='orange', height=2, width=20, command=intro)
button1.place(x=450, y=440)

button2 = tk.Button(master=root, text='Quit', bg='orange', height=2, width=20, command=quit)
button2.place(x=450, y=500)

#Get the game loop going!
root.mainloop()