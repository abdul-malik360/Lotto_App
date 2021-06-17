
import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.config(bg="sky blue")

Photoshop = tk.Button(root, text = 'Photoshop',

                      bg = 'sky blue',
                      bd =  10,
                      highlightthickness=4,
                      highlightcolor="pink",
                      highlightbackground="black",
                      borderwidth=0)
Photoshop.pack()

root.mainloop()
