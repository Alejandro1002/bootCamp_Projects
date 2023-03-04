# import
from random import choice, randint
from turtle import Turtle
from CONS import CAR_COLORS, CAR_HEADING, CAR_START_MOVING, CAR_MOVING_INCREMENT

# class
class CarManager(Turtle):

    # attributes
    def __init__(self):
        super().__init__()
        self.carList = []
        self.carSpeed = CAR_START_MOVING

    # generate car
    def creatingCars(self):
        # add little delay to cars that appear on canvas
        randomChoice = randint(1,6)
        if randomChoice == 1:
            newCar = Turtle()
            newCar.shape('square')
            newCar.shapesize(stretch_wid=1, stretch_len=2)
            newCar.color(choice(CAR_COLORS))
            newCar.setheading(CAR_HEADING)
            newCar.penup()
            newCar.goto(x=300, y=randint(-250, 260))
            self.carList.append(newCar)

    # moving cars backwards
    def movingCarsBackwards(self):
        for item in self.carList:
            item.backward(self.carSpeed)

    # increasing cars speed
    def increasingCarSpeed(self):
        self.carSpeed += CAR_MOVING_INCREMENT

