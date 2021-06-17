from tkinter import *

root = Tk()
root.geometry("600x600")
root.title("Welcome To Ithuba Lotto")
root.config(bg="#FFC107")


class WelcomeScreen:

    def __init__(self, master):
        self.lotto_logo = PhotoImage(file="images/loto logo 1.png")
        self.ithuba_logo = PhotoImage(file="images/ithuba.PNG")
        self.welcome_pic = PhotoImage(file="images/welcome pic.PNG")

        self.canvas = Canvas(root, width=270, height=180, highlightthickness="0")
        self.canvas.create_image(0, 0, anchor=NW, image=self.lotto_logo)
        self.canvas.place(x=165, y=10)

        self.canvas = Canvas(root, width=574, height=180, highlightthickness="0")
        self.canvas.create_image(0, 0, anchor=NW, image=self.welcome_pic)
        self.canvas.place(x=10, y=300)

        self.canvas = Canvas(root, width=178, height=55, highlightthickness="0")
        self.canvas.create_image(0, 0, anchor=NW, image=self.ithuba_logo)
        self.canvas.place(x=400, y=520)

        self.rules_btn = Button(root, text="Rules", bg="#EED313", command=self.rules_screen)
        self.rules_btn.place(x=260, y=480)

        self.sign_btn = Button(root, text="Sign in", bg="#EED313", command=self.login_screen)
        self.sign_btn.place(x=160, y=480)

    def rules_screen(self):
        root.destroy()
        import rules

    def login_screen(self):
        root.destroy()
        import login_screen


a = WelcomeScreen(root)
root.mainloop()
