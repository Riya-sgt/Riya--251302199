import tkinter as tk

# Function to update the expression
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Function to evaluate the expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set(" error ")
        expression = ""

# Function to clear the screen
def clear():
    global expression
    expression = ""
    equation.set("")

# Main window
root = tk.Tk()
root.title("GUI Calculator")
root.geometry("300x350")

expression = ""
equation = tk.StringVar()

# Entry box
entry = tk.Entry(root, textvariable=equation, font=('Arial', 18), bd=10, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
]

for (text,row,col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial',14),
                        command=equalpress)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial',14),
                        command=lambda t=text: press(t))
    btn.grid(row=row, column=col)

# Clear button
clear_btn = tk.Button(root, text="C", width=22, height=2, font=('Arial',14), command=clear)
clear_btn.grid(row=5, column=0, columnspan=4)

root.mainloop()
