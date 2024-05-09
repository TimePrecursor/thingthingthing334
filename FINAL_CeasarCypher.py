# -*- coding: utf-8 -*-


# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#                        The Gui

# creates a Tk() object
root = Tk()

# sets the geometry (size of the window) and
# creates the main root window
root.title("Ceasar Cypher")
root.geometry("400x400")
root.resizable(False, False)



# This creates a label to go over the user input (message to be encrypted/decrypted)
Label(root, text="Enter your message to decrypt or encrypt!", background='lightgrey' ,font=('Arial', 10)).pack(padx=.5,anchor= CENTER)



# This creates an entry box (user input box) and a variable to store said user input
message = StringVar()
messagebox1 = Entry(root, textvariable=message, width=40,font=("Arial","12"))
messagebox1.pack(pady=10)





mainloop()