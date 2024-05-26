# -*- coding: utf-8 -*-
"""
Created on Wed May 22 15:40:28 2024

@author: Time
"""


#This will import all the widgets
#and modules which are available in
#tkinter and ttk module
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox




# creates a Tk() object
root = Tk()

#sets the geometry of
#main root window
root.title("Ceasar Cypher")
root.geometry("500x500")
root.resizable(False, False)


# Create a menu with options (Version 1.2)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)


# define functions for
# the menu -

# placeholder function
def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

# fucntion to save the file
def menu_save():
    from function_file1 import filemenu_Save
    filemenu_Save(keyholder.get(), newmsg3.get(), typeoffile.get())


# (a later feature)
# filemenu.add_command(label="Open", command=donothing)

# lets the user save the current output
filemenu.add_command(label="Save", command=menu_save)
# separate
filemenu.add_separator()

# exits the program
filemenu.add_command(label="Exit", command=root.destroy)

# name the cascade as file
menubar.add_cascade(label="File", menu=filemenu)


# Initialise the menu
root.config(menu=menubar)









alphabet_3 = StringVar()
alphabet2 = []
alphabet1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
             'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
for x, y in enumerate(alphabet1):
    y = y.lower()
    alphabet2.insert(x,y)
alphabet_3 = ''.join(alphabet1)


def checkthekey(typelol):
    try:
        x = key.get()
        
    except:
        messagebox.showerror("error", "Please enter only whole numbers (under 25 and over 25") 
    else:
        boolx = bool(isinstance(x, int) == False or x < -25 or x > 26)
        if boolx == True:
            messagebox.showerror("error", "Please enter only whole numbers (under 25 and over 25") 
        elif boolx == False:
            if typelol == "de":
                decrypt()
            elif typelol == "en":
                encrypt()
    
        
        

Label(root, text="Enter your message to decrypt or encrypt!", background='lightgrey' ,
      font=('Arial', 10)).pack(padx=.5,anchor= CENTER)

message = StringVar()
messagebox1 = Entry(root, textvariable=message, width=40,font=("Arial","12"))
messagebox1.pack(pady=10)

# def clear_text():
    # messagebox1.delete(0,END)

Label(root, text="Provide the key!", background='lightgrey' ,
      font=('Arial', 10)).pack(padx=.5,anchor= CENTER)

key = IntVar()
keyholder = Entry(root, textvariable=key, width=10,font=("Arial","20"))
keyholder.pack(pady=20)



def copytoclip(msg1):
    root.clipboard_clear()
    root.clipboard_append(msg1)
    if newmsg == "":
        labelez['text']=('Output:',"None")
    else:
        labelez['text']=('Output:',newmsg3.get())

def updatelabel():
    labelez['text']=("please only enter english letters!")

# function to open a new window
# on a button click


newmsg = []
typeoffile = StringVar()


def decrypt():
    print("decrypt")
    global newmsg, newmsg3
    newmsg.clear()
    msg = message.get()
    msg = msg.lower()
    try:
        for count, item in enumerate(msg):
            pos1 = alphabet2.index(item)
            pos2 = pos1 - key.get()
            newmsg.append((alphabet1[pos2]))
    except:
        updatelabel()
    newmsg1 = newmsg
    newmsg2 = ''.join(newmsg1)
    newmsg3 = StringVar()
    newmsg3.set(newmsg2)
    copytoclip(newmsg3.get())
    typeoffile.set("decrypt")
    # print("Decrypted message: " + newmsg)
    # messagebox.showinfo("Decrypted", (newmsg2.get(),copytoclip('lol21')))copytoclip('lol21')


def encrypt():
    print("encrypt")
    global newmsg, newmsg3
    newmsg.clear()
    msg = message.get()
    msg = msg.lower()
    try:
        for count, item in enumerate(msg):
            pos1 = alphabet2.index(item)
            pos2 = pos1 + key.get()
            newmsg.append((alphabet1[pos2]))
    except:
        updatelabel()
    newmsg1 = newmsg
    newmsg2 = ''.join(newmsg1)
    newmsg3 = StringVar()
    newmsg3.set(newmsg2)
    copytoclip(newmsg3.get())
    typeoffile.set("encrypt")
    # messagebox.showinfo("Encrypted", newmsg)


my_text = "ez"
labelez = Label(root, text =(" "))

labelez.pack(pady=10)

# a button widget which will open a
# new window on button click
btn = Button(root,
			text ="Click to Decrypt",
			command= lambda: checkthekey("de")) #, checkthekey("en"))
btn.pack(pady = 10)
btn = Button(root,
			text ="Click to Encrypt",
			command= lambda: checkthekey("en"))
btn.pack(pady = 10)



# mainloop, runs infinitely
root.update_idletasks()
mainloop()
