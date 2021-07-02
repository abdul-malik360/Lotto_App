from tkinter import *
from playsound import playsound
import pyttsx3
import os


root = Tk()
root.geometry("700x700")
root.title("Rules and Prizes")
root.config(bg="#FFC107")


class RulesScreen:
    def __init__(self, master):
        self.lotto_logo = PhotoImage(file="images/loto logo 1.png")
        self.ithuba_logo = PhotoImage(file="images/ithuba.PNG")

        self.canvas = Canvas(master, width=270, height=180, highlightthickness="0")
        self.canvas.create_image(0, 0, anchor=NW, image=self.lotto_logo)
        self.canvas.place(x=220, y=10)

        self.canvas = Canvas(master, width=178, height=55, highlightthickness="0")
        self.canvas.create_image(0, 0, anchor=NW, image=self.ithuba_logo)
        self.canvas.place(x=500, y=620)

        self.rules_frame = LabelFrame(master, text="The Rules of the Game", width=378, height=290, bg="#EED313")
        self.rules_frame.place(x=100, y=250)

        self.rules_txt = Label(self.rules_frame,
                          text="Enter your Name, Email Address and ID Number""\n""Only valid inputs allows you to play" "\n""\n" "Age required to play game is 18 and older" "\n""\n" "You select a set of six numbers and run the game" "\n""\n" "You're allowed to generate 3 sets " "\n""\n" "Your selected set is compared to the game's lucky draw" "\n""\n" "Stand a chance to win R10 000 000" "\n""\n" "If you meet the age requirement, click register""\n""If not, click Exit",
                          bg="#EED313")
        self.rules_txt.grid(column=2, row=1)

        self.sign_in = Button(self.rules_frame, text="Register", bg="#EED313", command=self.login_screen, cursor="hand2", borderwidth=2, highlightthickness=1, highlightbackground="#FFC107")
        self.sign_in.grid(column=2, row=2, padx=10, pady=10)

        self.exit_game = Button(self.rules_frame, text="EXIT", bg="#EED313", command=self.exit, cursor="hand2", borderwidth=2, highlightthickness=1, highlightbackground="#FFC107")
        self.exit_game.grid(column=3, row=2, padx=10, pady=10)

        self.speaker = PhotoImage(file="images/speaker.PNG")
        self.speaker_btn = Button(self.rules_frame, image=self.speaker, command=self.rules, cursor="hand2", borderwidth=2, highlightthickness=1, highlightbackground="#FFC107", bg="#EED313")
        self.speaker_btn.grid(column=1, row=2, padx=10, pady=10)

    def login_screen(self):
        playsound("audio/i hope you're ready.mp3")
        root.destroy()
        import login_screen

    def exit(self):
        root.destroy()

    def rules(self):
        # self.engine = pyttsx3.init()
        # self.engine.setProperty("rate", 150)
        # self.engine.say(
        #     "Enter your Name, Email Address and ID Number. Only valid inputs allow you to play. Age required to play game is 18 and older. You select a set of six numbers and run the game. You're allowed to generate 3 sets. Your selected set is compared to the game's lucky draw. Stand a chance to win ten million rand. If you meet the age requirement, click register. If not, click Exit.")
        # self.engine.runAndWait()

        text = "Enter your Name, Email Address and ID Number. Only valid inputs allow you to play. Age required to play game is 18 and older. You select a set of six numbers and run the game. You're allowed to generate 3 sets. Your selected set is compared to the game's lucky draw. Stand a chance to win ten million rand. If you meet the age requirement, click register. If not, click Exit."
        os.system('espeak "{}"'.format(text))


b = RulesScreen(root)
root.mainloop()
