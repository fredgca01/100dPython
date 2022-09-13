from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pwd() -> None:
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    lettersNb = random.randint(5,8)
    numbersNb = random.randint(1,3)
    specialsNb = random.randint(1,2)

    result= []
    for num in range(0,lettersNb):
        result.append(random.choice(letters))
    for num in range(0,numbersNb):
        result.append(random.choice(numbers))
    for num in range(0,specialsNb):
        result.append(random.choice(symbols)) 
    random.shuffle(result)
    result_txt = "".join(result)
    pyperclip.copy(result_txt)
    pwd_entry.insert(0,result_txt)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save() -> None :
    if len(website_entry.get())!=0 or len(pwd_entry.get())!=0:
        if messagebox.askyesno(message="Do you want to save this new entry ?"):
            with open("./day29/data.txt",mode="a") as file:
                file.write(f"{website_entry.get()}||{login_entry.get()}||{pwd_entry.get()}\n")
            website_entry.delete(0,END)
    else :
        messagebox.showerror(title="oooops !", message="Cannot save empty message")
    pwd_entry.delete(0,END)
    website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
#window.minsize(width=200,height=200)
window.config(padx=50,pady=50,bg="white")

canvas = Canvas(width=200,height=200,bg="white", highlightthickness=0)
img = PhotoImage(file="./day29/logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)

Label(text="Website:",fg="black",bg="white").grid(row=1,column=0)
Label(text="email/username:",fg="black",bg="white").grid(row=2,column=0)
Label(text="Password:",fg="black",bg="white").grid(row=3,column=0)
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1, columnspan=2)
website_entry.focus()
login_entry = Entry(width=35)
login_entry.grid(row=2,column=1, columnspan=2)
login_entry.insert(INSERT,"fredgca@gmail.com")
pwd_entry = Entry(width=26)
pwd_entry.grid(row=3,column=1)
pwd_button = Button(text="Generate",width=30, command=generate_pwd)
pwd_button.grid(row=3,column=2)
add_button = Button(text="Add",width=30, command=save)
add_button.grid(row=4,column=1, columnspan=2)
pwd_button = Button(text="Generate",width=30, command=generate_pwd)
pwd_button.grid(row=3,column=2, columnspan=2)


window.mainloop()