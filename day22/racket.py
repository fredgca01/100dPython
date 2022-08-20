from turtle import Turtle

class Racket(Turtle):
    def __init__(self,x,y) -> None:
        super().__init__()
        self.speed("slow")
        self.shape("square")
        self.color("white")
        self.left(90)
        self.turtlesize(stretch_wid=1,stretch_len=5)
        self.penup()
        self.goto(x=x,y=y)

    def go_up(self):
        if self.ycor()<250: 
            self.forward(20)

    def go_down(self):
        if self.ycor()>-250:
            self.backward(20)

    def pong(self,ball) -> bool:
        # return True if racket bounce the ball
        if self.distance(ball)<40 and (self.xcor()>330 or self.xcor()<-330):
            return True
