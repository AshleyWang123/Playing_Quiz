import tkinter as tk
import tkinter.messagebox
from tkinter import *

class NewQuestionQuiz1(Frame):
    def __init__(self, master, **kw):
        # Initialise Questionnaire Class
        super().__init__(master, **kw)
        master.attributes("-zoomed", True)
        master.title("Write New Multiple Choice Question")
        self.master = master
        self.frame = tk.Frame(self.master)

        self.master.configure(bg="#9bb1d6", )
        self.configure(bg="#9bb1d6", )

        # Stores the user input into variables
        self.txtQuestion = Entry(self)
        self.txtAnswerA = Entry(self)
        self.txtAnswerB = Entry(self)
        self.txtAnswerC = Entry(self)
        self.txtAnswerD = Entry(self)
        self.txtCorrectAnswer = Entry(self)
        self.grid()
        self.create_question()

    # Sets up the display window
    def create_question(self):
        self.enter_question()
        lblClickSubmit = Label(self, text='Click "Submit Question" to save question when done',
                               bg="#9bb1d6", fg="white",font=('MS', 12))
        lblClickSubmit.grid(row=1, column=2, columnspan=6, sticky=W)

        lblSuggestedInput = Label(self, text='Example of Input Format',  bg="#9bb1d6",
                                  fg="white",font=('MS', 10, 'bold'))
        lblSuggestedInput.grid(row=1, column=9, columnspan=6, sticky=W + E)

        lblSpace = Label(self, text='',bg="#9bb1d6", fg="white")
        lblSpace.grid(row=3, column=3)
        lblSpace = Label(self, text='', bg="#9bb1d6", fg="white",font=('MS', 8, 'bold'))
        lblSpace.grid(row=4, column=3)

        lblEnterQuestion = Label(self, text='Enter New Question:', bg="#9bb1d6", fg="white",font=('MS', 12, 'bold'))
        lblEnterQuestion.grid(row=5, column=0, sticky=E)
        lblExampleQuestion = Label(self, text='What Colour is the sky?',bg="#9bb1d6", fg="white", font=('MS', 12))
        lblExampleQuestion.grid(row=5, column=9)

        lblSpace.grid(row=5, column=0)
        lblSpace = Label(self, text='        ', bg="#9bb1d6", fg="white",font=('MS', 8, 'bold'))
        lblSpace.grid(row=6, column=4)
        lblSpace = Label(self, text='', bg="#9bb1d6", fg="white",font=('MS', 8, 'bold'))
        lblSpace.grid(row=7, column=0)

        lblAnswerA = Label(self, text='Enter the Answer for Option A:', bg="#9bb1d6", fg="white",font=('MS', 12, 'bold'))
        lblAnswerA.grid(row=8, column=0, sticky=E)
        lblExampleQuestion = Label(self, text='A - Green',bg="#9bb1d6", fg="white", font=('MS', 12))
        lblExampleQuestion.grid(row=8, column=9, sticky=W)

        lblAnswerB = Label(self, text='Enter the Answer for Option B:', bg="#9bb1d6", fg="white",font=('MS', 12, 'bold'))
        lblAnswerB.grid(row=9, column=0, sticky=E)
        lblExampleQuestion = Label(self, text='B - Orange', bg="#9bb1d6", fg="white",font=('MS', 12))
        lblExampleQuestion.grid(row=9, column=9, sticky=W)

        lblAnswerC = Label(self, text='Enter the Answer for Option C:', bg="#9bb1d6", fg="white",font=('MS', 12, 'bold'))
        lblAnswerC.grid(row=10, column=0, sticky=E)
        lblExampleQuestion = Label(self, text='C - Blue', bg="#9bb1d6", fg="white",font=('MS', 12))
        lblExampleQuestion.grid(row=10, column=9, sticky=W)

        lblAnswerD = Label(self, text='Enter the Answer for Option D:',bg="#9bb1d6", fg="white", font=('MS', 12, 'bold'))
        lblAnswerD.grid(row=11, column=0, sticky=E)
        lblExampleQuestion = Label(self, text='D - Purple', bg="#9bb1d6", fg="white",font=('MS', 12))
        lblExampleQuestion.grid(row=11, column=9, sticky=W)

        lblSpace = Label(self, text='', bg="#9bb1d6", fg="white",font=('MS', 8, 'bold'))
        lblSpace.grid(row=12, column=0)
        lblSpace = Label(self, text='', bg="#9bb1d6", fg="white",font=('MS', 8, 'bold'))
        lblSpace.grid(row=13, column=0)
        lblSpace = Label(self, text='',bg="#9bb1d6", fg="white", font=('MS', 8, 'bold'))
        lblSpace.grid(row=14, column=0)

        lblCorrectAnswer = Label(self, text='Enter the Correct Answer "Option" (A, B, C, or D):',
                                 bg="#9bb1d6", fg="white",  font=('MS', 12, 'bold'))
        lblCorrectAnswer.grid(row=15, column=0, sticky=E)
        lblExampleQuestion = Label(self, text='C', bg="#9bb1d6", fg="white",font=('MS', 12))
        lblExampleQuestion.grid(row=15, column=8, sticky=W)

        lblSpace.grid(row=15, column=5)
        lblSpace.grid(row=16, column=6)

    # Sets up the user input boxes and buttons
    def enter_question(self):
        self.txtQuestion.grid(row=5, column=2, columnspan=5, sticky=W + E, padx = 10, pady = 10, ipady = 10)

        self.txtAnswerA.grid(row=8, column=2, columnspan=5, sticky=W + E, padx = 10, pady = 10, ipady = 10)

        self.txtAnswerB.grid(row=9, column=2, columnspan=5, sticky=W + E, padx = 10, pady = 10, ipady = 10)

        self.txtAnswerC.grid(row=10, column=2, columnspan=5, sticky=W + E, padx = 10, pady = 10, ipady = 10)

        self.txtAnswerD.grid(row=11, column=2, columnspan=5, sticky=W + E, padx = 10, pady = 10, ipady = 10)

        self.txtCorrectAnswer.grid(row=15, column=2, columnspan=5, sticky=W + E, padx = 10, pady = 10, ipady = 10)

        butSubmit = Button(self, text='Submit Question', bg="white", font=('MS', 10, 'bold'),
                           command=lambda: self.storeResponse(self.txtQuestion, self.txtAnswerA, self.txtAnswerB,
                                                              self.txtAnswerC, self.txtAnswerD, self.txtCorrectAnswer))
        butSubmit.grid(row=17, column=2)

        butClear = Button(self, text='Next Question',bg="white",
                          font=('MS', 10, 'bold'), command=lambda: self.clearInput())
        butClear.grid(row=17, column=3)
        lblClickSubmit = Label(self,
                               text='Click "Next Question" to write a new question',
                               bg="#9bb1d6", fg="white", font=('MS', 12))
        lblClickSubmit.grid(row=2, column=2, sticky=W)

        butStartQuiz = Button(self, text='Return to Main Menu',bg="white",
                              font=('MS', 10, 'bold'), command=self.close_windows)
        butStartQuiz.grid(row=0, column=0)

    def close_windows(self):
        self.master.destroy()

    # Clears the form so the user can write another question
    def clearInput(self):
        self.txtQuestion.delete(0, END)
        self.txtAnswerA.delete(0, END)
        self.txtAnswerB.delete(0, END)
        self.txtAnswerC.delete(0, END)
        self.txtAnswerD.delete(0, END)
        self.txtCorrectAnswer.delete(0, END)

    # Takes user input and writes to file
    # Sets up and user error warnings such as not providing all question answers etc.
    def storeResponse(self, new_question, new_answer_a, new_answer_b, new_answer_c, new_answer_d, new_correct_answer):

        user_question = new_question.get()
        user_question_a = new_answer_a.get()
        user_question_b = new_answer_b.get()
        user_question_c = new_answer_c.get()
        user_question_d = new_answer_d.get()
        user_correct_answer = new_correct_answer.get().upper()

        if user_question_a == "" or user_question_b == "" or user_question_c == "" or user_question_d == "":
            tkinter.messagebox.showinfo("ERROR", "You Need To Supply All Answers!")
        elif user_question == "":
            tkinter.messagebox.showinfo("ERROR", "You Need To Supply A Question!")
        elif user_correct_answer == "":
            tkinter.messagebox.showinfo("ERROR", "You Need To Supply A Correct Answer!")
        elif not user_correct_answer.isalpha():
            tkinter.messagebox.showinfo("ERROR", "The Correct Answer must be \nA, B, C or D")
        elif len(user_correct_answer) >= 2:
            tkinter.messagebox.showinfo("ERROR", "You Entered more than ONE letter\n\n"
                                                 "The Correct Answer must be \nA, B, C or D")
        else:
            file = open("questionsQuiz1.txt", "a")  # append to file

            file.write("\n")
            file.write(user_question)
            file.write("\n")
            file.write(user_question_a)
            file.write("\n")
            file.write(user_question_b)
            file.write("\n")
            file.write(user_question_c)
            file.write("\n")
            file.write(user_question_d)
            file.write("\n")
            file.write(user_correct_answer)
            file.close()
            tkinter.messagebox.showinfo("Success", "New Question has been saved to file")
            root1.lift()



root1 = tk.Tk()
root1.title("Write New Question")
root1.attributes("-zoomed", True)
app = NewQuestionQuiz1(root1)
