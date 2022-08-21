from random import randint
import time
from turtle import Screen
from car import Car
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

RYTHM=0.5
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
garage = CarManager()
garage.generateCars()

def go_up():
    player.go_up()

screen.listen()
screen.onkey(fun=go_up,key="z")

game_is_on = True
turn=0
while game_is_on:
    time.sleep(0.1)
    garage.move()
    garage.generateCars()
    garage.clean()
    if player.win():
        score.update()
        garage.speedUp()
        player.reset()
    elif garage.hit(player):
        game_is_on=False
        score.game_over()
    screen.update()

screen.exitonclick()