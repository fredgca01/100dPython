from turtle import Turtle,Screen, turtles, xcor
from random import randrange
from scoreboard import Scoreboard
from snake import Snake
from seed import Seed
import time

MAX_HEIGHT=450
MAX_WIDTH=450
screen = Screen()
screen.setup(width=MAX_WIDTH,height=MAX_HEIGHT)
screen.bgcolor("black")
screen.title("Le jeu du Serpent")
screen.tracer(0)

snake = Snake()
seed = Seed()
score = Scoreboard()

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

def reset():
    snake.reset()
    score.reset()

playing=True

screen.listen()

screen.onkey(fun=turn_left,key="q")
screen.onkey(fun=turn_right,key="d")


while playing:
    time.sleep(0.1)
    if not snake.move_snake(MAX_HEIGHT,MAX_WIDTH):
        time.sleep(2)
        reset()
        seed.generate_seed(height=MAX_HEIGHT,width=MAX_WIDTH)
    elif check_seed():
        score.increase_score()
        snake.extend_snake()
        seed.generate_seed(height=MAX_HEIGHT,width=MAX_WIDTH)
    screen.update()

screen.exitonclick()