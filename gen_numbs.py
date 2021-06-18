from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.geometry("500x500")
root.title("Generate Your Numbers")

numb_ans = StringVar()
numb_ent = StringVar()
same_ans = StringVar()
mylist = []
mynewlist = []
same_numb = []

numb_lab = Label(root, text="", bg="sky blue", textvariable=numb_ent)
numb_lab.place(x=50, y=25)
Label(root, textvariable=numb_ans, bg="sky blue").place(x=50, y=50)
Label(root, textvariable=same_ans, bg="sky blue").place(x=50, y=80)


def generate():
    x = 0
    while x < 1:
        number = random.randint(1, 2)
        if number not in mylist:
            mylist.append(number)
            x = x + 1

    else:
        x = x - 1

    mylist.sort()
    mynewlist.sort()
    numb_ans.set(mylist)


def samenumb():
    for i in numb_ans.get():
        if i in numb_ent.get():
            same_numb.append(i)
            same_ans.set(same_numb)

def choose():
    numb_ent.set(1)


def choose1():
    numb_ent.set(12)


gen_btn = Button(root, text="Generate", command=generate)
gen_btn.place(x=50, y=100)

ge_btn = Button(root, text="check same", command=samenumb)
ge_btn.place(x=150, y=100)

one_btn = Button(root, text="1", command=choose)
one_btn.place(x=150, y=200)

two_btn = Button(root, text="12", command=choose1)
two_btn.place(x=200, y=200)

root.mainloop()
