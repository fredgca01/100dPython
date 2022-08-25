from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score=0
        self.highscore=0
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 14, "bold"))
        self.goto(100,200)
        self.write(f"High Score: {self.highscore}", align="center", font=("Arial", 14, "bold"))

    def increase_score(self):
        self.score+=1
        if self.score>self.highscore:
            self.highscore=self.score
        self.update_score()

    def reset(self):
        self.score=0
        self.update_score()