from turtle import Turtle, Vec2D

class Snake:
    def __init__(self) -> None:
        self.main_turtle=Turtle()
        self.main_turtle.speed("normal")
        self.main_turtle.shape("square")
        self.main_turtle.shapesize(0.5,0.5)
        self.main_turtle.color("white")
        self.main_turtle.penup()
        self.snake = {}
        self.snake[self.main_turtle.stamp()]=self.main_turtle.position()

    def move_snake(self,height,width)->bool:
        snakebis = self.snake.copy()
        for stampid in snakebis.keys():
            self.main_turtle.clearstamp(stampid)
            self.snake.pop(stampid)
            self.main_turtle.forward(3)
            self.snake[self.main_turtle.stamp()]=self.main_turtle.position()
            if not self.check_queue() or not self.check_boundaries(height=height,width=width):
                return False
            else:
                return True
            

    def extend_snake(self)->None:
        #snake increase by one after eating a seed
        for _ in range (0,10):
            self.main_turtle.forward(3)
            self.snake[self.main_turtle.stamp()]=self.main_turtle.position()

    def turn_right(self)->None:
        self.main_turtle.right(90)

    def turn_left(self)->None:
        self.main_turtle.left(90)

    def getXcor(self)->float:
        return self.main_turtle.xcor()
    
    def getYcor(self)-> float:
        return self.main_turtle.ycor()

    def check_boundaries(self, height, width) -> bool:
        # return true if screen boundaries are not crossed       
        if self.getXcor()>=width/2 or self.getXcor()<=-width/2:
            self.write("Explosion contre le mur !! \n GAME OVER")
            return False
        elif self.getYcor()>=height/2 or self.getYcor()<=-height/2:
            self.write("Explosion contre le mur !! \n GAME OVER")
            return False
        else :
            return True
    
    def check_queue(self) -> bool:
        # return true if snake is not crossed
        values = list(self.snake.values())
        values.pop()
        for position in values:
            if self.main_turtle.distance(position)<=2:
                self.write("Cannibale !! \n GAME OVER")
                return False
        return True
    
    def write(self, text):
        self.main_turtle.hideturtle()
        self.main_turtle.home()
        self.main_turtle.write(text, align="center", font=("Arial", 12, "bold"))

    def reset(self):
        self.main_turtle.clear()
        self.main_turtle.home()
        self.snake = {}
        self.snake[self.main_turtle.stamp()]=self.main_turtle.position()
