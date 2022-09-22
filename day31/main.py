from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
TIMER=5000
try :
    data = pandas.read_csv("./day31/data/still_learning.csv")
    print("still_learning.csv")
except FileNotFoundError :
    data = pandas.read_csv("./day31/data/dico GB_FR.csv")
    print("dico GB_FR.csv")
data_dict={row.FR:row.GB for (index,row) in data.iterrows()}
#data_dict = data.to_dict(orient="records")
french_words = [row.FR for (index,row) in data.iterrows()]
english_words= [row.GB for (index,row) in data.iterrows()]

print(f"FR: {len(french_words)}, GB: {len(english_words)}")
french=""
english=""
flip_timer=""

def next_card():
    global french,english,french_words,english_words
    french = choice(list(data_dict.keys()))
    english = data_dict[french]
    french_words.remove(french)
    english_words.remove(english)
    return english

def display_question():
    global flip_timer
    if flip_timer!="":
        window.after_cancel(flip_timer)
    english = next_card()
    canvas.itemconfig(canvas_image, image=img_front)
    canvas.itemconfig(txt,text=english)
    canvas.itemconfig(title_txt,text="English")
    flip_timer = window.after(TIMER,func=display_answer)

def display_answer():
    global french,flip_timer
    if flip_timer!="":
        window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=img_back)
    canvas.itemconfig(txt,text=french)
    canvas.itemconfig(title_txt,text="Francais")
    french_words.append(french)
    english_words.append(english)
    flip_timer = window.after(TIMER,func=display_question)

def save():
    global french_words,english_words
    try :
        df = pandas.DataFrame({"FR":french_words,"GB":english_words})
        df.to_csv("./day31/data/still_learning.csv",mode="w", index=False)
    except Exception as msg :
        print(msg)
    finally:
        window.destroy()

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.config(highlightthickness=0)

window.protocol("WM_DELETE_WINDOW",  save)

canvas = Canvas(width=820,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
img_front = PhotoImage(file="./day31/images/card_front.png")
img_back = PhotoImage(file="./day31/images/card_back.png")
canvas_image = canvas.create_image(400,263,image=img_front)
title_txt=canvas.create_text(400,150,text="English",font=("Arial", 40,"italic"))
txt=canvas.create_text(400,263,text="Text",font=("Arial", 60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

wrong_image = PhotoImage(file="./day31/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0,command=display_answer)
wrong_button.grid(row=1,column=0)
right_image = PhotoImage(file="./day31/images/right.png")
right_button = Button(image=right_image, highlightthickness=0,command=display_question)
right_button.grid(row=1,column=1)

english=next_card()
canvas.itemconfig(txt,text=english)

window.mainloop()