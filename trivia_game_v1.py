from tkinter import *
from tkinter import ttk
import tkinter.font as font

win = Tk()

frm = ttk.Frame(win, padding=9, width=500, height=500)
frm.pack()
fontsize = font.Font(size=20)


def switchframe():
    frm.pack_forget()
    q1.pack(fill=BOTH, expand=True)
    next.destroy()


q1 = ttk.Frame(win, padding=10, width=500, height=500)
ttk.Label(frm, text="welcome to trivia night").grid(column=1, row=0)
next = ttk.Button(win, text="next", command=switchframe)
next.pack()

ttk.Label(
    q1, text="How old was Queen Elizabeth II when she was crowned Queen of England?"
).pack(side=TOP)
ttk.Label(q1, text="this question is worth 5 points").pack(side=TOP)

answer1 = StringVar(q1, "27")
Radiobutton(q1, text="27", variable=answer1, value="27").pack(side=LEFT)
Radiobutton(q1, text="25", variable=answer1, value="25").pack(side=LEFT)
Radiobutton(q1, text="22", variable=answer1, value="22").pack(side=LEFT)
Radiobutton(q1, text="28", variable=answer1, value="28").pack(side=LEFT)

q2 = ttk.Frame(win, padding=10, width=500, height=500)


def switchframe1():
    q1.pack_forget()
    q2.pack(fill=BOTH, expand=True)
    next.destroy()


next1 = ttk.Button(q1, text="next", command=switchframe1)
next1.pack(side=BOTTOM)
ttk.Label(q2, text="What is the name of Thomas Jefferson's main house?").pack(side=TOP)
ttk.Label(q2, text="This question is worth 3 points ").pack(side=TOP)

answer2 = StringVar(q2, "monticello")
Radiobutton(q2, text="monticello", variable=answer2, value="monticello").pack(side=LEFT)
Radiobutton(q2, text="cedar", variable=answer2, value="cedar").pack(side=LEFT)
Radiobutton(q2, text="vernon", variable=answer2, value="vernon").pack(side=LEFT)
Radiobutton(q2, text="greentown", variable=answer2, value="greentown").pack(side=LEFT)

q3 = ttk.Frame(win, padding=10, width=500, height=500)


def switchframe2():
    q2.pack_forget()
    q3.pack(fill=BOTH, expand=True)
    next2.destroy()


next2 = ttk.Button(q2, text="next", command=switchframe2)
next2.pack(side=BOTTOM)
ttk.Label(q3, text="What year was the wreck of the Titanic discovered?").pack(side=TOP)

answer3 = StringVar(q3, "1985")
Radiobutton(q3, text="1981", variable=answer2, value="1981").pack(side=LEFT)
Radiobutton(q3, text="1978", variable=answer2, value="1978").pack(side=LEFT)
Radiobutton(q3, text="1985", variable=answer2, value="1985").pack(side=LEFT)
Radiobutton(q3, text="1992", variable=answer2, value="1992").pack(side=LEFT)

points = 0

def answer_count():
    global points
    if answer1.get() == "25":
        points += 5
        ttk.Label(
            q2, text="Your previous answer was Correct! Your score is " + str(points)
        ).pack(side=TOP)
    else:
        ttk.Label(
            q2, text="Your previous answer was Incorrect! Your score is " + str(points)
        ).pack(side=TOP)


answer_count()

win.mainloop()
