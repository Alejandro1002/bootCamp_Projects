# import
import turtle
from turtle import Turtle, Screen
from colorgram import extract
from random import choice

# extracting colors from image
def gettingColorsFromImage():
    colors = extract('image.jpg', 15)
    paletteColors = colors

    palette = []

    for item in range(0, len(paletteColors)):
        color = paletteColors[item]
        r = color.rgb[0]
        g = color.rgb[1]
        b = color.rgb[2]

        # create tuple to store colors
        rgb = (r, g, b)
        palette.append(rgb)

    return palette

hirst_palette = gettingColorsFromImage()

# defining canvas
canvas = Screen()
canvas.bgcolor('white')
canvas.title('THE HIRST PAINTING')
canvas.setup(width=800, height=650)

# defining turtle object as dotsOnScreen
dotsOnScreen = Turtle()
dotsOnScreen.shape('arrow')
dotsOnScreen.speed('fastest')

# getting random colors from turtle class
turtle.colormode(255)

# defining coordinates
dotsOnScreen.penup()
# hide the object
dotsOnScreen.hideturtle()
# set cordinates x and y
dotsOnScreen.setx(x=-380)
dotsOnScreen.sety(y=-300)

# moving first 10 rows
def movingFirstTenRows():
    for item in range(1, 10):
        dotsOnScreen.pendown()
        dotsOnScreen.dot(30, choice(hirst_palette))
        dotsOnScreen.penup()
        dotsOnScreen.forward(75)
        dotsOnScreen.pendown()
        dotsOnScreen.dot(30, choice(hirst_palette))

# moving backwards leaving no dots
def movingBackwardsTenRows():
    # to move to the left on the screen
    dotsOnScreen.setheading(90)
    dotsOnScreen.penup()
    dotsOnScreen.forward(75)
    dotsOnScreen.left(90)
    dotsOnScreen.forward(675)
    # to set direction back to right
    dotsOnScreen.setheading(0)

# calling functions
for item in range(1, 10):

    movingFirstTenRows()

    movingBackwardsTenRows()

# exit canvas
canvas.exitonclick()


