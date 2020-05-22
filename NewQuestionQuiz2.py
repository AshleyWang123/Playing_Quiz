import tkinter as tk
import tkinter.messagebox
from tkinter import *

class NewQuestionQuiz2(Frame):
    def __init__(self, master, **kw):
        # Initialise Questionnaire Class
        super().__init__(master, **kw)
        master.attributes("-zoomed", True)
        master.title("Write New Matching Pairs Question")
        self.master = master
        self.frame = tk.Frame(self.master)

        self.master.configure(bg="#9bb1d6", )
        self.configure(bg="#9bb1d6", )

        # Stores the user input into variables
        self.txtQuestion = Entry(self)
        self.Match1 = Entry(self)
        self.Answer1 = Entry(self)
        self.Match2 = Entry(self)
        self.Answer2 = Entry(self)
        self.Match3 = Entry(self)
        self.Answer3 = Entry(self)
        self.grid()
        self.create_question()

    # Sets up the display window
    def create_question(self):
        self.enter_question()
        lblClickSubmit = Label(self, text='Click "Submit Question" to save question when done',bg="#9bb1d6",
                                  fg="white",font=('MS', 12))
        lblClickSubmit.grid(row=1, column=2, columnspan=6, sticky=W)

        lblSuggestedInput = Label(self, text='Example of Input Format', bg="#9bb1d6",
                                  fg="white",font=('MS', 12, 'bold'))
        lblSuggestedInput.grid(row=1, column=9, columnspan=6, sticky=W + E)

        lblSpace = Label(self, text='',bg="#9bb1d6", fg="white",)
        lblSpace.grid(row=3, column=3)
        lblSpace = Label(self, text='',bg="#9bb1d6", fg="white", font=('MS', 8, 'bold'))
        lblSpace.grid(row=4, column=3)

        lblEnterQuestion = Label(self, text='Enter New Question:', bg="#9bb1d6",
                                  fg="white",font=('MS', 12, 'bold'))
        lblEnterQuestion.grid(row=5, column=0, sticky=E)
        lblExampleQuestion = Label(self, text='Match the Fruit and Colours', bg="#9bb1d6",
                                  fg="white",font=('MS', 12))
        lblExampleQuestion.grid(row=5, column=9)
        back = Label(self, text='             ', bg="#9bb1d6")
        back.grid(row=5, column=8)

        lblSpace.grid(row=5, column=0)
        lblSpace = Label(self, text='        ', bg="#9bb1d6",
                                  fg="white",font=('MS', 8, 'bold'))
        lblSpace.grid(row=6, column=4)
        lblSpace = Label(self, text='', bg="#9bb1d6",
                                  fg="white",font=('MS', 8, 'bold'))
        lblSpace.grid(row=7, column=0)

        lblAnswerA = Label(self, text='Enter the First Match:',bg="#9bb1d6",
                                  fg="white", font=('MS', 12, 'bold'))
        lblAnswerA.grid(row=8, column=0, sticky=E)
        lblExampleQuestion = Label(self, text='Banana', bg="#9bb1d6",
                                  fg="white",font=('MS', 12))
        lblExampleQuestion.grid(row=8, column=9, sticky=W)

        lblAnswerB = Label(self, text='Enter the Answer for the First Match:',bg="#9bb1d6",
                                  fg="white", font=('MS', 12, 'bold'))
        lblAnswerB.grid(row=9, column=0, sticky=E)
        lblExampleQuestion = Label(self, text='Yellow',bg="#9bb1d6",
                                  fg="white", font=('MS', 12))
        lblExampleQuestion.grid(row=9, column=9, sticky=W)

        lblAnswerC = Label(self, text='Enter the Second Match:', bg="#9bb1d6",
                                  fg="white",font=('MS', 12, 'bold'))
        lblAnswerC.grid(row=10, column=0, sticky=E)
        lblExampleQuestion = Label(self, text='Satsuma',bg="#9bb1d6",
                                  fg="white", font=('MS', 12))
        lblExampleQuestion.grid(row=10, column=9, sticky=W)

        lblAnswerD = Label(self, text='Enter the Answer for the Second Match:',bg="#9bb1d6",
                                  fg="white", font=('MS', 12, 'bold'))
        lblAnswerD.grid(row=11, column=0, sticky=E)
        lblExampleQuestion = Label(self, text='Orange',bg="#9bb1d6",
                                  fg="white", font=('MS', 12))
        lblExampleQuestion.grid(row=11, column=9, sticky=W)

        lblCorrectAnswer = Label(self, text='Enter the Third Match:',bg="#9bb1d6",
                                  fg="white", font=('MS', 12, 'bold'))
        lblCorrectAnswer.grid(row=15, column=0, sticky=E)
        lblExampleQuestion = Label(self, text='Cherry', bg="#9bb1d6",
                                  fg="white",font=('MS', 12))
        lblExampleQuestion.grid(row=15, column=9, sticky=W)

        lblCorrectAnswer = Label(self, text='Enter the Answer for the Third Match:',
                                 bg="#9bb1d6", fg="white", font=('MS', 12, 'bold'))
        lblCorrectAnswer.grid(row=16, column=0, sticky=E)
        lblExampleQuestion = Label(self, text='Red',bg="#9bb1d6",
                                  fg="white", font=('MS', 12))
        lblExampleQuestion.grid(row=16, column=9, sticky=W)

        lblSpace.grid(row=17, column=5)
        lblSpace.grid(row=18, column=6)

    # Sets up the user input boxes and buttons
    def enter_question(self):
        self.txtQuestion.grid(row=5, column=2, columnspan=5, sticky=W + E, padx = 10, pady = 10, ipady = 10)

        self.Match1.grid(row=8, column=2, columnspan=5, sticky=W + E, padx = 10, pady = 10, ipady = 10)

        self.Answer1.grid(row=9, column=2, columnspan=5, sticky=W + E, padx = 10, pady = 10, ipady = 10)

        self.Match2.grid(row=10, column=2, columnspan=5, sticky=W + E, padx = 10, pady = 10, ipady = 10)

        self.Answer2.grid(row=11, column=2, columnspan=5, sticky=W + E, padx = 10, pady = 10, ipady = 10)

        self.Match3.grid(row=15, column=2, columnspan=5, sticky=W + E, padx = 10, pady = 10, ipady = 10)

        self.Answer3.grid(row=16, column=2, columnspan=5, sticky=W + E, padx=10, pady=10, ipady=10)

        butSubmit = Button(self, text='Submit Question', font=('MS', 10, 'bold'),bg="white",
                           command=lambda: self.storeResponse(self.txtQuestion, self.Match1, self.Answer1,
                                                              self.Match2, self.Answer2, self.Match3, self.Answer3))
        butSubmit.grid(row=17, column=2)

        butClear = Button(self, text='Next Question', font=('MS', 10, 'bold'),bg="white", command=lambda: self.clearInput())
        butClear.grid(row=17, column=3)
        lblClickSubmit = Label(self,
                               text='Click "Next Question" to write a new question', bg="#9bb1d6",
                                  fg="white",font=('MS', 12))
        lblClickSubmit.grid(row=2, column=2, sticky=W)

        butStartQuiz = Button(self, text='Return to Main Menu',bg="white", font=('MS', 10, 'bold'), command=self.close_windows)
        butStartQuiz.grid(row=0, column=0)

    def close_windows(self):
        self.master.destroy()

    # Clears the form so the user can write another question
    def clearInput(self):
        self.txtQuestion.delete(0, END)
        self.Match1.delete(0, END)
        self.Answer1.delete(0, END)
        self.Match2.delete(0, END)
        self.Answer2.delete(0, END)
        self.Match3.delete(0, END)
        self.Answer3.delete(0, END)

    # Takes user input and writes to file
    # Sets up and user error warnings such as not providing all question answers etc.
    def storeResponse(self, new_question, new_match_1, new_answer_1, new_match_2, new_answer_2, new_match_3, new_answer_3):

        user_question = new_question.get()
        user_match_1 = new_match_1.get()
        user_answer_1 = new_answer_1.get()
        user_match_2 = new_match_2.get()
        user_answer_2 = new_answer_2.get()
        user_match_3 = new_match_3.get()
        user_answer_3 = new_answer_3.get()

        if user_match_1 == "" or user_answer_1 == "" or user_match_2 == "" or user_answer_2 == ""\
                or user_match_3 == "" or user_answer_3 == "":
            tkinter.messagebox.showinfo("ERROR", "You Need To Supply All Matches and Answers!")
        elif user_question == "":
            tkinter.messagebox.showinfo("ERROR", "You Need To Supply A Question!")

        else:
            file = open("questionsQuiz2.txt", "a")  # append to file

            file.write("\n")
            file.write(user_question)
            file.write("\n")
            file.write(user_match_1)
            file.write("\n")
            file.write(user_answer_1)
            file.write("\n")
            file.write(user_match_2)
            file.write("\n")
            file.write(user_answer_2)
            file.write("\n")
            file.write(user_match_3)
            file.write("\n")
            file.write(user_answer_3)
            file.close()
            tkinter.messagebox.showinfo("Success", "New Question has been saved to file")
            root1.lift()

root1 = tk.Tk()
root1.title("Write New Question")
root1.attributes("-zoomed", True)
app = NewQuestionQuiz2(root1)


