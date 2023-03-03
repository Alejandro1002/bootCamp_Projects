# import
from turtle import Screen
from time import sleep
from paddle_right import PaddlesPlayerRight
from paddle_left import PaddlesPlayerLeft
from score_file import ScoreBoard
from ball import RollingBall
import CONS as cnst

# create the screen
canvas = Screen()
canvas.setup(width=800, height=600)
canvas.title('PONG GAME')
canvas.bgcolor('black')
# turning animation on/off
canvas.tracer(0)

# calling objects
paddleRight = PaddlesPlayerRight()
paddleLeft = PaddlesPlayerLeft()
ball = RollingBall()
score = ScoreBoard()

# event listeners & controllers
canvas.listen()

# keyboard commands
canvas.onkey(key='p', fun=paddleRight.movingPaddleUp)
canvas.onkey(key='l', fun=paddleRight.movingPaddleDown)
canvas.onkey(key='w', fun=paddleLeft.movingPaddleUp)
canvas.onkey(key='s', fun=paddleLeft.movingPaddleDown)

# flag while loop
shouldContinue = True

while shouldContinue:

    # add delay on the screen
    sleep(0.1)
    # update screen when tracer is turn off (0 given)
    canvas.update()

    # initial move
    ball.initialBallMovement()

    # detect collision with wall and bounce
    if ball.ycor() > cnst.UPPER_BORDER or ball.ycor() < cnst.LOWER_BORDER:

        ball.bouncingAxis_Y()

    # detect collision with paddles
    if ball.distance(paddleRight) < cnst.DISTANCE and ball.xcor() > cnst.PADDLE_LINE_R or ball.distance(paddleLeft) < cnst.DISTANCE \
            and ball.xcor() < cnst.PADDLE_LINE_L:

        ball.bouncingAxis_X()

    # detect collision when paddle misses
    if ball.xcor() > cnst.GOAL_LINE_R:
        ball.resetPositionRightMisses()
        # keep score
        score.scoreForLeftPaddle()

    if ball.xcor() < cnst.GOAL_LINE_L:
        ball.resetPositionLeftMisses()
        # keep score
        score.scoreForRightPaddle()


canvas.exitonclick()