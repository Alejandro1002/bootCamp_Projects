# import
from turtle import Screen
from time import sleep
from snakeFile import SnakeBody
from foodFile import SnakeFood
from scoreFile import SnakeScore

# create the canvas
canvas = Screen()
canvas.setup(width=600, height=600)
canvas.title('SNAKE GAME')
canvas.bgcolor('black')
# set up the tracer to reset the updates of screen layers
canvas.tracer(0)

# instance objects
snake = SnakeBody()
food = SnakeFood()
score = SnakeScore()

# make the screen to listen
canvas.listen()

# give the commands to the screen
canvas.onkey(key='Up', fun=snake.movingUp)
canvas.onkey(key='Down', fun=snake.movingDown)
canvas.onkey(key='Left', fun=snake.movingLeft)
canvas.onkey(key='Right', fun=snake.movingRight)

# set the while loop flag
shouldContinue = True

while shouldContinue:

    # call update screen for transitioning
    canvas.update()

    # add a little delay whenever
    sleep(0.1)

    # move the snake
    snake.movingSnakeAround()

    # detect collisions with food
    if snake.head.distance(food) < 15:

        # move around food
        food.movingAroundFood()

        # add a segment to the snake
        snake.extendsSnakeBody()

        # increase score
        score.increasingScoreBoard()

    # detect collisions with walls
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # change flag
        shouldContinue = False
        # print game over
        score.gameOverText()

    # detect collisions with the tail [1:] excludes the first element on the array. the snake head
    for segment in snake.snakeBody[1:]:
        if snake.head.distance(segment) < 10:
            shouldContinue = False
            score.gameOverText()

# exit on click
canvas.exitonclick()