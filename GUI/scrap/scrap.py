from tkinter import *
import tkinter as tk
from tkinter import messagebox

#initiate the instance
root = tk.Tk()

def button1():
    x = 0

def clear():
    x = 0

b = Button(root, text="Enter", width=10, height=2, command=button1)
b.config()
b.pack(side=LEFT)

c = Button(root, text="Clear", width=10, height=2, command=clear)
c.pack(side=LEFT)


scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
text.config(width=35, height=15)
text.pack(side=RIGHT, fill=Y)
scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)

root.mainloop()
