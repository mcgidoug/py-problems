from tkinter import *
from tkinter import ttk

class QuestionForm:
    def __init__(self, root, question, options, answer):
        self.root = root
        self.question = question
        self.options = options
        self.answer = answer
        self.selected_answer = None
        self.points = 0

        self.var = StringVar()

        self.question_label = ttk.Label(self.root, text=self.question, wraplength=300, justify="center")
        self.question_label.pack(pady=10)

        self.radio_buttons = []
        for i, option in enumerate(self.options):
            radio = ttk.Radiobutton(self.root, text=option, variable=self.var, value=option)
            radio.pack()
            self.radio_buttons.append(radio)

        self.submit_button = ttk.Button(self.root, text="Submit", command=self.submit_answer)
        self.submit_button.pack(pady=10)

    def submit_answer(self):
        self.selected_answer = self.var.get()
        if self.selected_answer == self.answer:
            self.points += 1
        self.clear_form()

    def clear_form(self):
        self.question_label.pack_forget()
        for radio in self.radio_buttons:
            radio.pack_forget()
        self.submit_button.pack_forget()
        if self.points == 3:
            self.show_result()
        else:
            self.points += 1
            self.question_label.config(text=f"You scored {self.points} out of 3. Next question:")
            self.question_label.pack()
            self.var.set("")
            for radio in self.radio_buttons:
                radio.pack()
            self.submit_button.pack()

    def show_result(self):
        result_label = ttk.Label(self.root, text=f"You scored {self.points} out of 3")
        result_label.pack()

# Sample Questions
questions = [
    {
        "question": "How old was Queen Elizabeth II when she was crowned Queen of England?",
        "options": ["27", "25", "22", "28"],
        "answer": "27"
    },
    {
        "question": "What is the name of Thomas Jefferson's main house?",
        "options": ["Monticello", "Cedar", "Vernon", "Greentown"],
        "answer": "Monticello"
    },
    {
        "question": "What year was the wreck of the Titanic discovered?",
        "options": ["1981", "1978", "1985", "1992"],
        "answer": "1985"
    }
]

# Initialize Tkinter
root = Tk()
root.title("Questionnaire")

# Create instances of QuestionForm for each question
question_forms = []
for q in questions:
    form = QuestionForm(root, q["question"], q["options"], q["answer"])
    question_forms.append(form)

root.mainloop()
