from tkinter import *

window = Tk()

window.title('Simple Program')
window.geometry('500x700')
window.config(bg="#A2a2a2")
frame1 = Frame(window, bg="#2f2f2f", width=300, height=300, cursor="dot")
frame2 = Frame(window, bg="#FAFAFA", width=300, height=300, cursor="dotBox")
button1 = Button(frame1, bg="blue", fg="white", text="Button1")
button2 = Button(frame2, bg="green", fg="white", text="Button2")
button3 = Button(frame1, bg="red", fg="white", text="Button3")
frame1.pack(side=TOP)
frame2.pack(side=BOTTOM)
button1.pack()
button2.pack()
button3.pack()
mainloop()