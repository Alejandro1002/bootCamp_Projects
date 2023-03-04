# import
from CONS import TITLE_CANVAS
from turtle import Screen
from Player import TurtlePlayer
from Cars import CarManager
from Score import ScoreBoard
from time import sleep

# set up canvas
canvas = Screen()
canvas.setup(width=600, height=600)
canvas.title(TITLE_CANVAS)
canvas.bgcolor('black')
canvas.tracer(0)

# calling objects
player = TurtlePlayer()
cars = CarManager()
score = ScoreBoard()

# screen listener
canvas.listen()

# controls
canvas.onkey(key='Up', fun=player.movingPlayerForward)

# while loop
shouldContinue = True

while shouldContinue:
    # add delay
    sleep(0.1)

    # update screen
    canvas.update()

    # make cars appear and move
    cars.creatingCars()
    cars.movingCarsBackwards()



    # detect if player collision with any car
    for item in cars.carList:
        if item.distance(player) <= 21:
            shouldContinue = False
            # print game over
            score.gameOverMessage()

    # detect if player reaches the top line
    if player.reachingTheTopLine():
        # back to start
        player.resettingToOriginalPosition()
        # speed up cars
        cars.increasingCarSpeed()
        # update scoreboard
        score.levelUpMessage()

# exit on click
canvas.exitonclick()

