# import
from turtle import Turtle, Screen
from random import randint

# create canvas
canvas = Screen()
canvas.setup(width=800, height=400)
canvas.title('TURTLE RACE TRACKING')
canvas.bgcolor('white')
userBet = canvas.textinput(title='Turtle',prompt=' MAKE A BET. CHOOSE A TURTLE COLOR FROM THE RAINBOW TO'
                                                 'MAKE YOUR BET: ')

# list of colors
listColors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
yPositing = [150, 100, 50, 0, -50, -100]
listRacers = []

# flag for while loop
shouldContinue = False

# defining racers
for item in range(0, 6):
    turtle = Turtle()
    turtle.shape('turtle')
    turtle.speed(2)
    turtle.penup()
    turtle.goto(x=-380, y=yPositing[item])
    turtle.color(listColors[item])
    # append to list
    listRacers.append(turtle)

# conditional to determine if user has already placed its bet
if userBet:
    shouldContinue = True

# run while loop
while shouldContinue:

    # move the list of racers
    for run in listRacers:

        # catch when the user hits the border
        if run.xcor() > 355:
            # stop the while loop
            shouldContinue = False
            winningColor = run.pencolor()

            if winningColor == userBet:
                print(f'\n YOU HAVE WON THE BET!. THE WINNER IS THE TURTLE COLOR [ {winningColor.upper()} ] \n')

            else:
                print(f'\n YOU HAVE LOST THE BET!. THE WINNER IS THE TURTLE COLOR [ {winningColor.upper()} ] \n')

        # make the turtle run
        randomMovement = randint(0, 10)
        run.forward(randomMovement)

# exit on click
canvas.exitonclick()
