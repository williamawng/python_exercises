import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


root = tk.Tk()

root.geometry("300x275")

text_result = tk.Text(root, height= 2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

b1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
b1.grid(row=2, column=1)

b2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
b2.grid(row=2, column=2)

b3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
b3.grid(row=2, column=3)

b4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
b4.grid(row=3, column=1)

b5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
b5.grid(row=3, column=2)

b6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
b6.grid(row=3, column=3)

b7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
b7.grid(row=4, column=1)

b8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
b8.grid(row=4, column=2)

b9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
b9.grid(row=4, column=3)

b0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
b0.grid(row=5, column=2)

b_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
b_plus.grid(row=2, column=4)

b_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
b_minus.grid(row=3, column=4)

b_mul = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
b_mul.grid(row=4, column=4)

b_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
b_div.grid(row=5, column=4)

b_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
b_open.grid(row=5, column=1)

b_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
b_close.grid(row=5, column=3)

b_equal = tk.Button(root, text="=", command= evaluate_calculation, width=11, font=("Arial", 14))
b_equal.grid(row=6, column=3, columnspan=2)

b_clear = tk.Button(root, text="C", command= clear_field, width=11, font=("Arial", 14))
b_clear.grid(row=6, column=1, columnspan=2)
root.mainloop()