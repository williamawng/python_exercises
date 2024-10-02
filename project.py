import tkinter as tk

calculation = "" # Makes an empty string

def add_to_calculation(symbol): # Defines a function that adds numbers into the GUI using 1 parameter
    global calculation # Makes sure the string variable, calculation, is global
    calculation += str(symbol) # Adds the string variable symbol
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation(): # Defines a function that answers or evaluates the equation
    global calculation # Makes sure the string variable, calculation, is global
    try: # This 'tries' to do the things below:
        result = str(eval(calculation)) # Makes 'calculation' = the evaluation of the answer
        calculation = "" # Resets 'calculation' back to an empty string
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except: # If there is an error in the code then the things below happen:
        clear_field() # Calls the "clear_field()" function
        text_result.insert(1.0, "Error") # Inserts the word "Error"

def clear_field(): # Defines a function that clears the calculator
    global calculation # Makes sure the string variable, calculation, is global
    calculation = "" # Resets 'calculation' back to an empty string
    text_result.delete(1.0, "end")


root = tk.Tk() # sets root to tk.Tk()

root.geometry("300x275") # sets the size of the GUI to 300px by 275px

text_result = tk.Text(root, height= 2, width=16, font=("Arial", 24)) # sets text_result to tk.Text choosing the height, width, and font.
text_result.grid(columnspan=5) # creates a grid with 5 columns

b1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14)) # sets b1 to tk.Button choosing the text, width, font and making the command=lambda
b1.grid(row=2, column=1) # sets b1 to row 2, column 1

b2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14)) # sets b2 to tk.Button choosing the text, width, font and making the command=lambda
b2.grid(row=2, column=2) # sets b2 to row 2, column 2

b3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14)) # sets b3 to tk.Button choosing the text, width, font and making the command=lambda
b3.grid(row=2, column=3) # sets b3 to row 2, column 3

b4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14)) # sets b4 to tk.Button choosing the text, width, font and making the command=lambda
b4.grid(row=3, column=1) # sets b4 to row 3, column 1

b5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14)) # sets b5 to tk.Button choosing the text, width, font and making the command=lambda
b5.grid(row=3, column=2) # sets b5 to row 3, column 2

b6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14)) # sets b6 to tk.Button choosing the text, width, font and making the command=lambda
b6.grid(row=3, column=3) # sets b6 to row 3, column 3

b7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14)) # sets b7 to tk.Button choosing the text, width, font and making the command=lambda
b7.grid(row=4, column=1) # sets b7 to row 4, column 1

b8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14)) # sets b8 to tk.Button choosing the text, width, font and making the command=lambda
b8.grid(row=4, column=2) # sets b8 to row 4, column 2

b9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14)) # sets b9 to tk.Button choosing the text, width, font and making the command=lambda
b9.grid(row=4, column=3) # sets b9 to row 4, column 3

b0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14)) # sets b0 to tk.Button choosing the text, width, font and making the command=lambda
b0.grid(row=5, column=2) # sets b0 to row 5, column 2

b_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14)) # sets b_plus to tk.Button choosing the text, width, font and making the command=lambda
b_plus.grid(row=2, column=4) # sets b_plus to row 2, column 4

b_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14)) # sets b_minus to tk.Button choosing the text, width, font and making the command=lambda
b_minus.grid(row=3, column=4) # sets b_minus to row 3, column 4

b_mul = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14)) # sets b_mul to tk.Button choosing the text, width, font and making the command=lambda
b_mul.grid(row=4, column=4) # sets b_mul to row 4, column 4

b_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14)) # sets b_div to tk.Button choosing the text, width, font and making the command=lambda
b_div.grid(row=5, column=4) # sets b_div to row 5, column 4

b_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14)) # sets b_open to tk.Button choosing the text, width, font and making the command=lambda
b_open.grid(row=5, column=1) # sets b_open to row 5, column 1

b_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14)) # sets b_close to tk.Button choosing the text, width, font and making the command=lambda
b_close.grid(row=5, column=3) # sets b_close to row 5, column 3

b_equal = tk.Button(root, text="=", command= evaluate_calculation, width=11, font=("Arial", 14)) # sets b_equal to tk.Button choosing the text, width, font and making the command= evaluate_calculation
b_equal.grid(row=6, column=3, columnspan=2) # sets b_equal to row 6, column 3, taking the space of 2 columns

b_clear = tk.Button(root, text="C", command= clear_field, width=11, font=("Arial", 14)) # sets b_clear to tk.Button choosing the text, width, font and making the command= evaluate_calculation
b_clear.grid(row=6, column=1, columnspan=2) # sets b_clear to row 6, column 1, taking the space of 2 columns
root.mainloop() # Updates the GUI based on the events handler's actions.