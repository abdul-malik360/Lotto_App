from tkinter import *

root = Tk()
root.geometry("600x600")
root.title("Welcome To Ithuba Lotto")
root.config(bg="#FFC107")

lotto_logo = PhotoImage(file="images/loto logo 1.png")
ithuba_logo = PhotoImage(file="images/ithuba.PNG")

# place image
canvas = Canvas(root, width=270, height=180, highlightthickness="0") #
canvas.create_image(0, 0, anchor=NW, image=lotto_logo,)
canvas.place(x=165, y=10)

canvas = Canvas(root, width=178, height=55, highlightthickness="0") #
canvas.create_image(0, 0, anchor=NW, image=ithuba_logo,)
canvas.place(x=400, y=520)





root.mainloop()
