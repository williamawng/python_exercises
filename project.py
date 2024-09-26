import tkinter

window = tkinter.Tk()

counter = tkinter.IntVar()
counter.set(0)
def click():
    counter.set(counter.get() +1)
if __name__ == '__main__':
    window = tkinter.Tk()
    # The model.
    counter = tkinter.IntVar()
    counter.set(0)

frame = tkinter.Frame(window)
frame.pack()

button = tkinter.Button(frame, text='Click', command=click)
button.pack()
label = tkinter.Label(frame, textvariable=counter)
label.pack()
# button0 = tkinter.Button(frame, text='0', command = click)
# button0.pack(side='left')

# button9 = tkinter.Button(frame, text='9', command=click)
# button9.pack(side='right')

# button8 = tkinter.Button(frame, text='8', command=click)
# button8.pack(side='right')

# button7 = tkinter.Button(frame, text='7', command=click)
# button7.pack(side='right')

# button6 = tkinter.Button(frame, text='6', command=click)
# button6.pack(side='right')

# button5 = tkinter.Button(frame, text='5', command=click)
# button5.pack(side='right')

# button4 = tkinter.Button(frame, text='4', command=click)
# button4.pack(side='right')

# button3 = tkinter.Button(frame, text='3', command=click)
# button3.pack(side='right')

# button2 = tkinter.Button(frame, text='2', command = click)
# button2.pack(side='right')

# button1 = tkinter.Button(frame, text='1', command = click)
# button1.pack(side='right')



window.mainloop()