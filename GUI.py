from tkinter import *

root = Tk()
root.title('Cutting Stock Problem Solver')
root.geometry('940x500')
root.config(bg='#119ff1')

#widgets
left_frame = Frame(root, bd=2, relief=SOLID, padx=10, pady=10)

Label(left_frame, text="Insert width of demands", font=('Times', 14)).grid(row=0, column=0, sticky=W, pady=10)
Label(left_frame, text="Insert quantity", font=('Times', 14)).grid(row=1, column=0, pady=10)
Label(left_frame, text="Insert width of stock", font=('Times', 14)).grid(row=2, column=0, pady=10)
demands = Entry(left_frame, font=('Times', 14))
quantity = Entry(left_frame, font=('Times', 14))
stock = Entry(left_frame, font=('Times', 14))
calculate_btn = Button(left_frame, width=15, text='Calculate', font=('Times', 14), command=None)

right_frame = Frame(root, bd=2, relief=SOLID, padx=10, pady=10)

# widgets placement
demands.grid(row=0, column=1, pady=10, padx=20)
quantity.grid(row=1, column=1, pady=10, padx=20)
stock.grid(row=2, column=1, pady=10, padx=20)
calculate_btn.grid(row=3, column=1, pady=10, padx=20)
left_frame.place(x=50, y=50)



# infinite loop
root.mainloop()