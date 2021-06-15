from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.geometry("500x500")
root.title("Generate Your Numbers")

numb_ans = StringVar()
numb_ent = StringVar()
mylist = []
mynewlist = [numb_ent]

ent_numb = Entry(root, textvariable=numb_ent)
ent_numb.place(x=50, y=25)
Label(root, textvariable=numb_ans).place(x=50, y=50)


def generate():
    for x in range(1, 7):
        number = random.randint(1, 49)
        mylist.append(number)
        numb_ans.set(mylist)
    if numb_ans == numb_ent.get():
        messagebox.showinfo("you win", "Weldone")
    elif numb_ans != numb_ent.get():
        messagebox.showinfo("you loose", "try again")


gen_btn = Button(root, text="Generate", command=generate)
gen_btn.place(x=50, y=100)

root.mainloop()
