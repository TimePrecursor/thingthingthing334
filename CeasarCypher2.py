# -*- coding: utf-8 -*-

# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *

# creates a Tk() object
root = Tk()

# sets the geometry and creates 
# the main root window
root.title("Ceasar Cypher")
root.geometry("400x400")
root.resizable(False, False)


alphabet3 = StringVar()
alphabet2 = []
alphabet1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
for x, y in enumerate(alphabet1):
    y = y.lower()
    alphabet2.insert(x,y)
alphabet3 = ''.join(alphabet1)
    
Label(root, text="Enter your message to decrypt or encrypt!", background='lightgrey' ,font=('Arial', 10)).pack(padx=.5,anchor= CENTER)

message = StringVar()
messagebox1 = Entry(root, textvariable=message, width=40,font=("Arial","12"))
messagebox1.pack(pady=10)

def clear_text():
    messagebox1.delete(0,END)

Label(root, text="Provide the key!", background='lightgrey' ,font=('Arial', 10)).pack(padx=.5,anchor= CENTER)

key = IntVar()
Entry(root, textvariable=key, width=10,font=("Arial","20")).pack(pady=20)



def copytoclip(msg1):
    root.clipboard_clear()
    root.clipboard_append(msg1)
    if newmsg == "":
        labelez['text']=('Output:',"None")
    else:
        labelez['text']=('Output:',newmsg)

def updatelabel():
    labelez['text']=("please only enter english letters!")

# function to open a new window 
# on a button click
def decrypt():
    global newmsg
    newmsg = []
    key1 = key.get()
    msg = message.get()
    msg = msg.lower()
    try:    
        for count, item in enumerate(msg):
            pos1 = alphabet2.index(item)
            pos2 = pos1 - key1
            newmsg.append((alphabet1[pos2]))
    except:
        updatelabel()        
    newmsg = ''.join(newmsg)
    newmsg2 = StringVar()
    newmsg2.set(newmsg)
    copytoclip(newmsg2.get())



def encrypt():
    global newmsg
    newmsg = []
    key1 = key.get()
    msg = message.get()
    msg = msg.lower()
    try:    
        for count, item in enumerate(msg):
            pos1 = alphabet2.index(item)
            pos2 = pos1 - key1
            newmsg.append((alphabet1[pos2]))
    except:
        updatelabel()
        
    newmsg = ''.join(newmsg)
    newmsg = ''.join(newmsg)
    newmsg2 = StringVar()
    newmsg2.set(newmsg)
    copytoclip(newmsg2.get())
    


my_text = "ez"
labelez = Label(root, text =(" "))

labelez.pack(pady = 10)

# a button widget which will open a
# new window on button click
btn = Button(root, 
			text ="Click to Decrypt", 
			command= lambda:(decrypt(),clear_text()))
btn.pack(pady = 10)
btn = Button(root, 
			text ="Click to Encrypt", 
			command= lambda:(encrypt(),clear_text()))
btn.pack(pady = 10)





# mainloop, runs infinitely until
#  code is stopped

mainloop()