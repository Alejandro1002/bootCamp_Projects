# import
from turtle import Turtle
from CONS import GAME_OVER, FONT, FONT_LEVEL

# class
class ScoreBoard(Turtle):

    # attributes
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color('yellow')
        self.penup()
        self.gameOver = GAME_OVER
        self.goto(x=-280, y=260)
        self.updatingScoreBoardMessage()

    # turtle has reached a car
    def gameOverMessage(self):
        self.goto(x=0, y=0)
        self.write(arg=self.gameOver, align='center', font=FONT)

    # level message
    def updatingScoreBoardMessage(self):
        self.write(arg=f'Level: {self.level}', align='left', font=FONT_LEVEL)

    # updating level
    def levelUpMessage(self):
        self.clear()
        self.level += 1
        self.updatingScoreBoardMessage()
