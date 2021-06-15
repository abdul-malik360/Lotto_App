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
        self.label_name = Label(master, text="Name")
        self.label_name.place(x=80, y=200)

        self.label_email = Label(master, text="Email Address")
        self.label_email.place(x=80, y=250)

        self.label_id = Label(master, text="ID Number")
        self.label_id.place(x=80, y=300)

        self.name_ent = Entry(master, textvariable=self.player_name)
        self.name_ent.place(x=200, y=200)

        self.email_ent = Entry(master, textvariable=self.player_email)
        self.email_ent.place(x=200, y=250)

        self.id_ent = Entry(master, textvariable=self.user_id)
        self.id_ent.place(x=200, y=300)
        self.id_ans = Label(master, bg="#FFC107", textvariable=self.id_res)
        self.id_ans.place(x=200, y=350)

        self.log_btn = Button(root, text="Login In", command=self.name)
        self.log_btn.place(x=200, y=380)

        self.ithuba_logo = PhotoImage(file="images/ithuba.PNG")

        self.canvas = Canvas(root, width=178, height=55, highlightthickness="0")
        self.canvas.create_image(0, 0, anchor=NW, image=self.ithuba_logo,)
        self.canvas.place(x=400, y=520)

    def name(self):
        try:
            with open("lotto.txt", "w") as written:
                written.write(self.player_name.get())
                written.write("\n")
                written.write(self.player_email.get())
                written.write("\n")
                written.write(self.user_id.get())

        except ValueError:
             messagebox.showerror("Entry Invalid", "Please enter a valid Name")
        #     if self.player_name.get() != str:
        #         messagebox.showerror("Entry Invalid", "Please enter a valid Name")
        self.email()





    def email(self):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(regex, self.player_email.get() )):
            pass
        else:
            messagebox.showerror("Entry Invalid", "Please enter a valid Email Address")
        self.dob()

    def dob(self):
        try:

            id_number = rsaidnumber.parse(self.id_ent.get())
            age = (datetime.today() - id_number.date_of_birth) // timedelta(days=365.245)
            self.id_res.set(age)
            if age >= 18:
                messagebox.showinfo("Access Granted", "Lets Play")
                root.destroy()
                import lotto_game
            elif age < 18:
                young = 18 - age
                messagebox.showerror("You are too young to play", "Please try again in " + str(young) + " years")
                root.destroy()
                import main
        except ValueError:

            messagebox.showerror("Entry Invalid", "Please enter a valid ID Number")




a = LoginAccess(root)
root.mainloop()
