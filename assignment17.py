
#Q1. Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.
#SOL.
import tkinter
from tkinter import *
import sys
def display():
    sys.display()

root=Tk()
root.title("my first gui assignment")
root.geometry("250x250")
root.resizable(False,False)
a=Label(root,text="hello world",width=150)
a.pack()
b=Button(root,text="Exit",command=exit)
b.pack()
root.mainloop()    



#Q2. Write a python program to in the same interface as above and create a action when the button is click it will display some tex
#SOL
import tkinter
from tkinter import*

def display():  
    print("hello world!")

root=Tk()
b=Button(root,text="hello",width=25,bg='blue',fg='white',command=display)
b.pack()
root.mainloop()



#Q3. Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text.
#SOL.
import tkinter
from tkinter import *
import sys
def Change():
	label.config(text= "Chaai Peelo")
root = Tk()
label = Label(root,text="hello friends")
label.grid(row = 0)
btn = Button(root, text="Change",command=Change)
btn.grid(row= 1)
btn2 = Button(root, text="Exit",command=sys.exit)
btn2.grid(row= 2)
root.mainloop()

 
 

#Q4. Write a python program using tkinter interface to take an input in the GUI program and print it.
#SOL.

import tkinter
from tkinter import *

def show():
	print(entry.get())

root=Tk()
root.title("My App")
root.geometry("250x250")
root.resizable(True,True)
root.minsize(200,200)
entry=Entry(root,width=20)
entry.pack()
b=Button(root,text='click',width=20,command=show)
b.pack()
root.mainloop()
