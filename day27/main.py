import tkinter

window = tkinter.Tk()
window.title("Test UI")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

label = tkinter.Label(text="sample label", font=("Arial", 24,"bold"))
label.grid(column=0,row=0)
label["text"]="Reviewed label"
label.config(padx=10,pady=10)

def add(*args):
    total=0
    for n in args:
        total+=n
    return total

button = tkinter.Button(text="Click")
button.grid(column=1,row=1)

button = tkinter.Button(text="new")
button.grid(column=2,row=0)

input = tkinter.Entry()
input.grid(column=3,row=2)

def button_clicked():
    label["text"]=input.get()

button["command"]=button_clicked


window.mainloop()