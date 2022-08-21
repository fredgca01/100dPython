
from turtle import Turtle


class Car(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("square")
        self.speed("slow")
        self.setheading(180)
        self.turtlesize(stretch_wid=1,stretch_len=2)
        self.penup()