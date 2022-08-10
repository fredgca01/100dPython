import turtle
from turtle import Turtle, Screen
from random import choice,randint
import colorgram

hirst_paint=[]
colors = colorgram.extract("./day18/Spot-paintings.jpg",100)
for color in colors:
    hirst_paint.append((color.rgb.r,color.rgb.g,color.rgb.b))

#removing white background
for _ in range (5):
    hirst_paint.pop(0)

def random_color():
    rand_color=choice(hirst_paint)
    return rand_color

timmy = Turtle()
timmy.shape("circle")
timmy.speed("fastest")
turtle.colormode(255)
timmy.hideturtle()
timmy.pensize(20)
timmy.penup()
timmy.setposition(-250,-280)
starting_line=[]
starting_line.append(timmy.xcor())
starting_line.append(timmy.ycor())

def setPosition():
    timmy.penup()
    starting_line[1]+=50
    timmy.setx(starting_line[0])
    timmy.sety(starting_line[1])
    
for _ in range(11):
    setPosition()
    for _ in range(10):
        timmy.pendown()
        timmy.color(random_color())
        timmy.stamp()
        timmy.penup()
        timmy.forward(50)

screen = Screen()
screen.exitonclick()
