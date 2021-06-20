from tkinter import *
from playsound import playsound

root = Tk()
root.geometry("600x600")
root.title("Welcome To Ithuba Lotto")
root.config(bg="#FFC107")


class WelcomeScreen:

    def __init__(self, master):
        self.lotto_logo = PhotoImage(file="images/loto logo 1.png")
        self.ithuba_logo = PhotoImage(file="images/ithuba.PNG")
        self.play_pic = PhotoImage(file="images/play to win.png")
        # self.home_pic = PhotoImage(file="images/home background.png")
        self.ten_mill = PhotoImage(file="images/10 million.png")

        self.canvas = Canvas(root, width=270, height=180, highlightthickness="0")
        self.canvas.create_image(0, 0, anchor=NW, image=self.lotto_logo)
        self.canvas.place(x=165, y=10)

        # self.canvas = Canvas(root, width=224, height=192, highlightthickness="0")
        # self.canvas.create_image(0, 0, anchor=NW, image=self.home_pic)
        # self.canvas.place(x=350, y=165)

        self.canvas = Canvas(root, width=224, height=189, highlightthickness="0")
        self.canvas.create_image(0, 0, anchor=NW, image=self.play_pic)
        self.canvas.place(x=20, y=225)

        self.canvas = Canvas(root, width=184, height=194, highlightthickness="0")
        self.canvas.create_image(0, 0, anchor=NW, image=self.ten_mill)
        self.canvas.place(x=300, y=200)

        self.canvas = Canvas(root, width=178, height=55, highlightthickness="0")
        self.canvas.create_image(0, 0, anchor=NW, image=self.ithuba_logo)
        self.canvas.place(x=400, y=520)

        self.rules_btn = Button(root, text="Rules", bg="#EED313", command=self.rules_screen, borderwidth="5", cursor="hand2", font=2, foreground="black")
        self.rules_btn.place(x=260, y=480)

        self.sign_btn = Button(root, text="Sign in", bg="#EED313", command=self.login_screen, borderwidth="5", cursor="hand2", font=2, foreground="black")
        self.sign_btn.place(x=160, y=480)

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
