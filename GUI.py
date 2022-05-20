
# import modules
import tkinter as tk
from tkinter import *

import typer
from stock_cutter_1d import solve_model, solve_large_model, StockCutter1D, drawGraph

# configure workspace
root = tk.Tk()
root.title('Cutting Stock Problem Solver')
# root.geometry('500x680')
root.config(bg='#c4c3d0')
# window = tk.Tk()

root.rowconfigure(0, minsize=150, weight=1)
root.columnconfigure([0, 1, 2, 4], minsize=8, weight=1)

stock_length = globals()["stock_length"] = tk.StringVar()

vasi_gia_titlo = tk.Frame(root, bd=2, relief=SOLID, bg='#efdecd', padx=10, pady=10)
vasi_gia_titlo.rowconfigure(0, minsize=50, weight=1)
vasi_gia_titlo.columnconfigure([0, 1, 2, 4], minsize=8, weight=1)
vasi_gia_titlo.grid(row=0, column=0, sticky="news")
titlos = Label(vasi_gia_titlo, font=('Times', 16, 'bold'), bg='#efdecd', text="Welcome to Cutting Stock Problem Solver",
               fg="black", bd=5, padx=50, pady=10)
titlos.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

vasi_gia_eisagwgh = tk.Frame(root, bd=2, relief=SOLID, bg='#efdecd', padx=10, pady=10)
vasi_gia_eisagwgh.rowconfigure(0, minsize=50, weight=1)
vasi_gia_eisagwgh.columnconfigure([0, 1, 2, 4], minsize=8, weight=1)
vasi_gia_eisagwgh.grid(row=1, column=0, sticky="news")

enter_stock_length = Entry(vasi_gia_eisagwgh, textvariable=stock_length, width=45)
enter_stock_length.grid(row=0, column=1)
enter_stock_length.insert(0, "")
enter_stock_length.insert(0,"Enter stock length")
enter_stock_length_lbl = Label(vasi_gia_eisagwgh, font=('aria', 12, 'bold'), text="STOCK LENGTH :",
                               bg='#efdecd', anchor=W, padx=10, pady=20).grid(row=0, column=0)


class InputFields:          #The code starts by initializing the input fields.
                            #The variable startFields is initialized to 3, and the counter variable is set to 0.
    startFields = 3
    counter = 0

    ## init input fileds @start
    def initInputForm(numOfInputFields=startFields):     #is defined to initialize the input fields for each of the number of inputs specified in startFields .
                                                        #For example, if startFields was set to 4 then this code would initialize four input fields with their respective variables: InputField1 , InputField2 , InputEnd3 , and InputEnd4 .
        InputFields.counter = InputFields.startFields
        for i in range(numOfInputFields):               # a loop iterates through all of the numbers in range(numOfInputFields) which are three in this case.
            # Dynamic variables
            length = globals()["length%s" % i] = tk.StringVar()         #In order for these loops to work properly they need two dynamic variables: length and quantity .
            quantity = globals()["quantity%s" % i] = tk.StringVar()     #These variables are declared as global string vars so that they can be accessed from anywhere
                                                                        #They are used later on when calculating how many times an item should be added or subtracted from an inventory list based on what has been entered into one of these input boxes.
                                                                        #The first line inside the loop sets up a new length var named length with value "length%i" % i where i represents one of three possible values (0-2).
                                                                        #This creates a new string var with name "length" that
                                                                        #The code initializes the input fields with a start value of 3.
                                                                        #The counter variable is initialized to 0 and the length and quantity variables are initialized to "".
            enter_length = Entry(vasi_gia_eisagwgh, textvariable=length, width=25)
            enter_length.grid(row=(i + 1), column=1)
            enter_length.insert(0, "")
            enter_length.insert(0,"Enter desired length")
            enter_length_lbl = Label(vasi_gia_eisagwgh, font=('aria', 12, 'bold'), text="LENGTH :",
                                     bg='#efdecd', anchor=W, padx=10).grid(row=(i + 1), column=0)

            enter_quantity = Entry(vasi_gia_eisagwgh, textvariable=quantity, width=25)
            enter_quantity.grid(row=(i + 1), column=4)
            enter_quantity.insert(0, "")
            enter_quantity.insert(0,"Enter desired quantity")
            enter_quantity_lbl = Label(vasi_gia_eisagwgh, font=('aria', 12, 'bold'), text="QUANTITY :",
                                       bg='#efdecd', anchor=W, padx=10).grid(row=(i + 1), column=3)

    ## Add extra input field
    def addInputField():
        InputFields.counter += 1
        # Dynamic variables
        length = globals()["length%s" % (InputFields.counter - 1)] = tk.StringVar()
        quantity = globals()["quantity%s" % (InputFields.counter - 1)] = tk.StringVar()

        enter_length = Entry(vasi_gia_eisagwgh, textvariable=length, width=25)
        enter_length.grid(row=InputFields.counter, column=1)
        enter_length.insert(0, "")
        # enter_length.insert(0,"Enter desired length")
        enter_length_lbl = Label(vasi_gia_eisagwgh, font=('aria', 12, 'bold'), text="LENGTH :",
                                 bg='#efdecd', anchor=W, padx=10).grid(row=InputFields.counter, column=0)

        enter_quantity = Entry(vasi_gia_eisagwgh, textvariable=quantity, width=25)
        enter_quantity.grid(row=InputFields.counter, column=4)
        enter_quantity.insert(0, "")
        # enter_quantity.insert(0,"Enter desired quantity")
        enter_quantity_lbl = Label(vasi_gia_eisagwgh, font=('aria', 12, 'bold'), text="QUANTITY :",
                                   bg='#efdecd', anchor=W, padx=10).grid(row=InputFields.counter, column=3)


## init start Input Fields
InputFields.initInputForm()

# Toggler function for button "Show/Hide results"
hidden = False


def toggleTextBox():
    global hidden
    if hidden:
        textBox.grid()
        show_btn["text"] = "HIDE RESULTS"
    else:
        textBox.grid_remove()
        show_btn["text"] = "SHOW RESULTS"
    hidden = not hidden


# Function for Generate button
def calculate():
    entries = []
    for i in range(InputFields.counter):
        length = globals()["length%s" % i].get()
        quantity = globals()["quantity%s" % i].get()

        if (length != "" and quantity != ""):
            try:
                length = int(length)
                quantity = int(quantity)
                row = [quantity, length]
                entries.append(row)
            except ValueError:
                print("That's not an int!")

    res = [entries, int(stock_length.get())]
    c_rolls = entries
    p_rolls = [[1, res[1]]]  # 1 is unused = quantity of rod to cut from

    consumed_big_rolls = StockCutter1D(c_rolls, p_rolls, output_json=False, large_model=False)
    # consumed_big_rolls = StockCutter1D(c_rolls, p_rolls, output_json=False, large_model=False)

    typer.echo(f"{consumed_big_rolls}")
    textBox.delete(1.0, tk.END)
    for idx, roll in enumerate(consumed_big_rolls):
        # Print to console
        typer.echo(f"Roll #{idx}:{roll}")

        # Print to textbox
        rs = (f"Roll #{idx}:{roll}\n")
        tmp = 0
        print("roll: ", roll)
        for r in roll[1]:
            tmp += int(r)

        textBox.insert(tk.END, rs)
        percent = (f"Used: {(tmp / res[1]) * 100}%\n")
        textBox.insert(tk.END, percent)
        textBox.insert(tk.END, "\n")

    drawGraph(consumed_big_rolls, c_rolls, parent_width=p_rolls[0][1])

# Define a function to clear the Entry Widget Content
def clear_fields():#(numOfInputFields, InputFields):
    enter_stock_length.delete(0, END)
    InputFields.initInputForm()



    '''
    if numOfInputFields > 3 :
    vasi_gia_eisagwgh.destroy()
    vasi_gia_eisagwgh = tk.Frame(root, bd=2, relief=SOLID, bg='#efdecd', padx=10, pady=10)
vasi_gia_eisagwgh.rowconfigure(0, minsize=50, weight=1)
vasi_gia_eisagwgh.columnconfigure([0, 1, 2, 4], minsize=8, weight=1)
vasi_gia_eisagwgh.grid(row=1, column=0, sticky="news")
    else:
    InputFields.initInputForm()
    
    
        for i in range(InputFields.counter):
            length = globals()["length%s" % i].destroy()
            quantity = globals()["quantity%s" % i].destroy()
    InputFields.initInputForm()
    #text.delete(0, END)
    #e.destroy()
'''


# buttons
vasi_gia_btn = tk.Frame(root, bd=2, relief=SOLID, bg='#efdecd', padx=10, pady=10)
vasi_gia_btn.rowconfigure(0, minsize=50, weight=1)
vasi_gia_btn.columnconfigure([0, 1, 2, 4], minsize=8, weight=1)
vasi_gia_btn.grid(row=2, column=0, sticky="news")

add_row_btn = Button(vasi_gia_btn, text="ADD", bg='#efdecd', command=InputFields.addInputField)
add_row_btn.grid(row=1, column=0, padx=10, pady=10)

generate_btn = Button(vasi_gia_btn, text="GENERATE", bg='#efdecd', command=calculate)
generate_btn.grid(row=1, column=1, padx=10, pady=10)

show_btn = Button(vasi_gia_btn, text="HIDE RESULTS", bg='#efdecd', command=toggleTextBox)
show_btn.grid(row=1, column=2, padx=10, pady=10)

clear_btn = Button(vasi_gia_btn, text="CLEAR FIELDS", bg='#efdecd', command=clear_fields)
clear_btn.grid(row=1, column=3, padx=10, pady=10)

quit_btn = Button(vasi_gia_btn, text='Quit', bg='#efdecd', command=root.destroy)
quit_btn.grid(row=1, column=4, padx=10, pady=10)

textBox = tk.Text()
textBox.rowconfigure(0, minsize=1, weight=1)
textBox.columnconfigure([0], minsize=10, weight=1)
textBox.grid(row=4, column=0, sticky="news")
# textBox.grid_remove()

# infinite loop
root.mainloop()


