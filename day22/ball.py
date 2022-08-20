from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.speed("slow")
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(randint(0,270))

    def checkCollision(self):
        # return True if walls are crossed
        return self.ycor()>=275 or self.ycor()<=-275
    
    def checkExit(self):
        # return True if ball exit from the game
        return self.xcor()>=365 or self.xcor()<=-365

    def display(self, text):
        self.hideturtle()
        self.home()
        self.write(text, align="center", font=("Arial", 12, "bold"))

    def bounce(self,angle)-> None:
        self.setheading(angle-self.heading())

    def reset_position(self):
        self.hideturtle()
        self.goto(0,0)
        self.setheading(randint(0,270))
        self.showturtle()

    def move(self,one, two) -> bool:
        self.forward(5)
        if self.checkCollision():
            self.bounce(360)
        elif self.checkExit():
            return False
        elif one.pong(self):
            self.bounce(180)
        elif two.pong(self):
            self.bounce(180)
        return True