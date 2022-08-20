from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align="center", font=("Arial", 20, "bold"))
        self.goto(100,200)
        self.write(self.r_score, align="center", font=("Arial", 20, "bold"))

    def increase_score(self,player):
        if player == "right":
            self.r_score+=1
            self.update_score()
        else :
            self.l_score+=1
            self.update_score()