from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import  pandas as pd
import  sys
import random
# from QuizQuestion import *


# function to get the data from txt file for the quiz
def get_quiz_data(filename, quiz_data):
	quiz_data = []              #list to store file data
	file = open(filename, "r")
	line = file.readline()

	while line != "":
		quiz_question = line
		answers_from_file = []
		for i in range(4):
			answers_from_file.append(file.readline())

		correct_answer_from_file = file.read(1)
		file.readline()
		quiz_data.append((quiz_question, answers_from_file, correct_answer_from_file))
		line = file.readline()
	return (quiz_data)

def get_quiz_data2(filename, quiz_data):
	quiz_data = []
	file = open(filename, "r")
	line = file.readline()
	while line != "":
		quiz_question = line
		match_a = []
		match_b = []
		for i in range(3):
			match_a.append(file.readline().rstrip('\n'))
			match_b.append(file.readline().rstrip('\n'))
		quiz_data.append((quiz_question, match_a, match_b))
		line = file.readline()
	return (quiz_data)


#function to set status bar and reset button for quiz screens
def reset_pop(top):
	global round_quiz_1
	global round_quiz_2
	global right_ans_quiz1
	global right_ans_quiz2
	confirm = messagebox.askyesno("Reset", "Are you sure you want to Reset ?")
	if confirm == 1:
		round_quiz_1 = 0
		round_quiz_2 = 0
		right_ans_quiz1=[]
		right_ans_quiz2=[]
		messagebox.showinfo("Information", "To play these quizzes agian, click on 'Re-Activate Quiz' ")
		top1.destroy()
		top2.destroy()


def set_status_reset(top, quiz_no, round, quiz_data):
		status = Label(top, text="Welcome To Quiz "+quiz_no+"   |   Progress bar: "+str(round+1) +
								 " out of "+str( len(quiz_data) )+"  |", bd=2, relief=SUNKEN,
					   			bg="#9bb1d6", fg="white",font = ("MS", 20, "bold"), pady=10, width=50)
		status.grid(row=0, column=0,columnspan=5,pady=50)
		reset_btn = Button(top, text="Reset",bg="white",font = ("MS", 20), bd=2, relief=SUNKEN, width=7,command=lambda:reset_pop(top))
		reset_btn.grid(row=0,column=5)


# return a list with right and wrong ans
def right_wrong_ans_count(alist):
	r_count=0
	w_count=0
	for i in alist:
		if i ==1:
			r_count +=1
		else:
			w_count+=1
	count=[r_count, w_count]
	return(count)

round_quiz_1 = 0 # rounds for quiz 2
round_quiz_2 = 0 # rounds for quiz 2

quiz_1_data=[]
quiz_1_data = get_quiz_data("questionsQuiz1.txt", quiz_1_data)
quiz_2_data=[]
quiz_2_data = get_quiz_data2("questionsQuiz2.txt", quiz_2_data)

right_ans_quiz1=[]  #list of right and wrong ans for quiz1
right_ans_quiz2=[]  #list of right and wrong ans for quiz2

#Quiz 1 window
def quiz_1():
	messagebox.showinfo( "Quiz 1", "INSTRUCTIONS: Click On Any 1 Option Out Of 4 To Submit The Answer")
	global top1
	top1 = Toplevel()
	top1.title('Home/Quiz1')
	top1.configure(bg="#9bb1d6")
	top1.attributes("-zoomed", True)

	q1 = StringVar()
	q1.set("A")
	quizBtn['state']=DISABLED


	def que_ans_display(data):
		global display
		display = LabelFrame(top1)
		display.configure(bg="#9bb1d6")
		display.grid(row=0, column=0)
		display.place(x=250,y=220)

		set_status_reset(display, "1", round_quiz_1, ([1,2]) )
		quiz1_que = Label(display, text=data[0], bg="#9bb1d6", fg="white",font= ("MS", 15, "bold"))
		quiz1_que.grid(row=1,column=0, pady=30)

		#Options
		option=data[1]
		quiz1_options1 = Radiobutton(display, text=option[0], variable = q1, fg="white", bg="#9bb1d6",selectcolor="#9bb1d6",value="A", font= ("MS", 15)).grid(row=2, column=0, sticky=W)
		quiz1_options2 = Radiobutton(display, text=option[1], variable = q1, fg="white", bg="#9bb1d6",selectcolor="#9bb1d6", value="B", font= ("MS", 15)).grid(row=2, column=1, sticky=W)
		quiz1_options3 = Radiobutton(display, text=option[2], variable = q1, fg="white", bg="#9bb1d6",selectcolor="#9bb1d6",value="C", font= ("MS", 15)).grid(row=3, column=0, sticky=W)
		quiz1_options4 = Radiobutton(display, text=option[3], variable = q1, fg="white", bg="#9bb1d6",selectcolor="#9bb1d6",value="D", font= ("MS", 15)).grid(row=3, column=1, sticky=W)

		#submitButton
		submitBtn1 = Button(display, text='Submit', bg="white",command = feedback, width=15)
		submitBtn1.grid(row = 4, column=2)


	# feedback after submitting the answer
	def feedback():
		global round_quiz_1
		global right_ans_quiz1

		if q1.get() == quiz_1_data[round_quiz_1][2]:
			messagebox.showinfo("FeedBack", "Right Answer!, The answer was option \""+quiz_1_data[round_quiz_1][2]+"\" \nFor next question click \"ok\"")
			right_ans_quiz1.append(1)
		else:
			messagebox.showerror("FeedBack", "Wrong Answer!, The answer was option \""+quiz_1_data[round_quiz_2][2]+"\" \nFor next question click \"ok\"")
			right_ans_quiz1.append(0)

		round_quiz_1 +=1
		if round_quiz_1<len(quiz_1_data):
			display.destroy()
			que_ans_display(quiz_1_data[round_quiz_1])
			set_status_reset(display, "1", round_quiz_1, quiz_1_data)
		elif round_quiz_1 == len(quiz_1_data):
			top1.destroy()
			count=right_wrong_ans_count(right_ans_quiz1)
			score_screen("Quiz 1", len(quiz_1_data), count[0])


	if len(quiz_1_data)>0:
		que_ans_display(quiz_1_data[round_quiz_1])
	else:
		quiz1_que = Label(top1, text="Please add some questions to start the quiz ... ...", bg="#9bb1d6", fg="white",font= ("MS", 15, "bold"))
		quiz1_que.grid(row=1,column=0, pady=30)



#Quiz 2 window
def quiz_2():
	messagebox.showinfo("Quiz 2", "INSTRUCTIONS: Click On An Option & Then Click On Its Match")
	global top2
	top2 = Toplevel()
	top2.title('Home/Quiz2')
	top2.configure(bg="#9bb1d6")
	top2.attributes("-zoomed", True)

	quizBtn2['state']=DISABLED


	#display for questions and options
	def que_ans_display(data):
		global display2
		global selected_answer1
		global selected_answer2
		global selected_answer3
		global ans
		global clicker
		clicker = 0
		display2 = LabelFrame(top2)
		display2.grid(row=0, column=0)
		display2.configure(bg="#9bb1d6")
		display2.place(x=250, y=220)

		set_status_reset(display2, "2", round_quiz_2, quiz_2_data)

		quiz2_que = Label(display2, text=data[0], bg="#9bb1d6", fg="white",font= ("MS", 15, "bold"))
		quiz2_que.grid(row=1,column=0, pady=30)

		option=data[1]
		match=data[2]
		#Options
		quiz2_options1 = Button(display2, text=option[0], fg="white", bg="#9bb1d6",font= ("MS", 15), command=lambda:[click1(option[0]), clicked(quiz2_options1)],width=25)
		quiz2_options2 = Button(display2, text=match[0], fg="white", bg="#7f90ad",font= ("MS", 15), command=lambda:[clickA(match[0]), clicked(quiz2_options2)],width=25)
		quiz2_options3 = Button(display2, text=option[1], fg="white", bg="#9bb1d6",font= ("MS", 15), command=lambda:[click2(option[1]), clicked(quiz2_options3)],width=25)
		quiz2_options4 = Button(display2, text=match[1], fg="white", bg="#7f90ad",font= ("MS", 15), command=lambda:[clickB(match[1]), clicked(quiz2_options4)],width=25)
		quiz2_options5 = Button(display2, text=option[2], fg="white", bg="#9bb1d6",font= ("MS", 15), command=lambda:[click3(option[2]), clicked(quiz2_options5)],width=25)
		quiz2_options6 = Button(display2, text=match[2], fg="white", bg="#7f90ad",font= ("MS", 15), command=lambda:[clickC(match[2]), clicked(quiz2_options6)],width=25)

		submit = Button(display2, text="Submit", command=feedback)
		a, b, c = random.sample(range(2,5), 3)

		quiz2_options1.grid(row=2, column=0, sticky=W)
		quiz2_options2.grid(row=a, column=2, sticky=E)
		quiz2_options3.grid(row=3, column=0, sticky=W)
		quiz2_options4.grid(row=b, column=2, sticky=E)
		quiz2_options5.grid(row=4, column=0, sticky=W)
		quiz2_options6.grid(row=c, column=2, sticky=E)
		submit.grid(row=5, column=0)

		def clicked(name):
			global clicker
			clicker += 1
			if clicker < 3:
				name.config(bg='#fcd4a7', relief=SUNKEN)
			elif clicker < 5:
				name.config(bg='#a7fcd4', relief=SUNKEN)
			else:
				name.config(bg='#fca7b3', relief=SUNKEN)

		selected_answer1 = []
		selected_answer2 = []
		selected_answer3 = []

		ans = {option[0]: match[0], option[1]: match[1], option[2]: match[2]}

	def click1(item):
		global selected_answer1
		if len(selected_answer1) == 0:
			selected_answer1.append(item)

	def click2(item):
		global selected_answer2
		if len(selected_answer2) == 0:
			selected_answer2.append(item)

	def click3(item):
		global selected_answer3
		if len(selected_answer3) == 0:
			selected_answer3.append(item)

	def clickA(item):
		if len(selected_answer1) == 1:
			selected_answer1.append(item)
		elif len(selected_answer2) == 1:
			selected_answer2.append(item)
		elif len(selected_answer3) == 1:
			selected_answer3.append(item)

	def clickB(item):
		if len(selected_answer1) == 1:
			selected_answer1.append(item)
		elif len(selected_answer2) == 1:
			selected_answer2.append(item)
		elif len(selected_answer3) == 1:
			selected_answer3.append(item)

	def clickC(item):
		if len(selected_answer1) == 1:
			selected_answer1.append(item)
		elif len(selected_answer2) == 1:
			selected_answer2.append(item)
		elif len(selected_answer3) == 1:
			selected_answer3.append(item)


	def feedback():
		global round_quiz_2
		global right_ans_quiz2
		global ans

		word = list(ans.items())[0][1]
		match = list(ans.items())[0][0]
		word2 = list(ans.items())[1][1]
		match2 = list(ans.items())[1][0]
		word3 = list(ans.items())[2][1]
		match3 = list(ans.items())[2][0]

		print(len(quiz_2_data))
		if selected_answer1[1] == word and selected_answer2[1] == word2:
			messagebox.showinfo("FeedBack", "Right Answer! \nThe correct matches are: \n" +str(selected_answer1[0])+" & "+str(selected_answer1[1])+"\n"+str(selected_answer2[0])+" & "+str(selected_answer2[1])+"\n"+str(selected_answer3[0])+" & "+str(selected_answer3[1])+"\nFor next question click \"ok\"")
			right_ans_quiz2.append(1)
		else:
			messagebox.showerror("FeedBack", "Wrong Answer!, \nThe correct matches are: \n" +match+" & "+word+"\n"+match2+" & "+word2+"\n"+match3+" & "+word3+"\nFor next question click \"ok\"")
			right_ans_quiz2.append(0)

		round_quiz_2 +=1
		if round_quiz_2<(len(quiz_2_data)-1):
			display2.destroy()
			que_ans_display(quiz_2_data[round_quiz_2])
			set_status_reset(display2, "2", round_quiz_2, quiz_2_data)
		elif round_quiz_2 == len(quiz_2_data)-1:
			top2.destroy()
			count=right_wrong_ans_count(right_ans_quiz2)
			score_screen("Quiz 2", len(quiz_2_data), count[0])



	if len(quiz_2_data)>0:
		que_ans_display(quiz_2_data[round_quiz_2])
	else:
		quiz2_que = Label(top2, text="Please add some questions to start the quiz ... ...", bg="#9bb1d6", fg="white",
						  font= ("MS", 15, "bold"))
		quiz2_que.grid(row=1,column=0, pady=30)

def score_screen(msg, total_que, r_ans):
	schoolName = schoolS.get()
	top3 = Toplevel()
	top3.title('Home/FeedBack or Statistic')
	top3.configure(bg="#9bb1d6")
	top3.attributes("-zoomed", True)

	#store in the csv
	if right_ans_quiz1==[]:
		data = {"school": [schoolName], "Quiz1Question1": None,
				"Quiz1Question2": None, "Quiz1Question3": None,
				"Quiz1Question4": None, "Quiz1Question5": None,
				"Quiz2Question6": [right_ans_quiz2[0]], "Quiz2Question7": [right_ans_quiz2[1]],
				"Quiz2Question8": [right_ans_quiz2[2]], "Quiz2Question9": [right_ans_quiz2[3]],
				"Quiz2Question10": [right_ans_quiz2[4]]}

	elif right_ans_quiz2==[]:
		data = {"school": [schoolName], "Quiz1Question1": [right_ans_quiz1[0]],
				"Quiz1Question2": [right_ans_quiz1[1]], "Quiz1Question3": [right_ans_quiz1[2]],
				"Quiz1Question4": [right_ans_quiz1[3]], "Quiz1Question5": [right_ans_quiz1[4]],
				"Quiz2Question6": None, "Quiz2Question7": None,
				"Quiz2Question8": None, "Quiz2Question9": None,
				"Quiz2Question10": None}

	else:
		data = {"school":[schoolName], "Quiz1Question1":[right_ans_quiz1[0]],
			  "Quiz1Question2":[right_ans_quiz1[1]], "Quiz1Question3":[right_ans_quiz1[2]],
			  "Quiz1Question4":[right_ans_quiz1[3]], "Quiz1Question5":[right_ans_quiz1[4]],
			  "Quiz2Question6":[right_ans_quiz2[0]], "Quiz2Question7":[right_ans_quiz2[1]],
			  "Quiz2Question8":[right_ans_quiz2[2]], "Quiz2Question9":[right_ans_quiz2[3]],
			  "Quiz2Question10":[right_ans_quiz2[4]]}

	dataframe=pd.DataFrame(data)
	dataframe.to_csv("dataset_results.csv",mode="a",header=False,index=False)

	# finish = Label(top3, text="Thanks for playing "+ msg +". Your Score is "+str(r_ans)+" out of "+str(total_que)+". Press 'Continue' button to play another quiz ").pack()
	# edit by WYATT
	if r_ans == 5:
		lblEnd = Label(top3, text='WELL DONE!!!!! You are a real master!',bg="#9bb1d6",
					fg="white",font=('MS',25,'bold'))

	if r_ans >= 1 and r_ans <= 4:
		lblEnd = Label(top3, text='Congradulations! You just finished the quiz!',bg="#9bb1d6", fg="white",font=('MS',25,'bold'))

	if r_ans == 0 :
		lblEnd = Label(top3, text='OH NOOOO! You need to work on this later on!',bg="#9bb1d6",
					fg="white",font=('MS',25,'bold'))

	lblEnd.grid(row=0, column=0, columnspan =10)
	lblEnd.place(x=950, y=200, anchor="center")


	lblEnd1 = Label(top3, text='Your final score is '+ str(r_ans)+ ' out of '+str(total_que-1) ,bg="#9bb1d6",
					fg="white",font=('MS',25),padx=250,pady=70)
	lblEnd1.grid()
	lblEnd1.place(x=950, y=400, anchor="center")

	b = Button(top3, text="Click here to see details",bg="white", command = lambda:final_fb(),width = 30)
	b.grid()
	b.place(x=950, y=500, anchor="center")
	cont_btn= Button(top3, text="Continue", bg="white",command=top3.destroy).place(x=950, y=600, anchor="center")

def final_fb(): #etail feedback page by WYATT
	global user_answer
	top = Toplevel()
	top.title('Detail Score')
	# top.geometry("500x500")

	lblStrAgr = Label(top, text = 'Correct \n Answer',font=('MS', 10,'bold'))
	lblStrAgr.grid(row=0, column= 8, rowspan=2)
	lblStrAgr1 = Label(top, text = 'Your \n Answer', font=('MS', 10,'bold'))
	lblStrAgr1.grid(row=0, column= 9, rowspan=2)

	final0 = Label(top, text='Quiz:',font=('MS', 10,'bold'))
	final0.grid(row=0, column= 0, rowspan=2)
	final1 = Label(top, text='1. '+str(quiz_2_data[0][0])+str(quiz_2_data[0][1]),font=('MS',10))
	final1.grid(row=2, column=0, columnspan=6, sticky=W)
	final2 = Label(top, text='2. '+str(quiz_2_data[1][0])+str(quiz_2_data[1][1]),font=('MS',10))
	final2.grid(row=4, column=0, columnspan=6, sticky=W)
	final3 = Label(top, text='3. '+str(quiz_2_data[2][0])+str(quiz_2_data[2][1]),font=('MS',10))
	final3.grid(row=6, column=0, columnspan=6, sticky=W)
	final3 = Label(top, text='4. '+str(quiz_2_data[3][0])+str(quiz_2_data[3][1]),font=('MS',10))
	final3.grid(row=8, column=0, columnspan=6, sticky=W)
	final4 = Label(top, text='5. '+str(quiz_2_data[4][0])+str(quiz_2_data[4][1]),font=('MS',10))
	final4.grid(row=10, column=0, columnspan=6, sticky=W)

	# curract answer
	c_answer0 = Label(top, text = str(quiz_2_data[0][2]),font=('MS',10))
	c_answer0.grid(row = 2, column = 8, rowspan=2)
	c_answer1 = Label(top, text = str(quiz_2_data[1][2]),font=('MS',10))
	c_answer1.grid(row = 4, column = 8, rowspan=2)
	c_answer2 = Label(top, text = str(quiz_2_data[2][2]),font=('MS',10))
	c_answer2.grid(row = 6, column = 8, rowspan=2)
	c_answer3 = Label(top, text = str(quiz_2_data[3][2]),font=('MS',10))
	c_answer3.grid(row = 8, column = 8, rowspan=2)
	c_answer4 = Label(top, text = str(quiz_2_data[4][2]),font=('MS',10))
	c_answer4.grid(row = 10, column = 8, rowspan=2)

	# user's answer
	u_answer0 = Label(top, text = str(user_answer[0]),font=('MS',10))
	u_answer0.grid(row = 2, column = 9, rowspan=2)
	u_answer1 = Label(top, text = str(user_answer[1]),font=('MS',10))
	u_answer1.grid(row = 4, column = 9, rowspan=2)
	u_answer2 = Label(top, text = str(user_answer[2]),font=('MS',10))
	u_answer2.grid(row = 6, column = 9, rowspan=2)
	u_answer3 = Label(top, text = str(user_answer[3]),font=('MS',10))
	u_answer3.grid(row = 8, column = 9, rowspan=2)
	u_answer4 = Label(top, text = str(user_answer[4]),font=('MS',10))
	u_answer4.grid(row = 10, column = 9, rowspan=2)


#main
root=Tk()
root.title('Home')
root.attributes("-zoomed",True)
root.configure(bg="#9bb1d6",)

#page layout
Label(root, text=" ",bg="#9bb1d6").grid(row=0,column=20,columnspan=20)
Label(root, text=" ",width=68,bg="#9bb1d6").grid(row=1,column=2)

#Heading
labelHead = Label(root, text="Quiz Time", fg="white", bg="#9bb1d6",font=("MS", 20, "bold"))
labelHead.grid(row=1, column=18, pady=50,)

#Subheading
labelSubHead = Label(root, text="Let's play- It's quiz time!", fg="white", bg="#9bb1d6",font=("MS", 15, "bold"))
labelSubHead.grid(row=2, column=18, pady=20,sticky=E)

#UserName & Greetings
nameLbl = Label(root, text="Name:", fg="white", bg="#9bb1d6",font=(15))
nameLbl.grid(row=3, column=17, columnspan=2, pady=20, sticky=W)
nameE = Entry(root,width=25,borderwidth=5)
nameE.grid(row=3, column=18,sticky=E)
nameE.insert(0,"Optional")

#schools
schoolLbl = Label(root, text="School:", fg="white", bg="#9bb1d6",font=(15))
schoolLbl.grid(row=4, column=17, columnspan=2, pady=20, sticky=W)
schoolS = ttk.Combobox(root,values=["school1","school2","school3","school4","school5","school6",
									"school7"],font=(15))
schoolS.set("school1")
schoolS.grid(row=4, column=18,sticky=E)

def name_func():
	global inst_lbl
	if nameE.get()!="Optional":
		msg = "Hello " + nameE.get() + ","
	else:
		msg="Hello, "
	inst_lbl = Label(root, text = msg + " Please select one of the options:", fg="white", bg="#9bb1d6",font=("MS", 10, "bold"))
	inst_lbl.grid(row=5, column=18, columnspan=4, pady=10, sticky=W)


nameBtn = Button(root,text="Submit", bg="white",command = name_func).grid(row=4, column=19)



#Quiz buttons
inst_lbl = Label(root, text=" Please select one of the options:",fg="white", bg="#9bb1d6",font=("MS", 10, "bold"))
inst_lbl.grid(row=5, column=18, columnspan=4, pady=10, sticky=W)

quizBtn = Button(root, text="Start Quiz 1",bg="white", width=15, command=quiz_1)
quizBtn2 = Button(root, text="Start Quiz 2", bg="white",width=15, command=quiz_2)

quizBtn.grid(row=6, column=18, pady=10, sticky=W,)
quizBtn2.grid(row=6, column=19, sticky=E, pady=10)

def openStats():
	import statistics
	del sys.modules["statistics"]


#Statistic buttons
stats = Button(root, text="Administror",bg="white", width=20, command=openStats)
stats.grid(row=7, column=19, sticky=E, pady=10)

#Refresh buttons and function(allow us to play quizzes multiple time without closing app)
def activate_quiz():
	global round_quiz_1
	global round_quiz_2
	global right_ans_quiz1
	global right_ans_quiz2
	messagebox.showwarning("Warning", "Make sure both the quiz windows are closed")
	confirm = messagebox.askyesno("Reset", "Are you sure you want to Re-Activate?")
	if confirm == 1:
		round_quiz_1 = 0
		round_quiz_2 = 0
		right_ans_quiz1=[]
		right_ans_quiz2=[]
		quizBtn['state']=NORMAL
		quizBtn2['state']=NORMAL


Activate_Quiz= Button(root, text="Re-Activate Quiz", bg="white",width=20, command=activate_quiz)
Activate_Quiz.grid(row=7, column=18, sticky=W, pady=10)

root.mainloop()
