from turtle import Screen
from racket import Racket
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PONG Game")

playerOne = Racket(x=350,y=0)
playerTwo = Racket(x=-350,y=0)
ball = Ball()
score = Scoreboard()

screen.listen()

screen.onkey(fun=playerOne.go_up,key="l")
screen.onkey(fun=playerOne.go_down,key="m")
screen.onkey(fun=playerTwo.go_up,key="q")
screen.onkey(fun=playerTwo.go_down,key="s")

gaming=True
while gaming:
    if not ball.move(playerOne,playerTwo):
        #gaming=False
        if ball.xcor()>=360 :
            score.increase_score("right")
        elif ball.xcor()<=-360:
            score.increase_score("left")
        ball.reset_position()

screen.exitonclick()

