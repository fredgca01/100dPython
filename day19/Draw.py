from turtle import Turtle,Screen, heading

timmy = Turtle()

def clean_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

def move(gap):
    timmy.forward(gap)

def backward():
    move(-10)

def forward():
    move(10)

def right():
    timmy.right(10)

def left():
    timmy.left(10)

screen = Screen()
screen.listen()

screen.onkey(fun=clean_screen,key="c")
screen.onkeypress(fun=forward,key="z")
screen.onkeypress(fun=backward,key="s")
screen.onkey(fun=right,key="d")
screen.onkey(fun=left,key="q")



screen.exitonclick()