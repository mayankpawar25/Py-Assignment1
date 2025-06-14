# Step1: import
from tkinter import *

# Step2: Gui interaction
window = Tk()
window.geometry('500x500')

# Step3: Adding inputs

# Entry Box
e = Entry(window, width=56, borderwidth=5)
e.place(x=0, y=0)

# Buttons
def click(num):
    result=e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))

b = Button(window, text='1', width=12, command=lambda:click(1))
b.place(x=10, y=60)

b = Button(window, text='2', width=12, command=lambda:click(2))
b.place(x=100, y=60)

b = Button(window, text='3', width=12, command=lambda:click(3))
b.place(x=190, y=60)

b = Button(window, text='4', width=12, command=lambda:click(4))
b.place(x=10, y=120)

b = Button(window, text='5', width=12, command=lambda:click(5))
b.place(x=100, y=120)

b = Button(window, text='6', width=12, command=lambda:click(6))
b.place(x=190, y=120)

b = Button(window, text='7', width=12, command=lambda:click(7))
b.place(x=10, y=180)

b = Button(window, text='8', width=12, command=lambda:click(8))
b.place(x=100, y=180)

b = Button(window, text='9', width=12, command=lambda:click(9))
b.place(x=190, y=180)

b = Button(window, text='0', width=12, command=lambda:click(0))
b.place(x=10, y=240)

b = Button(window, text='+', width=12, command=lambda:click('+'))
b.place(x=100, y=240)

b = Button(window, text='-', width=12, command=lambda:click('-'))
b.place(x=190, y=240)

b = Button(window, text='*', width=12, command=lambda:click('*'))
b.place(x=10, y=300)

b = Button(window, text='/', width=12, command=lambda:click('/'))
b.place(x=100, y=300)

b = Button(window, text='=', width=12)
b.place(x=190, y=300)

b = Button(window, text='Clear', width=12)
b.place(x=10, y=350)

# Step4: Mainloop
mainloop()