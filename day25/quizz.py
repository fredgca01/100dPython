from turtle import Turtle,Screen
import pandas

screen = Screen()
screen.title("Quizz des regions de France")
screen.addshape("./day25/franceRegions.gif")

turtle = Turtle()
turtle.shape("./day25/franceRegions.gif")
writer = Turtle()
writer.penup()
writer.hideturtle()
scoreboard = Turtle()
scoreboard.penup()
scoreboard.hideturtle()


gaming=True
score = 0
guessed=[]

regions_data = pandas.read_csv("./day25/franceRegions.csv")

def get_mouse_click_coor(x, y):
    print(x, y)

def update_score():
    scoreboard.clear()
    scoreboard.goto(-100,200)
    scoreboard.write(f"Score: {score}", align="center", font=("Arial", 14, "bold"))

while gaming:
    #turtle.onclick(get_mouse_click_coor)
    answer = screen.textinput(f"{len(guessed)}/17 regions","Donne moi un nom de région française: ")
    if answer==None:
        gaming=False
    else:
        region = regions_data[regions_data.name==answer]
        if not region.empty and guessed.count(answer)==0:
            print(region)
            writer.goto(int(region.x),int(region.y))
            writer.write(answer)
            score+=1
            update_score()
            guessed.append(answer)
        elif guessed.count(answer)!=0:
            print("Déjà dit")
        else : 
            print("Non, ca n'existe pas")

notguessed_data={}
name=[]
x=[]
y=[]
# for value in regions_data.name.items():
#      if value[1] not in guessed:
#         row = regions_data[regions_data.name == value[1]]
#         name.append(row.name)
#         x.append(row.x)
#         y.append(row.y)

result = regions_data[(~regions_data["name"].isin(guessed))]
print(result["name"])
result.to_csv("./day25/toLearn.csv")

screen.exitonclick()