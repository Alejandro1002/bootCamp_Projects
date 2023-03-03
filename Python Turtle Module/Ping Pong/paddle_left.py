# import
from turtle import Turtle

# constants
COORDINATES = (-378, 0)

# CLASS
class PaddlesPlayerLeft(Turtle):

    # attributes
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('red')
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.penup()
        self.goto(COORDINATES)


    # moving paddles up
    def movingPaddleUp(self):
        new_y = self.ycor() + 35
        self.goto(x=self.xcor(), y=new_y)

    def movingPaddleDown(self):
        new_y = self.ycor() - 35
        self.goto(x=self.xcor(), y=new_y)

