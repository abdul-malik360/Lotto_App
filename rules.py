from tkinter import *

root = Tk()
root.geometry("600x600")
root.title("Rules and Prizes")
root.config(bg="#FFC107")


class RulesScreen:
    def __init__(self, master):
        self.lotto_logo = PhotoImage(file="images/loto logo 1.png")
        self.ithuba_logo = PhotoImage(file="images/ithuba.PNG")
        self.lotto_balls = PhotoImage(file="images/lotto balls.PNG")
        # place image
        self.canvas = Canvas(root, width=154, height=148, highlightthickness="0")
        self.canvas.create_image(0, 0, anchor=NW, image=self.lotto_balls)
        self.canvas.place(x=10, y=200)

        self.canvas = Canvas(root, width=270, height=180, highlightthickness="0")
        self.canvas.create_image(0, 0, anchor=NW, image=self.lotto_logo, )
        self.canvas.place(x=165, y=10)

        self.canvas = Canvas(root, width=178, height=55, highlightthickness="0")
        self.canvas.create_image(0, 0, anchor=NW, image=self.ithuba_logo, )
        self.canvas.place(x=400, y=520)

        self.rules_frame = LabelFrame(root, text="The Rules of the Game", width=378, height=290, bg="#EED313")
        self.rules_frame.place(x=200, y=200)

        self.rules_txt = Label(self.rules_frame,
                          text="Enter your Name, Email Address and ID Number""\n" "\n""Only valid inputs allows you to play" "\n""\n" "Age required to play game is 18 and older" "\n""\n" "You select a set of six numbers and run the game" "\n""\n" "You're allowed to generate 3 sets " "\n""\n" "Your selected set is compared to the game's selected numbers" "\n""\n" "Stand a chance to win R10 000 000" "\n""\n" "If you meet the age requirement, click sign in""\n""If not, click Mini Game",
                          bg="#EED313")
        self.rules_txt.place(x=10, y=10)

        self.sign_in = Button(root, text="Sign in", bg="#EED313", command=self.login_screen)
        self.sign_in.place(x=200, y=500)

    def login_screen(self):
        root.destroy()
        import login_screen


b = RulesScreen(root)
root.mainloop()
