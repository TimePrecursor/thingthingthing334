# -*- coding: utf-8 -*-
"""
Created on Sun May 26 13:15:54 2024

@author: Time
"""


# import all needed components
# from the tkinter library
from tkinter import filedialog
import datetime as dt


# Function for opening the 
# file explorer window


#not needed right now
def filemenu_open():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files","*.txt*"),
                                                       ("all files","*.*")))

    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)


# menu_save the last output with 
# time/date and type
# of decrype/encrypt
def filemenu_Save(file_in, file_out, y):
    x = dt.datetime.now()
    date = x.strftime("%x")
    time = x.strftime("%X")
    type_ = str(y)
    f = open("myfile.txt", "w")
    f.write(f"{date} | {time} | {type_} | Input: {file_in} Output: {file_out}")
    f.close()