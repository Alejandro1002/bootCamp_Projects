# import
from turtle import Turtle

# constants
COORDINATE_R = (100, 220)
COORDINATE_L = (-100, 220)
ALIGN = 'center'
FONT = ('Arial', 50, 'normal')

# CLASS
class ScoreBoard(Turtle):

    # attributes
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.leftScore = 0
        self.rightScore = 0
        self.updatingScoreBoard()

    # update score board
    def updatingScoreBoard(self):
        self.clear()
        self.goto(COORDINATE_R)
        self.write(self.rightScore, align=ALIGN, font=FONT)
        self.goto(COORDINATE_L)
        self.write(self.leftScore, align=ALIGN, font=FONT)

    # score for right paddle
    def scoreForRightPaddle(self):
        self.rightScore += 1
        self.updatingScoreBoard()

    # score for left paddle
    def scoreForLeftPaddle(self):
        self.leftScore += 1
        self.updatingScoreBoard()
