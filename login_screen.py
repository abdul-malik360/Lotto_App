from tkinter import *
import rsaidnumber
from datetime import datetime, timedelta
from tkinter import messagebox
import re

root = Tk()
root.geometry("600x600")
root.title("Login Screen")
root.config(bg="#FFC107")


class LoginAccess:
    player_name = StringVar()
    player_email = StringVar()
    user_id = StringVar()
    id_res = StringVar()

    def __init__(self, master):
        self.lotto_logo = PhotoImage(file="images/loto logo 1.png")
        self.canvas = Canvas(root, width=270, height=180, highlightthickness="0")
        self.canvas.create_image(0, 0, anchor=NW, image=self.lotto_logo)
        self.canvas.place(x=165, y=10)

        self.sa_flag = PhotoImage(file="images/sa flag.png")
        self.canvas = Canvas(root, width=158, height=100, highlightthickness="0")
        self.canvas.create_image(0, 0, anchor=NW, image=self.sa_flag)
        self.canvas.place(x=10, y=280)

        self.login_frame = LabelFrame(root, padx=50, pady=30, width=378, height=290, bg="#EED313")
        self.login_frame.place(x=200, y=280)

        self.label_name = Label(self.login_frame, text="Name", bg="#EED313")
        self.label_name.grid(column=1, row=1)

        self.label_email = Label(self.login_frame, text="Email Address", bg="#EED313")
        self.label_email.grid(column=1, row=2)

        self.label_id = Label(self.login_frame, text="ID Number", bg="#EED313")
        self.label_id.grid(column=1, row=3)

        self.name_ent = Entry(self.login_frame, textvariable=self.player_name)
        self.name_ent.grid(column=2, row=1)

        self.email_ent = Entry(self.login_frame, textvariable=self.player_email)
        self.email_ent.grid(column=2, row=2)

        self.id_ent = Entry(self.login_frame, textvariable=self.user_id)
        self.id_ent.grid(column=2, row=3)

        self.log_btn = Button(root, text="Login", command=self.email, bg="#EED313", borderwidth="5", cursor="hand2", font=2, foreground="black")
        self.log_btn.place(x=200, y=415)

        self.back_btn = Button(root, text="Back", command=self.back, bg="#EED313", borderwidth="5", cursor="hand2", font=2, foreground="black")
        self.back_btn.place(x=300, y=415)

        self.ithuba_logo = PhotoImage(file="images/ithuba.PNG")

        self.canvas = Canvas(root, width=178, height=55, highlightthickness="0")
        self.canvas.create_image(0, 0, anchor=NW, image=self.ithuba_logo,)
        self.canvas.place(x=400, y=520)

    def name(self):
        try:
            with open("player_id.txt", "w") as written:
                written.write(self.player_name.get())
                written.write("\n")
                written.write(self.player_email.get())
                written.write("\n")
                written.write(self.user_id.get())
                written.write("\n")
                written.write(self.id_res.get())
                written.write("\n")
        except ValueError:
             messagebox.showerror("Entry Invalid", "Please enter a valid Name")

    def email(self):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(regex, self.player_email.get() )):
            pass
        else:
            messagebox.showerror("Entry Invalid", "Please enter a valid Email Address")
        self.dob()

    def dob(self):
        if len(self.user_id.get()) < 13:
            messagebox.showerror("Entry Invalid", "ID Number characters missing")
        elif len(self.user_id.get()) > 13:
            messagebox.showerror("Entry Invalid", "ID Number characters exceeding limit")
        try:
            id_number = rsaidnumber.parse(self.id_ent.get())
            age = (datetime.today() - id_number.date_of_birth) // timedelta(days=365.245)
            self.id_res.set(age)
            if age >= 18:
                messagebox.showinfo("Access Granted", "Let's Play")
                root.destroy()
                import lotto_game
            elif age < 18:
                young = 18 - age
                messagebox.showerror("You are too young to play", "Please try again in " + str(young) + " years")
                root.destroy()
                import mini_game
        except ValueError:

            messagebox.showerror("Entry Invalid", "Invalid ID Number. Try Again")
        self.name()

    def back(self):
        root.destroy()
        import main

c = LoginAccess(root)
root.mainloop()
