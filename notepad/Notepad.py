from tkinter.filedialog import *
import tkinter as tk
from tkinter import *


def saveFile():
    new_file = asksaveasfile(mode="w",filetypes=[("text files",".txt")])
    if new_file is None:
        return
    text = str(entry.get(1.0,END))
    new_file.write(text)
    new_file.close()

def clickMeFile():
    file = open("hello.txt","r")
    #print(file.readline())
    content = file.read()
    entry.insert(INSERT,content)
    file.close()




def openFile():
    global content
    file = askopenfile(mode="r",filetypes=[("text file",".txt")])
    if file is not None:
        content = file.read()
    entry.insert(INSERT,content)
    


def clearFile():
    entry.delete(1.0,END)

canvas = tk.Tk()


canvas.geometry("400x600")
canvas.title("My Notepad")
canvas.config(bg="white")
top = Frame(canvas)

b1 = Button(canvas,text="Open",bg="white",command=openFile)
b1.pack(side=BOTTOM)


b2 = Button(canvas,text="Save",bg="white",command=saveFile)
b2.pack(side=TOP)


b3 = Button(canvas,text="Clear",bg="white",command=clearFile)
b3.pack(side=LEFT)

b4 = Button(canvas,text="Exit",bg="white",command=exit)
b4.pack(side=RIGHT)

b5 = Button(canvas,text="ClickMe",bg="white",command=clickMeFile)
b5.pack(side=RIGHT)

entry = Text(canvas,wrap=WORD,bg="#F9DDA4",font=("poppins",15))
entry.pack(padx=10,pady=5,expand=TRUE,fill=BOTH)

canvas.mainloop()
