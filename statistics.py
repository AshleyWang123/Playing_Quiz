import tkinter as tk
import tkinter.messagebox
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from  matplotlib.figure import  Figure
import sys

#framework
class Basedesk:
    #GUI Setup

    def __init__(self,master):
        # Initialise Questionnaire class
        self.master=master
        self.initface = tk.Frame(self.master,)
        self.initface.pack(fill="both", expand=True)
        self.initface.configure(bg="#9bb1d6",)
        self.initface.pack()

        text = tk.Label(self.initface, text='Quiz Statistics Platform',bg="#9bb1d6", fg="white", font=('MS', 18, 'bold'))
        text.grid(row=1, column=2, padx=15,pady=15)
        text.place(x=950, y=200, anchor="center")

        text4 = tk.Label(self.initface, text='Welcome COMSC!', bg="#9bb1d6", fg="white", font=('MS', 16, 'bold'))
        text4.grid(row=2, column=1, padx=15, pady=15)
        text4.place(x=800, y=300, anchor="center")

        text1 = tk.Label(self.initface, text='Pupils Information:',bg="#9bb1d6", fg="white", font=('MS', 14, 'normal'))
        text1.grid(row=4, column=1, padx=15,pady=15)
        text1.place(x=800, y=400, anchor="center")
        btn1 = tk.Button(self.initface, text='View', bg="white", command=self.change1)
        btn1.grid(row=4,column=2,padx=15,pady=15)
        btn1.place(x=1100, y=400, anchor="center")

        text2 = tk.Label(self.initface, text='Qusetions:',bg="#9bb1d6",fg="white", font=('MS', 14, 'normal'))
        text2.grid(row=5, column=1, padx=15,pady=15)
        text2.place(x=800, y=500, anchor="center")
        btn2 = tk.Button(self.initface, text='View',bg="white", command=self.change2)
        btn2.grid(row=5,column=2,padx=15,pady=15)
        btn2.place(x=1100, y=500, anchor="center")

        text3 = tk.Label(self.initface, text='Question Counter:',bg="#9bb1d6", fg="white", font=('MS', 14, 'normal'))
        text3.grid(row=6, column=1, padx=15,pady=15)
        text3.place(x=800, y=600, anchor="center")
        btn3 = tk.Button(self.initface, text='View',bg="white", command=self.change3)
        btn3.grid(row=6,column=2,padx=15,pady=15)
        btn3.place(x=1100, y=600, anchor="center")

        btn4 = tk.Button(self.initface, text='Back',bg="white", command=self.back)
        btn4.grid(row=2,column=2,padx=15,pady=15)
        btn4.place(x=1200, y=300, anchor="center")

        self.re_resp()

    def change1(self, ):
        self.initface.destroy()
        Page1(self.master)

    def change2(self, ):
        self.initface.destroy()
        Page2(self.master)

    def change3(self, ):
        self.initface.destroy()
        Page3(self.master)

    def back(self,):
        self.initface.destroy()
        Page0(self.master)

#retrive the results
    def re_resp(self):
        dataset=pd.read_csv("dataset_results.csv")
        frame=pd.DataFrame(dataset)

        #the quantity of participants
        global countAll
        countAll=frame["school"].count()


        #the quantity of schools
        global countS1,countS2,countS3,countS4,countS5,countS6,countS7,countS8,countS9,countS10

        countS1 = list(frame.school).count("school1")
        countS2 = list(frame.school).count("school2")
        countS3 = list(frame.school).count("school3")
        countS4 = list(frame.school).count("school4")
        countS5 = list(frame.school).count("school5")
        countS6 = list(frame.school).count("school6")
        countS7 = list(frame.school).count("school7")

        #the quantity a question is answered correctly, wrongly or uncompleted
        global sumCq1, sumWq1, sumUq1
        global sumCq2, sumWq2, sumUq2
        global sumCq3, sumWq3, sumUq3
        global sumCq4, sumWq4, sumUq4
        global sumCq5, sumWq5, sumUq5
        global sumCq6, sumWq6, sumUq6
        global sumCq7, sumWq7, sumUq7
        global sumCq8, sumWq8, sumUq8
        global sumCq9, sumWq9, sumUq9
        global sumCq10, sumWq10, sumUq10


        sumCq1, sumWq1,sumUq1=list(frame.Quiz1Question1).count(1),list(frame.Quiz1Question1).count(0),list(frame.Quiz1Question1).count(-1)
        sumCq2, sumWq2,sumUq2=list(frame.Quiz1Question2).count(1),list(frame.Quiz1Question2).count(0),list(frame.Quiz1Question2).count(-1)
        sumCq3, sumWq3,sumUq3=list(frame.Quiz1Question3).count(1),list(frame.Quiz1Question3).count(0),list(frame.Quiz1Question3).count(-1)
        sumCq4, sumWq4,sumUq4=list(frame.Quiz1Question4).count(1),list(frame.Quiz1Question4).count(0),list(frame.Quiz1Question4).count(-1)
        sumCq5, sumWq5,sumUq5=list(frame.Quiz1Question5).count(1),list(frame.Quiz1Question5).count(0),list(frame.Quiz1Question5).count(-1)
        sumCq6, sumWq6,sumUq6=list(frame.Quiz2Question6).count(1),list(frame.Quiz2Question6).count(0),list(frame.Quiz2Question6).count(-1)
        sumCq7, sumWq7,sumUq7=list(frame.Quiz2Question7).count(1),list(frame.Quiz2Question7).count(0),list(frame.Quiz2Question7).count(-1)
        sumCq8, sumWq8,sumUq8=list(frame.Quiz2Question8).count(1),list(frame.Quiz2Question8).count(0),list(frame.Quiz2Question8).count(-1)
        sumCq9, sumWq9,sumUq9=list(frame.Quiz2Question9).count(1),list(frame.Quiz2Question9).count(0),list(frame.Quiz2Question9).count(-1)
        sumCq10,sumWq10,sumUq10=list(frame.Quiz2Question10).count(1),list(frame.Quiz2Question10).count(0),list(frame.Quiz2Question10).count(-1)

#loging
class Logging:
    #GUI Setup

    def __init__(self,master):
        # Initialise Questionnaire class

        global username, password
        self.master=master
        self.initface = tk.Frame(self.master,)
        self.initface.pack(fill="both", expand=True)
        self.initface.configure(bg="#9bb1d6",)
        self.initface.pack()

        text = tk.Label(self.initface, text='Administrator Platform',bg="#9bb1d6", fg="white", font=('MS', 24, 'bold'))
        text.grid(row=1, column=2, padx=15,pady=15)
        text.place(x=950,y=200,anchor="center")

        text1 = tk.Label(self.initface, text='User Name:', bg="#9bb1d6", fg="white", font=('MS', 14, 'normal'))
        text1.grid(row=3, column=1, padx=15, pady=15)
        text1.place(x=800,y=400,anchor="center")

        username = tk.Entry(self.initface,bd=2)
        username.grid(row=3, column=2, padx=15, pady=15)
        username.place(x=1000, y=400, anchor="center")

        text2 = tk.Label(self.initface, text='Password:', bg="#9bb1d6", fg="white", font=('MS', 14, 'normal'))
        text2.grid(row=4, column=1, padx=15, pady=15)
        text2.place(x=790, y=500, anchor="center")

        password = tk.Entry(self.initface, bd=2)
        password.grid(row=4, column=2, padx=15, pady=15)
        password.place(x=1000, y=500, anchor="center")

        btn1 = tk.Button(self.initface, text="Log in", bg="white", command=self.change1)
        btn1.grid(row=5, column=1, padx=15, pady=15)
        btn1.place(x=800, y=600, anchor="center")

        btn2 = tk.Button(self.initface, text="Quit", bg="white", command= self.quit)
        btn2.grid(row=5, column=2, padx=15, pady=15)
        btn2.place(x=1000, y=600, anchor="center")

        text3 = tk.Label(self.initface, text='Test Account:', bg="#9bb1d6", fg="white", font=('MS', 14, 'normal'))
        text3.grid(row=3, column=3, padx=15, pady=15)
        text3.place(x=800, y=300, anchor="center")

        text4 = tk.Label(self.initface, text='comsc:123456', bg="#9bb1d6", fg="white", font=('MS', 14, 'normal'))
        text4.grid(row=4, column=3, padx=15, pady=15)
        text4.place(x=1000, y=300, anchor="center")

    def change1(self, ):
        name=username.get()
        word=password.get()
        if(name=="comsc" and word=="123456"):
            self.initface.destroy()
            Page0(self.master)
        else:
            tk.messagebox.showwarning("Error","username or password is wrong!!!")
            self.master.lift()

    def quit(self,):
        try:
            root.destroy()
        except:
            self.master.destroy()

#main menu
class Page0:
    def __init__(self, master):
        self.master=master
        self.initface = tk.Frame(self.master,)
        self.initface.pack(fill="both", expand=True)
        self.initface.configure(bg="#9bb1d6",)
        self.initface.pack()
        self.index()

    def addQ1(self):
        import NewQuestionQuiz1
        del sys.modules["NewQuestionQuiz1"]

    def addQ2(self):
           import NewQuestionQuiz1
           del sys.modules["NewQuestionQuiz1"]

    def statistics(self):
        global top
        top = tk.Toplevel()
        top.title('Administrator')
        top.attributes("-zoomed", True)
        Basedesk(top)
        top.mainloop()

    def back(self,):
        self.initface.destroy()
        Logging(self.master)

    def index(self):
        text1 = tk.Label(self.initface, text='Welcome COMSC!', bg="#9bb1d6", fg="white", font=('MS', 24, 'normal'))
        text1.grid(row=0, column=1, padx=15, pady=15)
        text1.place(x=950, y=200, anchor="center")

        btn1 = tk.Button(self.initface, text='Add Question to Quiz 1', bg="white", command=self.addQ1)
        btn1.grid(row=1, column=1, padx=15, pady=15)
        btn1.place(x=950, y=300, anchor="center")

        btn2 = tk.Button(self.initface, text='Add Question to Quiz 2', bg="white", command=self.addQ2)
        btn2.grid(row=2, column=1, padx=15, pady=15)
        btn2.place(x=950, y=400, anchor="center")

        btn3 = tk.Button(self.initface, text='Statistics', bg="white", command=self.statistics)
        btn3.grid(row=3, column=1, padx=15, pady=15)
        btn3.place(x=950, y=500, anchor="center")

        btn4 = tk.Button(self.initface, text='Log out', bg="white", command=self.back)
        btn4.grid(row=4, column=1, padx=15, pady=15)
        btn4.place(x=950, y=600, anchor="center")

#puplies
class Page1:
    def __init__(self, master):
        self.master = master
        self.Page1 = tk.Frame(self.master, )
        self.Page1.pack()
        btn_back = tk.Button(self.Page1, text='Back', command=self.back)
        btn_back.pack()

        self.count_schools()

    def back(self):

        self.Page1.pack_forget()
        canvas.get_tk_widget().destroy()
        toolbar.destroy()
        Basedesk(self.master)

    def count_schools(self):
        global canvas, toolbar

        # simulation data
        x = ["School1", "School2", "School3", "School4", "School5", "School6", "School7"]
        y = [countS1, countS2, countS3, countS4, countS5, countS6, countS7]

        #sum of students
        sum = 0
        for i in y:
            sum=sum+i
        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        rects=a.bar(x, y,color=["#107dac", "#189ad3","#1ebbd7"])

        for rect in rects:
            height = rect.get_height()
            a.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
        a.set_title("Tatal Students: "+str(sum))
        a.set_ylabel("Quantity of Schools")
        a.set_ylim(0,120)


        canvas = FigureCanvasTkAgg(f, top)
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, top)
        toolbar.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.YES)

#questions
class Page2:
    def __init__(self, master):
        self.master = master
        self.Page1 = tk.Frame(self.master, )
        self.Page1.pack()
        btn_back = tk.Button(self.Page1, text='Back', command=self.back)
        btn_back.pack()

        self.count_questions()


    def back(self):

        self.Page1.pack_forget()
        canvas.get_tk_widget().destroy()
        toolbar.destroy()
        Basedesk(self.master)

    def count_questions(self):
        global canvas, toolbar

        # simulation data
        category = ['Correct', "Wrong", 'umcompleted']
        question = {
            'Question 1': [sumCq1, sumWq1,sumUq1],
            'Question 2': [sumCq2, sumWq2,sumUq2],
            'Question 3': [sumCq3, sumWq3,sumUq3],
            'Question 4': [sumCq4, sumWq4,sumUq4],
            'Question 5': [sumCq5, sumWq5,sumUq5],
            'Question 6': [sumCq6, sumWq6,sumUq6],
            'Question 7': [sumCq7, sumWq7,sumUq7],
            'Question 8': [sumCq8, sumWq8,sumUq8],
            'Question 9': [sumCq9, sumWq9,sumUq9],
            'Question10': [sumCq10, sumWq10,sumUq10]
        }

        labels = list(question.keys())
        data = np.array(list(question.values()))
        data_cum = data.cumsum(axis=1)
        category_colors = plt.get_cmap('GnBu_r')(
            np.linspace(0.15, 0.85, data.shape[1]))

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(212)

        for i, (colname, color) in enumerate(zip(category, category_colors)):
            widths = data[:, i]
            starts = data_cum[:, i] - widths
            a.barh(labels, widths, left=starts, height=0.5,
                    label=colname, color=color)
            xcenters = starts + widths / 2

            r, g, b, _ = color
            text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
            for y, (x, c) in enumerate(zip(xcenters, widths)):
                a.text(x, y, str(int(c)), ha='center', va='center',
                        color=text_color)
        a.legend(ncol=len(category), bbox_to_anchor=(0, 1),
                  loc='lower left', fontsize='small')

        a = f.add_subplot(211)
        data = list(question.values())
        for i in range(10):
            for j in range(3):
                data[i][j] = round(data[i][j] /countAll * 100, 2)
                data[i][j] = str(data[i][j]) + "%"
        columns = list(question.keys())
        colors = plt.cm.BuPu(np.linspace(0, 0.5, len(columns)))

        # Reverse colors and text labels to display the last value at the top.
        colors = colors[::-1]

        # Add a table at the bottom of the axes
        a.table(cellText=data,
                  rowLabels=columns,
                  rowColours=colors,
                  colLabels=["Correct", "Wrong", "Uncompleted"],
                  loc="center")
        a.get_xaxis().set_visible(False)
        a.get_yaxis().set_visible(False)

        canvas = FigureCanvasTkAgg(f, top)
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, top)
        toolbar.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.YES)

#counter
class Page3:
    def __init__(self, master):
        self.master = master
        self.Page2 = tk.Frame(self.master, )
        self.Page2.pack()
        btn_back = tk.Button(self.Page2, text='Back', command=self.back)
        btn_back.pack()

        self.Time()


    def back(self):

        self.Page2.pack_forget()
        canvas.get_tk_widget().destroy()
        toolbar.destroy()
        Basedesk(self.master)

    def Time(self):
        global canvas, toolbar

        # simulation data
        X = ["Question1", "Question2", "Question3", "Question4", "Question5", "Question6", "Question7", "Question8",
             "Question9", "Question10"]
        Y1 = [sumCq1+sumWq1, sumCq2+sumWq2, sumCq3+sumWq3, sumCq4+sumWq4, sumCq5+sumWq5,
              sumCq6+sumWq6, sumCq7+sumWq7, sumCq8+sumWq8,sumCq9+sumWq9, sumCq10+sumWq10]
        Y2 = [sumUq1, sumUq2, sumUq3, sumUq4, sumUq5, sumUq6, sumUq7, sumUq8, sumUq9, sumUq10]

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)

        for x, y1, y2 in zip(X, Y1, Y2):
            a.bar(x, +y1, facecolor='#189ad3', edgecolor='white')
            a.bar(x, -y2, facecolor='#ea989d', edgecolor='white')

        for x, y in zip(X, Y1):
            a.text(x, y, y, ha='center', va='bottom')

        for x, y in zip(X, Y2):
            a.text(x, -y, y, ha='center', va='top')

        a.get_yaxis().set_visible(False)
        a.set_title("Question Counter \n" "Total: {}".format(countAll))
        a.legend(["Answer Counter","Given up Counter"],bbox_to_anchor=(0, 1),
                  loc='upper left', fontsize='small')
        canvas = FigureCanvasTkAgg(f, top)
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, top)
        toolbar.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.YES)


#Main
root = tk.Tk()
root.title("Quiz Statistic")
root.attributes("-zoomed", True)
app = Logging(root)
