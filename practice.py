from tkinter import *
import random
from tkinter import messagebox
from playsound import playsound

root = Tk()
root.geometry("500x500")
root.title("Generate Your Numbers")

numb_ans = StringVar()
numb_ent = StringVar()
same_ans = StringVar()
mylist = []
mynewlist = [numb_ent]
same_numb = []

ent_numb = Entry(root, textvariable=numb_ent)
ent_numb.place(x=50, y=25)
Label(root, textvariable=numb_ans, bg="sky blue").place(x=50, y=50)
Label(root, textvariable=same_ans, bg="sky blue").place(x=50, y=80)


def generate():
    x = 0
    playsound("audio/here they come.mp3")
    while x < 6:
        number = random.randint(1, 49)
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


gen_btn = Button(root, text="Generate", command=generate)
gen_btn.place(x=50, y=100)

ge_btn = Button(root, text="check same", command=samenumb)
ge_btn.place(x=150, y=100)

root.mainloop()
