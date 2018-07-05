import sys
import tkinter
from tkinter import*

def display():
     print("Bhai main ghr jaara ")
     sys.exit()
root=Tk()
lab=Label(root,text="hello world")
b=Button(root,text="exit",command=exit)
b.pack()
root.mainloop()
