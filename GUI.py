from tkinter import *

root = Tk()
root.title('Cutting Stock Problem Solver')

frame = LabelFrame(root,text = "This is my frame...", padx = 300, pady = 200)
frame.pack(padx=10, pady=10)
b = Button(frame,text="Calculate")
b.pack()
root.mainloop()