from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_id = 0

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    global reps
    reps=0
    window.after_cancel(timer_id)
    timer_label.config(text="Timer",fg=GREEN)
    canvas.itemconfig(timer_txt,text="00:00")
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps+=1
    if reps==8:
        timer_label.config(text="BREAK",fg=RED)
        count_down(LONG_BREAK_MIN)
    elif reps%2==0:
        timer_label.config(text="BREAK",fg=PINK)
        count_down(SHORT_BREAK_MIN)
    else:
        timer_label.config(text="WORK",fg=GREEN)
        count_down(WORK_MIN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = math.floor(count/60)
    secondes = count%60
    global timer_id

    canvas.itemconfig(timer_txt,text=f"{minutes:02}:{secondes:02}")
    if count>0:
        timer_id = window.after(1000,count_down, count-1)
    elif reps<8:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro !")
window.minsize(width=200,height=200)
window.config(padx=100,pady=50,bg=YELLOW)

timer_label = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME, 32,"bold"))
timer_label.grid(row=0,column=1)

canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="./day28/tomato.png")
canvas.create_image(100,112,image=img)
timer_txt=canvas.create_text(100,130,fill="white",text="00:00", font=(FONT_NAME, 24,"bold"))
canvas.grid(row=1,column=1)

start_button = Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset",highlightthickness=0, command=reset)
reset_button.grid(row=2,column=3)

window.mainloop()