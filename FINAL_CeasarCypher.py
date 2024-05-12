# -*- coding: utf-8 -*-


# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#                        The Gui
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


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


# creates the label to go above the key entry box
Label(root, text="Provide the key!", background='lightgrey' ,font=('Arial', 10)).pack(padx=.5,anchor= CENTER)

# create the key entry box and varibale to store it
key = IntVar()
Entry(root, textvariable=key, width=10,font=("Arial","20")).pack(pady=20)


# create a label that shows last output
labelez = Label(root, text =(" "))
labelez.pack(pady = 10)


# add a button widget which will decrypt or encrypt
# while clearing previous text in the entry 
btn = Button(root, text ="Click to Decrypt", 
			command= lambda:(decrypt(),clear_text()))
btn.pack(pady = 10)
btn = Button(root, text ="Click to Encrypt", 
			command= lambda:(encrypt(),clear_text()))
btn.pack(pady = 10)




# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#                        The Code
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


alphabet3 = StringVar()
alphabet2 = []
alphabet1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
for x, y in enumerate(alphabet1):
    y = y.lower()
    alphabet2.insert(x,y)
alphabet3 = ''.join(alphabet1)




# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#                        The Functions
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def copytoclip(msg1):
    root.clipboard_clear()
    root.clipboard_append(msg1)
    if newmsg == "":
        labelez['text']=('Output:',"None")
    else:
        labelez['text']=('Output:',newmsg)

def updatelabel():
    labelez['text']=("please only enter english letters!")



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


# create the encrypt function to encrypt
# and copy the output to clipboard
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
    


mainloop()