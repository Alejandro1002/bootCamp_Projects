# import
from turtle import Turtle

# constants
ALIGN = 'center'
FONT = ('Arial', 18, 'bold')

# set up the class
class SnakeScore(Turtle):

    # attributes
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.setposition(x=0, y=270)
        # call updating score
        self.updatingScoreBoard()

    # update score board
    def updatingScoreBoard(self):
        self.write(arg=f'SCORE: {self.score}', move=False, align=ALIGN, font=FONT)

    # game over text
    def gameOverText(self):
        self.setposition(x=0, y=0)
        self.write(arg='GAME OVER', move=False, align=ALIGN, font=FONT)

    # increase score
    def increasingScoreBoard(self):
        self.score += 1
        # clear the screen
        self.clear()
        # call the update function
        self.updatingScoreBoard()
