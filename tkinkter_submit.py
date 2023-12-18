import tkinter as tk

def submit():
    value = entry.get()
    print(f"Submitted: {value}")
    # You can perform any action with the submitted value here

root = tk.Tk()
root.title("Input and Submit")

# Entry Field
entry = tk.Entry(root, width=30)
entry.pack(padx=10, pady=10)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack(padx=10, pady=5)

root.mainloop()
