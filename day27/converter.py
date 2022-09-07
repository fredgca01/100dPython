from tkinter import *

window = Tk()
window.title("Miles to Km converter")
window.minsize(width=200,height=200)
window.config(padx=20,pady=20)

miles_input = Entry()
miles_input.grid(column=1,row=0)
Label(text="Miles").grid(column=2,row=0)
Label(text="is equals to").grid(column=0,row=1)
result = Label(text="0")
result.grid(column=1,row=1)
Label(text="Km").grid(column=2,row=1)
button = Button(text="Calculate")
button.grid(column=1,row=2)


def button_clicked():
    result["text"]=round(int(miles_input.get())/0.62137,3)

button["command"]=button_clicked


window.mainloop()
