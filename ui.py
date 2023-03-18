from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quiz Guiz")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)
        self.score = Label(text=f"Score: {0}", font=('Ariel', 15, 'italic'),bg=THEME_COLOR,fg="white",pady=20)
        self.score.grid(column=1, row=0)



        self.canvas=Canvas(width=350, height=300,bg="white")
        self.question_text = self.canvas.create_text(175, 150, width=280,text="Some Question text", font=('Ariel', 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2,pady=20)

        self.image_true= PhotoImage(file="images/true.png")
        self.true_button=Button(image= self.image_true,highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0,row=2)
        self.image_false = PhotoImage(file="images/false.png")
        self.false_button = Button(image= self.image_false, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            q_text=self.quiz.next_question()
            self.canvas.itemconfig( self.question_text, text=q_text)
            self.score.config(text=f"Score:{self.quiz.score}")
        else:
            self.canvas.config(bg="yellow")
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_pressed(self):
        self.feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        result=self.quiz.check_answer("False")
        self.feedback(result)

    def feedback(self,result):
        if result:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,self.get_next_question)


