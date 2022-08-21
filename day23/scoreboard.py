from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(x=-280,y=250)
        self.level=0
        self.update()

    def update(self):
        self.clear()
        self.level+=1
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)