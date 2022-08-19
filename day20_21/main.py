from turtle import Turtle,Screen, turtles, xcor
from random import randrange
from snake import Snake
from seed import Seed

MAX_HEIGHT=450
MAX_WIDTH=450
screen = Screen()
screen.setup(width=MAX_WIDTH,height=MAX_HEIGHT)
screen.bgcolor("black")
screen.title("Le jeu du Serpent")

snake = Snake()
seed = Seed()
seed.generate_seed(height=MAX_HEIGHT,width=MAX_WIDTH)
def turn_right():
    snake.turn_right()

def turn_left():
    snake.turn_left()

def check_boundaries():
    return snake.check_boundaries(height=MAX_HEIGHT,width=MAX_WIDTH)

def check_seed():
    return seed.is_eaten(snake.getXcor(), snake.getYcor())    

def check_queue():
    return snake.check_queue()

playing=True

screen.listen()

screen.onkey(fun=turn_left,key="q")
screen.onkey(fun=turn_right,key="d")


while playing:
    if not snake.move_snake(MAX_HEIGHT,MAX_WIDTH):
        playing=False
    elif check_seed():
        snake.extend_snake()
        seed.generate_seed(height=MAX_HEIGHT,width=MAX_WIDTH)
        print("MIAM")

screen.exitonclick()