# import
from turtle import Turtle
from random import randint

# create class
class SnakeFood(Turtle):

    # set up attributes
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        # funct that moves around the food
        self.movingAroundFood()

    # moving around food
    def movingAroundFood(self):
        newX = randint(-280, 280)
        newY = randint(-280, 260)
        self.goto(x=newX, y=newY)


