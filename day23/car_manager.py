from turtle import Turtle
from random import choice, randint
from car import Car


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2

class CarManager():
    def __init__(self) -> None:
        self.garage = []
        self.current_step = STARTING_MOVE_DISTANCE

    def buildCar(self) -> Car:
        car = Car()
        car.color(choice(COLORS))
        car.goto(x=280,y=randint(-240,240))
        return car
    
    def generateCars(self) -> None:
        for _ in range(randint(1,3)):
            self.garage.append(self.buildCar())

    def move(self):
        for car in self.garage:
            car.forward(self.current_step)

    def speedUp(self):
        self.current_step+=MOVE_INCREMENT

    def clean(self):
        for car in self.garage:
            if car.xcor()<-350:
                self.garage.remove(car)
                car.clear()

    def hit(self,turtle) -> bool:
        for car in self.garage:
            if turtle.distance(car)<=10:
                return True
