
import tkinter
from tkinter import *

root=Tk()

def show():
    a=entry.get()
    b=entry1.get()
    mylist.insert(END,a)
    dict[a]=b
    print(dict)

name=False
Mobile=False

def name(event):
    entry.delete(0,END)
    name=True

def Mobile(event):
    entry1.delete(0,END)
    Mobile=True

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
d={'Rukman':6316226,'Navjeet':456789,'Vidhi':6316234,'Rukman':456789,'dqd':6316234,'Rkmcj':456789,'Vi':6316234,'Rukwmcman':456789,'Vidnckhi':6316234}
mylist=Listbox(root,yscrollcommand=scrollbar.set)
for i in d:
    mylist.insert(END,i)
mylist.pack(fill=BOTH)


entry=Entry(root)
entry.insert(0,'name')
entry.bind("<Button>",name)
entry.pack()

entry1=Entry(root)
entry1.insert(0,'Mobile No.')
entry1.bind("<Button>",Mobile)
entry1.pack()


b=Button(root,text='Submit',command=show)
b.pack()

Scrollbar(mylist,orient="vertical")
scrollbar.config(command=mylist.yview)

#OR

scrollbar['command']=mylist.yview
root.geometry("100x100")
root.minsize(50,50)
root.maxsize(250,250)
root.mainloop()