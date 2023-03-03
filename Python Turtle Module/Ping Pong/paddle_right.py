# import
from turtle import Turtle

# constant
COORDINATE = (370, 0)

# CLASS
class PaddlesPlayerRight(Turtle):

    # attributes
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('blue')
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.penup()
        self.goto(COORDINATE)

    # moving paddles up
    def movingPaddleUp(self):
        new_y = self.ycor() + 35
        self.goto(x=self.xcor(), y=new_y)

    # moving paddles down
    def movingPaddleDown(self):
        new_y = self.ycor() - 35
        self.goto(x=self.xcor(), y=new_y)
