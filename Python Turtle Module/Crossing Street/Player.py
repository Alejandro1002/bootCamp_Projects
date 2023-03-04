# import
from turtle import Turtle
from CONS import PLAYER_MOVE_DISTANCE, PLAYER_HEADING, PLAYER_FINISH_LINE, PLAYER_START_POSITION

# class
class TurtlePlayer(Turtle):

    # attributes
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.movingOnYAxis = PLAYER_MOVE_DISTANCE
        self.setheading(PLAYER_HEADING)
        self.penup()
        self.goto(PLAYER_START_POSITION)

    # moving forward
    def movingPlayerForward(self):
        new_Y = self.ycor() + self.movingOnYAxis
        self.goto(x=self.xcor(), y=new_Y)

    # if player reaches the top line
    def reachingTheTopLine(self):
        if self.ycor() > PLAYER_FINISH_LINE:
            return True

    # reset player to its original position
    def resettingToOriginalPosition(self):
        self.goto(PLAYER_START_POSITION)

