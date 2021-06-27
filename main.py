from tkinter import *
from playsound import playsound

root = Tk()
root.geometry("700x700")
root.title("Welcome To Ithuba Lotto")
root.config(bg="#FFC107")


class WelcomeScreen:

    def __init__(self, master):
        self.lotto_logo = PhotoImage(file="images/loto logo 1.png")
        self.ithuba_logo = PhotoImage(file="images/ithuba.PNG")
        self.play_pic = PhotoImage(file="images/play and win.png")
        self.ten_mill = PhotoImage(file="images/10 mill.png")

        self.main_frame = LabelFrame(root, width=378, height=290, bg="#EED313")
        self.main_frame.place(x=120, y=250)

        self.canvas = Canvas(root, width=270, height=180, highlightthickness="0")
        self.canvas.create_image(0, 0, anchor=NW, image=self.lotto_logo)
        self.canvas.place(x=220, y=10)

        self.canvas = Canvas(self.main_frame, width=224, height=170, highlightthickness="0")
        self.canvas.create_image(0, 0, anchor=NW, image=self.play_pic)
        self.canvas.grid(column=1, row=1, padx=10, pady=10)

        self.canvas = Canvas(self.main_frame, width=184, height=194, highlightthickness="0")
        self.canvas.create_image(0, 0, anchor=NW, image=self.ten_mill)
        self.canvas.grid(column=2, row=1, padx=10, pady=10)

        self.canvas = Canvas(root, width=178, height=55, highlightthickness="0")
        self.canvas.create_image(0, 0, anchor=NW, image=self.ithuba_logo)
        self.canvas.place(x=500, y=620)

        self.rules_btn = Button(self.main_frame, text="Rules", bg="#EED313", command=self.rules_screen, borderwidth="5", cursor="hand2", font=2, foreground="black")
        self.rules_btn.grid(column=1, row=2, padx=10, pady=10)

        self.sign_btn = Button(self.main_frame, text="Register", bg="#EED313", command=self.login_screen, borderwidth="5", cursor="hand2", font=2, foreground="black")
        self.sign_btn.grid(column=2, row=2, padx=10, pady=10)

    def rules_screen(self):
        playsound("audio/click rules.mp3")
        root.destroy()
        import rules

    def login_screen(self):
        playsound("audio/welcome.mp3")
        root.destroy()
        import login_screen


a = WelcomeScreen(root)
root.mainloop()
