from turtle import Turtle, Screen
import turtle
from random import choice,randint

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.speed("fastest")
turtle.colormode(255)

#timmy.penup()
#timmy.setx(-300)

# for _ in range(0,4):
#     timmy.forward(100)
#     timmy.right(-90)

# for _ in range (50):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)

#colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# for face in range(4,10):
#     timmy.color(choice(colours))
#     for _ in range(face):
#         timmy.forward(100)
#         timmy.right(360/face)

def random_color():
    rand_color=(randint(0,255),randint(0,255),randint(0,255))
    return rand_color

# angles=[0,90,180,270]
# timmy.width(10)
# while True:
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(choice(angles))

gap = 2
for _ in range (int(360/gap)) :
    timmy.color(random_color())
    timmy.circle(100)
    timmy.setheading(timmy.heading()+gap)

screen = Screen()
screen.exitonclick()

