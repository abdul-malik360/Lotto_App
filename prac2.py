from tkinter import *


root = Tk()
root.geometry("600x600")
root.title("LOTTO GAME")
root.config(bg="#FFC107")


def choose_number():
    my_label.config(text="1")


number_pic = PhotoImage(file="1.png")
numb_label = Label(image=number_pic)

btn = Button(root, image=number_pic, command=choose_number, borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
btn.place(x=50, y=150)

my_label = Label(root, text="")
my_label.place(x=50, y=250)


root.mainloop()
