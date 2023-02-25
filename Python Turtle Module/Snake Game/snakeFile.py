# import
from turtle import Turtle

# constants
XCORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# set up the snake class. Inherit from Turtle
class SnakeBody(Turtle):

    # attributes
    def __init__(self):
        super().__init__()
        self.snakeBody = []
        # build the snake body with funct
        self.creatingBody()
        # set up the head of snake
        self.head = self.snakeBody[0]

    # creating segments of snake body
    def creatingSegmentsOfSnake(self, position):
        body = Turtle('square')
        body.color('white')
        body.penup()
        body.goto(position)

        self.snakeBody.append(body)

    # creating the body
    def creatingBody(self):
        for item in XCORDINATES:
            self.creatingSegmentsOfSnake(position=item)

    # when snake takes a food it grows. Add a new segment to the last position of the snake list
    # Position() func from Turtle allows the set the position for the element that's being added
    def extendsSnakeBody(self):
        self.creatingSegmentsOfSnake(position=self.snakeBody[-1].position())

    # move the snake around
    def movingSnakeAround(self):

        for item in range(len(self.snakeBody)-1, 0, -1):
            # move a body segment to the second-last position and so on
            newX = self.snakeBody[item-1].xcor()
            newY = self.snakeBody[item-1].ycor()
            self.snakeBody[item].goto(x=newX, y=newY)

        self.head.forward(MOVE)

    # adding directions and restrictions
    def movingUp(self):
        # if current position NOT poiting DOWN, then allow to point up
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def movingDown(self):
        # if current position NOT poiting UP, then allow to point down
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def movingRight(self):
        # if current position NOT poiting LEFT, then allow to point right
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def movingLeft(self):
        # if current position NOT poiting RIGHT, then allow to point left
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)








