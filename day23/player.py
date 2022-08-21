from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def go_up(self) -> None:
        # return True if turtle reach the upper side of the screen
        self.forward(MOVE_DISTANCE)

    def win(self)-> bool:
        return self.ycor()>FINISH_LINE_Y
        
    def reset(self) -> None:
        self.goto(STARTING_POSITION)