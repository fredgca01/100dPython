from tkinter import END, INSERT, Button, Label, PhotoImage, StringVar, Text, Tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizzInterface:
    def __init__(self, quizz_brain:QuizBrain) :
        self.window = Tk()
        self.window.title("Quizz")
        self.window.config(padx=20,pady=20,background=THEME_COLOR)
        
        self.quizz = quizz_brain

        self.score = StringVar()
        score_label = Label(self.window, textvariable=self.score,background=THEME_COLOR)
        score_label.grid(row=0, column=1)
        self.score.set("Score: 0")
        self.quiz_question = Text(self.window,height=10,width=50,bg="white")
        
        self.quiz_question.grid(row=1,column=0,columnspan=2,padx=20,pady=20)
        
        true_img = PhotoImage(file="./day34/images/true.png")
        true_button = Button(image=true_img, highlightthickness=0, command=self.true)
        true_button.grid(row=2, column=0)
        false_img = PhotoImage(file="./day34/images/false.png")
        false_button = Button(image=false_img, highlightthickness=0, command=self.false)
        false_button.grid(row=2, column=1)

        self.quiz_question.insert(INSERT,self.quizz.next_question())
        
        self.window.mainloop()
    
    def true(self):
        score,is_right = self.quizz.check_answer("True")
        self.score.set(f"Score : {score}")
        if is_right:
            self.quiz_question.config(bg="green")
        else:
            self.quiz_question.config(bg="red")
        self.window.after(500,lambda:self.quiz_question.config(bg="white"))

        self.quiz_question.delete('1.0',END)
        if self.quizz.still_has_questions():
            self.quiz_question.insert(INSERT,self.quizz.next_question())
        else :
            self.quiz_question.insert(INSERT,"You've completed the quizz.")
            self.window.after(3000,lambda:self.window.destroy())

    def false(self):
        score,is_right = self.quizz.check_answer("False")
        self.score.set(f"Score : {score}")
        if is_right:
            self.quiz_question.config(bg="green")
        else:
            self.quiz_question.config(bg="red")
        self.window.after(500,lambda:self.quiz_question.config(bg="white"))
        
        self.quiz_question.delete('1.0',END)
        if self.quizz.still_has_questions():
            self.quiz_question.insert(INSERT,self.quizz.next_question())
        else:
            self.quiz_question.insert(INSERT,"You've completed the quizz.")
            self.window.after(3000,lambda:self.window.destroy())