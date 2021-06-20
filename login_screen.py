from tkinter import *
import rsaidnumber
from datetime import datetime, timedelta
from tkinter import messagebox
import re
from playsound import playsound

root = Tk()
root.geometry("700x700")
root.title("Login Screen")
root.config(bg="#FFC107")


class LoginAccess:
    player_name = StringVar()
    player_email = StringVar()
    user_id = StringVar()
    id_res = StringVar()

    def __init__(self, master):
        self.lotto_logo = PhotoImage(file="images/loto logo 1.png")
        self.canvas = Canvas(master, width=270, height=180, highlightthickness="0")
        self.canvas.create_image(0, 0, anchor=NW, image=self.lotto_logo)
        self.canvas.place(x=220, y=10)

        # self.sa_flag = PhotoImage(file="images/sa flag.png")
        # self.canvas = Canvas(master, width=158, height=100, highlightthickness="0")
        # self.canvas.create_image(0, 0, anchor=NW, image=self.sa_flag)
        # self.canvas.place(x=10, y=280)

        self.login_frame = LabelFrame(master, padx=50, pady=30, width=378, height=290, bg="#EED313")
        self.login_frame.place(x=230, y=250)

        self.login_pic = PhotoImage(file="images/login logo.PNG")
        self.canvas1 = Canvas(self.login_frame, width=50, height=45, borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0 )
        self.canvas1.create_image(0, 0, anchor=NW, image=self.login_pic)
        self.canvas1.grid(column=2, row=1)

        self.label_name = Label(self.login_frame, text="Name", bg="#EED313")
        self.label_name.grid(column=2, row=2)

        self.label_email = Label(self.login_frame, text="Email Address", bg="#EED313")
        self.label_email.grid(column=2, row=4)

        self.label_id = Label(self.login_frame, text="ID Number", bg="#EED313")
        self.label_id.grid(column=2, row=6)

        self.empty_lab = Label(self.login_frame, text="", bg="#EED313")
        self.empty_lab.grid(column=2, row=8)

        self.name_ent = Entry(self.login_frame, textvariable=self.player_name)
        self.name_ent.grid(column=2, row=3)

        self.email_ent = Entry(self.login_frame, textvariable=self.player_email)
        self.email_ent.grid(column=2, row=5)

        self.id_ent = Entry(self.login_frame, textvariable=self.user_id)
        self.id_ent.grid(column=2, row=7)

        self.log_btn = Button(master, text="Login", command=self.name, bg="#EED313", borderwidth="2", cursor="hand2", foreground="black")
        self.log_btn.place(x=365, y=450)

        self.back_icon = PhotoImage(file="images/back btn.PNG")
        self.back_btn = Button(master, image=self.back_icon, command=self.back, bg="#EED313", cursor="hand2", borderwidth=1, highlightthickness=0, highlightbackground="#FFC107", bd=0)
        self.back_btn.place(x=425, y=255)

        self.clear_btn = Button(master, text="Clear",command=self.clear, bg="#EED313", borderwidth="2", cursor="hand2", foreground="black")
        self.clear_btn.place(x=310, y=450)

        self.ithuba_logo = PhotoImage(file="images/ithuba.PNG")
        self.canvas = Canvas(master, width=178, height=55, highlightthickness="0")
        self.canvas.create_image(0, 0, anchor=NW, image=self.ithuba_logo,)
        self.canvas.place(x=500, y=620)

    def name(self):
        try:
            pn = len(self.player_name.get())
            found = False

            for x in range(pn):

                if self.player_name.get()[x]:
                    found = True

            if found == True:
                pass

            else:
                messagebox.showerror("Login Failed", "Please enter a user name")
            self.email()
            with open("Game_Info.txt", "w") as written:
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
        # found = False
        if(re.search(regex, self.player_email.get() )):
            # found == True
            pass
        else:
            messagebox.showerror("Entry Invalid", "Please enter a valid Email Address")
        self.dob()

    def dob(self):
        try:
            id_number = rsaidnumber.parse(self.id_ent.get())
            age = (datetime.today() - id_number.date_of_birth) // timedelta(days=365.245)
            self.id_res.set(age)
            # found = False
            if age >= 18:
                # found == True
                pass

            elif age < 18:
                young = 18 - age
                messagebox.showerror("You are too young to play", "Please try again in " + str(young) + " years")
                root.destroy()
                import mini_game
        except ValueError:
            messagebox.showerror("Entry Invalid", "Invalid ID Number. Try Again")
        if len(self.user_id.get()) < 13:
            messagebox.showerror("Entry Invalid", "ID Number characters missing")
        elif len(self.user_id.get()) > 13:
            messagebox.showerror("Entry Invalid", "ID Number characters exceeding limit")
        self.all_func()

    def all_func(self):
        playsound("audio/access granted.mp3")
        messagebox.showinfo("Access Granted", "Let's Play")
        root.destroy()
        import lotto_game

    def back(self):
        playsound("audio/click.mp3")
        root.destroy()
        import main

    def clear(self):
        playsound("audio/sweep.mp3")
        self.name_ent.delete(0, END)
        self.email_ent.delete(0, END)
        self.id_ent.delete(0, END)


d = LoginAccess(root)
root.mainloop()
