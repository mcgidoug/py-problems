from tkinter import *
from tkinter import ttk
import tkinter.font as font

win = Tk()

frm = ttk.Frame(win, padding=9, width=500, height=500)
frm.pack()
fontsize = font.Font(size=20)

q1 = ttk.Frame(win, padding=10, width=500, height=500)
q2 = ttk.Frame(win, padding=10, width=500, height=500)
q3 = ttk.Frame(win, padding=10, width=500, height=500)

answer1 = StringVar(q1, "27")
answer2 = StringVar(q2, "monticello")
answer3 = StringVar(q3, "1985")

points = 0

def switchframe():
    frm.pack_forget()
    q1.pack(fill=BOTH, expand=True)
    next.destroy()

next = ttk.Button(win, text="next", command=switchframe)
next.pack()

def answer_evaluation(answer, current_frame):
    global points
    if answer.get() == "25":
        points += 5
        ttk.Label(
            current_frame, text="Your previous answer was Correct! Your score is " + str(points)
        ).pack(side=TOP)
    else:
        ttk.Label(
            current_frame, text="Your previous answer was Incorrect! Your score is " + str(points)
        ).pack(side=TOP)

def switchframe1():
    q1.pack_forget()
    answer_evaluation(answer1, q2)
    q2.pack(fill=BOTH, expand=True)
    next.destroy()

next1 = ttk.Button(q1, text="next", command=switchframe1)
next1.pack(side=BOTTOM)

def switchframe2():
    q2.pack_forget()
    answer_evaluation(answer2, q3)
    q3.pack(fill=BOTH, expand=True)
    next2.destroy()

next2 = ttk.Button(q2, text="next", command=switchframe2)
next2.pack(side=BOTTOM)

ttk.Label(frm, text="welcome to trivia night").grid(column=1, row=0)

# q1 elements
ttk.Label(
    q1, text="How old was Queen Elizabeth II when she was crowned Queen of England?"
).pack(side=TOP)
Radiobutton(q1, text="27", variable=answer1, value="27").pack(side=LEFT)
Radiobutton(q1, text="25", variable=answer1, value="25").pack(side=LEFT)
Radiobutton(q1, text="22", variable=answer1, value="22").pack(side=LEFT)
Radiobutton(q1, text="28", variable=answer1, value="28").pack(side=LEFT)

# q2 elements
ttk.Label(q2, text="What is the name of Thomas Jefferson's main house?").pack(side=TOP)
Radiobutton(q2, text="monticello", variable=answer2, value="monticello").pack(side=LEFT)
Radiobutton(q2, text="cedar", variable=answer2, value="cedar").pack(side=LEFT)
Radiobutton(q2, text="vernon", variable=answer2, value="vernon").pack(side=LEFT)
Radiobutton(q2, text="greentown", variable=answer2, value="greentown").pack(side=LEFT)

# q3 elements
ttk.Label(q3, text="What year was the wreck of the Titanic discovered?").pack(side=TOP)
Radiobutton(q3, text="1981", variable=answer3, value="1981").pack(side=LEFT)
Radiobutton(q3, text="1978", variable=answer3, value="1978").pack(side=LEFT)
Radiobutton(q3, text="1985", variable=answer3, value="1985").pack(side=LEFT)
Radiobutton(q3, text="1992", variable=answer3, value="1992").pack(side=LEFT)

win.mainloop()
