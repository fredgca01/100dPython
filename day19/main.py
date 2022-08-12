from turtle import Turtle,Screen

timmy = Turtle()

def move_forward():
    timmy.forward(10)

screen = Screen()
screen.listen()
screen.onkey(fun=move_forward, key="space")

screen.exitonclick()