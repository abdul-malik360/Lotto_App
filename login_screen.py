from tkinter import *
import rsaidnumber
from datetime import datetime, timedelta
from tkinter import messagebox

root = Tk()
root.geometry("600x600")
root.title("Login Screen")
root.config(bg="#FFC107")

class LoginAccess:
    id_no = StringVar()
    id_res = StringVar()
    player_name = StringVar()
    player_email = StringVar()


    def __init__(self, master):
        self.label_name = Label(master, text="Enter Name")
        self.label_name.place(x=50, y=200)

        self.name_ent = Entry(master, textvariable=self.player_name)
        self.name_ent.place(x=200, y=200)

        self.email_ent = Entry(master, textvariable=self.player_email)
        self.email_ent.place(x=200, y=150)

        self.id_ent = Entry(master, textvariable=self.id_no)
        self.id_ent.place(x=200, y=250)
        self.id_ans = Label(master, textvariable=self.id_res)
        self.id_ans.place(x=50, y=300)

        self.cal_btn = Button(root, command=self.dob)
        self.cal_btn.place(x=50, y=300)

        self.ithuba_logo = PhotoImage(file="images/ithuba.PNG")

        self.canvas = Canvas(root, width=178, height=55, highlightthickness="0") #
        self.canvas.create_image(0, 0, anchor=NW, image=self.ithuba_logo,)
        self.canvas.place(x=400, y=520)


    def dob(self):
        try:
            id_number = rsaidnumber.parse(self.id_ent.get())
            age = (datetime.today() - id_number.date_of_birth) // timedelta(days=365.245)
            self.id_res.set(age)
        except ValueError:
            messagebox.showerror("Entry Invalid", "Please enter a valid ID Number")

a = LoginAccess(root)
root.mainloop()
