from turtle import Turtle, Screen
import prettytable

# timmy = Turtle()
# print(timmy)
# my_screen = Screen()
# print(my_screen.canvheight)
# timmy.shape("turtle")
# timmy.color('green')
# timmy.forward(100)
# my_screen.exitonclick()

table = prettytable.PrettyTable()
table.add_column("Premiere",["test","test2"])
table.add_column("seconde",["test3","test4"])
print(table)