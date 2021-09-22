from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def time():
	string = strftime('%H:%M:%S %p')  # military time
	label.config(text = string)
	label.after(1000, time)

label = Label(root, font = ("TkDefaultFont", 80), background = 'black', foreground = 'cyan')
label.pack(anchor = 'center')
time()

mainloop()