import tkinter as tk
import math

# Create main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("420x600")
root.resizable(False, False)

# Entry field
expression = ""
input_text = tk.StringVar()

input_frame = tk.Frame(root)
input_frame.pack()

input_field = tk.Entry(input_frame, textvariable=input_text, font=('Arial', 20), bd=10, insertwidth=2, width=24, borderwidth=4, justify='right')
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Function to update expression
def press(key):
    global expression
    expression += str(key)
    input_text.set(expression)

# Clear screen
def clear():
    global expression
    expression = ""
    input_text.set("")

# Evaluate expression
def equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# Scientific functions
def sin_func():
    try:
        result = math.sin(math.radians(float(expression)))
        input_text.set(result)
    except:
        input_text.set("Error")

def cos_func():
    try:
        result = math.cos(math.radians(float(expression)))
        input_text.set(result)
    except:
        input_text.set("Error")

def tan_func():
    try:
        result = math.tan(math.radians(float(expression)))
        input_text.set(result)
    except:
        input_text.set("Error")

def log_func():
    try:
        result = math.log10(float(expression))
        input_text.set(result)
    except:
        input_text.set("Error")

def ln_func():
    try:
        result = math.log(float(expression))
        input_text.set(result)
    except:
        input_text.set("Error")

def sqrt_func():
    try:
        result = math.sqrt(float(expression))
        input_text.set(result)
    except:
        input_text.set("Error")

def square_func():
    try:
        result = float(expression) ** 2
        input_text.set(result)
    except:
        input_text.set("Error")

# Buttons layout
btns_frame = tk.Frame(root)
btns_frame.pack()

buttons = [
    ('C', 1, 0, clear), ('√', 1, 1, sqrt_func), ('x²', 1, 2, square_func), ('/', 1, 3, lambda: press('/')),

    ('7', 2, 0, lambda: press('7')), ('8', 2, 1, lambda: press('8')), ('9', 2, 2, lambda: press('9')), ('*', 2, 3, lambda: press('*')),

    ('4', 3, 0, lambda: press('4')), ('5', 3, 1, lambda: press('5')), ('6', 3, 2, lambda: press('6')), ('-', 3, 3, lambda: press('-')),

    ('1', 4, 0, lambda: press('1')), ('2', 4, 1, lambda: press('2')), ('3', 4, 2, lambda: press('3')), ('+', 4, 3, lambda: press('+')),

    ('0', 5, 0, lambda: press('0')), ('.', 5, 1, lambda: press('.')), ('=', 5, 2, equal),

    ('sin', 6, 0, sin_func), ('cos', 6, 1, cos_func), ('tan', 6, 2, tan_func),
    ('log', 7, 0, log_func), ('ln', 7, 1, ln_func),

    ('π', 8, 0, lambda: press(str(math.pi))), ('e', 8, 1, lambda: press(str(math.e)))
]

# Create buttons
for (text, row, col, cmd) in buttons:
    tk.Button(btns_frame, text=text, width=8, height=2, font=('Arial', 12),
              command=cmd).grid(row=row, column=col, padx=5, pady=5)

root.mainloop()