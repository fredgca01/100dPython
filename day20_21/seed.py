from turtle import Turtle
from random import randrange

class Seed(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.speed("fastest")
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.penup()

    def generate_seed(self,height,width)->None:
        self.clearstamps()
        x = randrange(start=-width/2+50,stop=width/2-50)
        y = randrange(start=-height/2+50,stop=height/2-50)
        self.goto(x=x,y=y)
        self.stamp()

    def getXcor(self)->float:
        return self.xcor()
    
    def getYcor(self)->float:
        return self.ycor()
    
    def is_eaten(self,x,y)->bool:
        return self.distance(x=x,y=y) <= 15