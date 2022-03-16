
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
# enter_stock_length.insert(0,"Enter stock length")
enter_stock_length_lbl = Label(vasi_gia_eisagwgh, font=('aria', 12, 'bold'), text="STOCK LENGTH :",
                               bg='#efdecd', anchor=W, padx=10, pady=20).grid(row=0, column=0)


class InputFields:
    startFields = 3
    counter = 0

    ## init input fileds @start
    def initInputForm(numOfInputFields=startFields):
        InputFields.counter = InputFields.startFields
        for i in range(numOfInputFields):
            # Dynamic variables
            length = globals()["length%s" % i] = tk.StringVar()
            quantity = globals()["quantity%s" % i] = tk.StringVar()

            enter_length = Entry(vasi_gia_eisagwgh, textvariable=length, width=25)
            enter_length.grid(row=(i + 1), column=1)
            enter_length.insert(0, "")
            # enter_length.insert(0,"Enter desired length")
            enter_length_lbl = Label(vasi_gia_eisagwgh, font=('aria', 12, 'bold'), text="LENGTH :",
                                     bg='#efdecd', anchor=W, padx=10).grid(row=(i + 1), column=0)

            enter_quantity = Entry(vasi_gia_eisagwgh, textvariable=quantity, width=25)
            enter_quantity.grid(row=(i + 1), column=4)
            enter_quantity.insert(0, "")
            # enter_quantity.insert(0,"Enter desired quantity")
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


# buttons
vasi_gia_btn = tk.Frame(root, bd=2, relief=SOLID, bg='#efdecd', padx=10, pady=10)
vasi_gia_btn.rowconfigure(0, minsize=50, weight=1)
vasi_gia_btn.columnconfigure([0, 1, 2, 4], minsize=8, weight=1)
vasi_gia_btn.grid(row=2, column=0, sticky="news")

add_row_btn = Button(vasi_gia_btn, text="ADD", bg='#efdecd', command=InputFields.addInputField)
add_row_btn.grid(row=1, column=0, padx=20, pady=10)

generate_btn = Button(vasi_gia_btn, text="GENERATE", bg='#efdecd', command=calculate)
generate_btn.grid(row=1, column=1, padx=20, pady=10)

show_btn = Button(vasi_gia_btn, text="HIDE RESULTS", bg='#efdecd', command=toggleTextBox)
show_btn.grid(row=1, column=2, padx=20, pady=10)

quit_btn = Button(vasi_gia_btn, text='Quit', command=root.destroy)
quit_btn.grid(row=1, column=3, padx=20, pady=10)

textBox = tk.Text()
textBox.rowconfigure(0, minsize=1, weight=1)
textBox.columnconfigure([0], minsize=10, weight=1)
textBox.grid(row=4, column=0, sticky="news")
# textBox.grid_remove()

# infinite loop
root.mainloop()
'''
global row_index
global column_index
row_index=1
column_index=1
def add_row():
    #vasi_gia_eisagwgh.height += 50
    enter_length = Entry(vasi_gia_eisagwgh, width=25)
    enter_length.grid(row=row_index + 1, column=column_index + 1)
    enter_length.insert(0, "Enter desired length")
    # enter_length_lbl = Label(vasi_gia_eisagwgh, font=('aria', 12, 'bold'), text="LENGTH :",
    # bg='#efdecd', anchor=W).grid(row=0, column=0)

    enter_quantity = Entry(vasi_gia_eisagwgh, width=25)
    enter_quantity.grid(row=row_index + 1, column=column_index + 2)
    enter_quantity.insert(0, "Enter desired quantity")

    row_index + 1
    column_index + 1
'''
'''
#==============================================================
list_of_lengths=[]
list_of_demands=[]

def add_row():
    return
def addClick():
    list_of_lengths.append(enter_length.get())
    list_of_lengths.append(enter_length1.get())
    list_of_lengths.append(enter_length2.get())

    list_of_demands.append(enter_quantity.get())
    list_of_demands.append(enter_quantity1.get())
    list_of_demands.append(enter_quantity2.get())

    print(list_of_lengths)
    print(list_of_demands)
#configure workspace
root = tk.Tk()
root.title('Cutting Stock Problem Solver')
#root.geometry('500x680')
root.config(bg='#c4c3d0')
#window = tk.Tk()

root.rowconfigure(0, minsize=150, weight=1)
root.columnconfigure([0, 1, 2, 4], minsize=8, weight=1)


vasi_gia_titlo = tk.Frame(root, bd=2, relief=SOLID,bg='#efdecd', padx=10, pady=10)
vasi_gia_titlo.rowconfigure(0, minsize=50, weight=1)
vasi_gia_titlo.columnconfigure([0, 1, 2, 4], minsize=8, weight=1)
vasi_gia_titlo.grid(row=0, column=0,sticky="news")
titlos = Label(vasi_gia_titlo, font=('Times', 16, 'bold'),bg='#efdecd', text="Welcome to Cutting Stock Problem Solver", fg="black", bd=5,padx=50, pady=10)
titlos.grid(row=0,column=0, columnspan=2,padx=10,pady=10)

vasi_gia_eisagwgh =tk.Frame(root, bd=2, relief=SOLID,bg='#efdecd', padx=10, pady=10)
vasi_gia_eisagwgh.rowconfigure(0, minsize=50, weight=1)
vasi_gia_eisagwgh.columnconfigure([0, 1, 2, 4], minsize=8, weight=1)
vasi_gia_eisagwgh.grid(row=1, column=0,sticky="news")

enter_stock_length = Entry(vasi_gia_eisagwgh, width =45)
enter_stock_length.grid(row=0, column=1)
enter_stock_length.insert(0,"Enter stock length")
enter_stock_length_lbl = Label(vasi_gia_eisagwgh, font=('aria', 12, 'bold'), text="STOCK LENGTH :",
                         bg='#efdecd', anchor=W,padx=10, pady=20).grid(row=0, column=0)
#1
enter_length = Entry(vasi_gia_eisagwgh, width =25)
enter_length.grid(row=1, column=1)
enter_length.insert(0,"Enter desired length")
enter_length_lbl = Label(vasi_gia_eisagwgh, font=('aria', 12, 'bold'), text="LENGTH :",
                         bg='#efdecd', anchor=W,padx=10).grid(row=1, column=0)

enter_quantity = Entry(vasi_gia_eisagwgh, width =25)
enter_quantity.grid(row=1, column=4)
enter_quantity.insert(0,"Enter desired quantity")
enter_quantity_lbl = Label(vasi_gia_eisagwgh, font=('aria', 12, 'bold'), text="QUANTITY :",
                           bg='#efdecd', anchor=W, padx=10).grid(row=1, column=3)
#2
enter_length1 = Entry(vasi_gia_eisagwgh, width =25)
enter_length1.grid(row=2, column=1)
enter_length1.insert(0,"Enter desired length")
enter_length_lbl1 = Label(vasi_gia_eisagwgh, font=('aria', 12, 'bold'), text="LENGTH :",
                         bg='#efdecd', anchor=W,padx=10).grid(row=2, column=0)

enter_quantity1 = Entry(vasi_gia_eisagwgh, width =25)
enter_quantity1.grid(row=2, column=4)
enter_quantity1.insert(0,"Enter desired quantity")
enter_quantity_lbl1 = Label(vasi_gia_eisagwgh, font=('aria', 12, 'bold'), text="QUANTITY :",
                           bg='#efdecd', anchor=W, padx=10).grid(row=2, column=3)
#3
enter_length2 = Entry(vasi_gia_eisagwgh, width =25)
enter_length2.grid(row=3, column=1)
enter_length2.insert(0,"Enter desired length")
enter_length_lbl2 = Label(vasi_gia_eisagwgh, font=('aria', 12, 'bold'), text="LENGTH :",
                         bg='#efdecd', anchor=W,padx=10).grid(row=3, column=0)

enter_quantity2 = Entry(vasi_gia_eisagwgh, width =25)
enter_quantity2.grid(row=3, column=4)
enter_quantity2.insert(0,"Enter desired quantity")
enter_quantity_lbl2 = Label(vasi_gia_eisagwgh, font=('aria', 12, 'bold'), text="QUANTITY :",
                           bg='#efdecd', anchor=W, padx=10).grid(row=3, column=3)

#buttons
vasi_gia_btn =tk.Frame(root, bd=2, relief=SOLID,bg='#efdecd', padx=10, pady=10)
vasi_gia_btn.rowconfigure(0, minsize=50, weight=1)
vasi_gia_btn.columnconfigure([0, 1, 2, 4], minsize=8, weight=1)
vasi_gia_btn.grid(row=2, column=0,sticky="news")

add_row_btn = Button(vasi_gia_btn,text ="ADD",bg='#efdecd')
add_row_btn.grid(row=1,column=0,padx=20,pady=10)

generate_btn= Button(vasi_gia_btn,text ="GENERATE",bg='#efdecd',command=addClick())
generate_btn.grid(row=1,column=1,padx=20,pady=10)


stock_length = enter_stock_length.get()



'''

#===================================================
'''
Vasi = LabelFrame(root, text='Parameters', bd=10, relief=RIDGE)
Vasi.grid(row=3, column=0, sticky=W,padx=10, pady=10)

stock_frame = Frame(Vasi)
stock_frame.pack()

# scrollbar
parameter_scroll = Scrollbar(stock_frame)
parameter_scroll.pack(side=RIGHT, fill=Y)

parameter_scroll = Scrollbar(stock_frame, orient='horizontal')
parameter_scroll.pack(side=BOTTOM, fill=X)

my_Table = ttk.Treeview(stock_frame, yscrollcommand=parameter_scroll.set, xscrollcommand=parameter_scroll.set)

my_Table.pack(anchor=W)

parameter_scroll.config(command=my_Table.yview)
parameter_scroll.config(command=my_Table.xview)
my_Table['columns'] = ('DESIRED LENGTHS', 'QUANTITY')

# format our column
my_Table.column("#0", width=0, stretch=NO)
my_Table.column("DESIRED LENGTHS", anchor=CENTER, width=150)
my_Table.column("QUANTITY", anchor=CENTER, width=150)


# Create Headings
my_Table.heading("#0", text="", anchor=CENTER)
my_Table.heading("DESIRED LENGTHS", text="DESIRED LENGTHS", anchor=CENTER)
my_Table.heading("QUANTITY", text="QUANTITY", anchor=CENTER)
'''
#===========================================



    #enter_quantity_lbl = Label(vasi_gia_eisagwgh, font=('aria', 12, 'bold'), text="QUANTITY :",
                          #     bg='#efdecd', anchor=W, padx=10).grid(row=0, column=3)


#titlos.grid(row=0, column=0,sticky="ew")

#enter_length = Entry(root, width = 50)
#enter_length.pack()
#enter_length.insert(0,"Enter desired length")

#message = Label(master=root, font=('Times', 12, 'bold'), text="To solve your problem choose: ", fg="black", width=10, height=10, bd=5,padx=50, pady=30)

#titlos.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

#frame1 = tk.Frame(root, bd=2, relief=SOLID,bg='#efdecd', padx=10, pady=10)
#Label(frame1, text="Welcome to Cutting Stock Problem Solver", font=('Times', 14),
    #  bg='#efdecd').grid(row=0, column=0, sticky=N,pady=10)
#frame1.pack()
#message.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#================================================================================
'''
#frames
frame1 = tk.Frame(root, bd=2, relief=SOLID,bg='#efdecd', padx=10, pady=10)
Label(frame1, text="Welcome to Cutting Stock Problem Solver", font=('Times', 14),
      bg='#efdecd').grid(row=0, column=0, sticky=N,pady=10)
frame1.place(x=300, y=50)


Vasi = LabelFrame(root, text='Parameters', bd=5, relief=RIDGE)
Vasi.grid(row=0, column=0, sticky=W, padx=70, pady=200)

stock_frame = Frame(Vasi)
stock_frame.pack()

# scrollbar
parameter_scroll = Scrollbar(stock_frame)
parameter_scroll.pack(side=RIGHT, fill=Y)

parameter_scroll = Scrollbar(stock_frame, orient='horizontal')
parameter_scroll.pack(side=BOTTOM, fill=X)

my_Table = ttk.Treeview(stock_frame, yscrollcommand=parameter_scroll.set, xscrollcommand=parameter_scroll.set)

my_Table.pack(anchor=W)

parameter_scroll.config(command=my_Table.yview)
parameter_scroll.config(command=my_Table.xview)
my_Table['columns'] = ('DESIRED LENGTHS', 'QUANTITY')

# format our column
my_Table.column("#0", width=0, stretch=NO)
my_Table.column("DESIRED LENGTHS", anchor=CENTER, width=150)
my_Table.column("QUANTITY", anchor=CENTER, width=150)


# Create Headings
my_Table.heading("#0", text="", anchor=CENTER)
my_Table.heading("DESIRED LENGTHS", text="DESIRED LENGTHS", anchor=CENTER)
my_Table.heading("QUANTITY", text="QUANTITY", anchor=CENTER)





def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fries Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Lunch Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="40", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheese Burger", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)

    roo.mainloop()

btnprice=Button(frame1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="powder blue",command=price)
btnprice.grid(row=7, column=0)




Checkbutton(Vasi, text='Pizza').pack(anchor=W)
Checkbutton(Vasi, text='Noodles').pack(anchor=W)
Checkbutton(Vasi, text='Sandwich').pack(anchor=W)
Checkbutton(Vasi, text='eggs').pack(anchor=W)
'''
#=======================================================================
'''
#table
game_frame = Frame(root)
game_frame.pack()

# scrollbar
game_scroll = Scrollbar(game_frame)
game_scroll.pack(side=RIGHT, fill=Y)

game_scroll = Scrollbar(game_frame, orient='horizontal')
game_scroll.pack(side=BOTTOM, fill=X)

my_game = ttk.Treeview(game_frame, yscrollcommand=game_scroll.set, xscrollcommand=game_scroll.set)

my_game.pack(anchor=W)

game_scroll.config(command=my_game.yview)
game_scroll.config(command=my_game.xview)

# define our column

my_game['columns'] = ('player_Name', 'player_Country', 'player_Medal')

# format our column
my_game.column("#0", width=0, stretch=NO)
my_game.column("player_Name", anchor=CENTER, width=80)
my_game.column("player_Country", anchor=CENTER, width=80)
my_game.column("player_Medal", anchor=CENTER, width=80)

# Create Headings
my_game.heading("#0", text="", anchor=CENTER)
my_game.heading("player_Name", text="Id", anchor=CENTER)
my_game.heading("player_Country", text="Name", anchor=CENTER)
my_game.heading("player_Medal", text="Rank", anchor=CENTER)

# add data
my_game.insert(parent='', index='end', iid=0, text='',
               values=('Tom', 'US', 'Gold'))
my_game.insert(parent='', index='end', iid=1, text='',
               values=('Aandrew', 'Australia', 'NA'))
my_game.insert(parent='', index='end', iid=2, text='',
               values=('Anglina', 'Argentina', 'Silver'))
my_game.insert(parent='', index='end', iid=3, text='',
               values=('Shang-Chi', 'China', 'Bronze'))

my_game.pack()

frame = Frame(root)
frame.pack(pady=20)

# labels
playerid = Label(frame, text="player_id")
playerid.grid(row=0, column=0)

playername = Label(frame, text="player_name")
playername.grid(row=0, column=1)

playerrank = Label(frame, text="Player_rank")
playerrank.grid(row=0, column=2)

# Entry boxes
playerid_entry = Entry(frame)
playerid_entry.grid(row=1, column=0)

playername_entry = Entry(frame)
playername_entry.grid(row=1, column=1)

playerrank_entry = Entry(frame)
playerrank_entry.grid(row=1, column=2)


# Select Record
def select_record():
    # clear entry boxes
    playerid_entry.delete(0, END)
    playername_entry.delete(0, END)
    playerrank_entry.delete(0, END)

    # grab record
    selected = my_game.focus()
    # grab record values
    values = my_game.item(selected, 'values')
    # temp_label.config(text=selected)

    # output to entry boxes
    playerid_entry.insert(0, values[0])
    playername_entry.insert(0, values[1])
    playerrank_entry.insert(0, values[2])


# save Record
def update_record():
    selected = my_game.focus()
    # save new data
    my_game.item(selected, text="", values=(playerid_entry.get(), playername_entry.get(), playerrank_entry.get()))

    # clear entry boxes
    playerid_entry.delete(0, END)
    playername_entry.delete(0, END)
    playerrank_entry.delete(0, END)


# Buttons
select_button = Button(root, text="Select Record", command=select_record)
select_button.pack(pady=10)

edit_button = Button(root, text="Edit ", command=update_record)
edit_button.pack(pady=10)

temp_label = Label(root, text="")
temp_label.pack()
'''
#==============================================================================
'''
#widgets
left_frame = Frame(root, bd=2, relief=SOLID, padx=10, pady=10)

Label(left_frame, text="DESIRED LENGTHS", font=('Times', 14)).grid(row=0, column=0, sticky=W, pady=10)
Label(left_frame, text="QUANTITY", font=('Times', 14)).grid(row=1, column=0, pady=10)
Label(left_frame, text="CAPACITY", font=('Times', 14)).grid(row=2, column=0, pady=10)
demands = Entry(left_frame, font=('Times', 14))
quantity = Entry(left_frame, font=('Times', 14))
stock = Entry(left_frame, font=('Times', 14))
calculate_btn = Button(left_frame, width=15, text='Calculate', font=('Times', 14), command=None)

right_frame = Frame(root, bd=2, relief=SOLID, padx=10, pady=10)
Label(right_frame, text="RESULTS", font=('Times', 14)).grid(row=0, column=0, sticky=W, pady=10)

# widgets placement
demands.grid(row=0, column=1, pady=10, padx=20)
quantity.grid(row=1, column=1, pady=10, padx=20)
stock.grid(row=2, column=1, pady=10, padx=20)
calculate_btn.grid(row=3, column=1, pady=10, padx=20)
left_frame.place(x=50, y=50)
#right_frame.place(x=600,y=50)

button_quit = Button(root, text= 'Exit Program', command= root.quit )
button_quit.grid(row=10, column=5, pady=10, padx=20)
'''

# infinite loop
#root.mainloop()

