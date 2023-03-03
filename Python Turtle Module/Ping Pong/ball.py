# import
from turtle import Turtle

# constants
COORDINATES = (0, 0)

# CLASS
class RollingBall(Turtle):

    # attributes
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(COORDINATES)
        self.newX = 12
        self.newY = 12
        self.moveSpeed = 0

    # make ball's initial movement
    def initialBallMovement(self):
        moveX = self.xcor() + self.newX
        moveY = self.ycor() + self.newY
        self.goto(x=moveX, y=moveY)

    # bouncing against walls
    def bouncingAxis_Y(self):
        # a num multiply by -1 it becomes its negative num
        self.newY *= -1

    # bouncing against paddle
    def bouncingAxis_X(self):
        # a num multiply by -1 it becomes its negative num
        self.newX *= -1
        # increase speed
        self.moveSpeed *= 0.15

    # reset ball position
    def resetPositionRightMisses(self):
        self.goto(COORDINATES)
        self.moveSpeed *= 0.1
        self.bouncingAxis_X()

    def resetPositionLeftMisses(self):
        self.goto(COORDINATES)
        self.moveSpeed *= 0.15
        self.bouncingAxis_X()