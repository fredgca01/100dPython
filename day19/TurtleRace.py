from turtle import Turtle,Screen
from random import randint,choice

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
turtles = {}

def create_turtle()-> Turtle:
    timmy=Turtle()
    timmy.shape("turtle")
    return timmy

def starting():
    for index in range(0,len(colors)):
        turtle = create_turtle()
        turtle.color(colors[index])
        turtles[index]=turtle
    y_pos=-200
    for turtle in turtles.values():
        turtle.penup()
        turtle.goto(x=-250,y=y_pos)
        y_pos+=50

def race():
    racing=True
    print("La course est partie ! ")
    while racing:
        for turtle in turtles.values():
            turtle.forward(randint(0,20))
            if(turtle.xcor()>250):
                racing=False
                print(f"le gagnant est {turtle.color()}")
                break

screen = Screen()
screen.setup(width=600,height=500)

another_race=True
while another_race:
    starting()
    answer = screen.textinput("La Course !!","Quel sera le vainqueur de la course ? Donne le numéro.")
    race()
    answer = screen.textinput("La Course !!","Une autre course ? (O/N).").lower()
    if answer=="n":
        another_race=False
    else :
        screen.clear()
    
screen.exitonclick()
