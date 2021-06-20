from tkinter import *
import random
from playsound import playsound
from tkinter import messagebox

root = Tk()
root.geometry("700x700")
root.title("Welcome To Ithuba Lotto")
root.config(bg="#FFC107")


class GameScreen:
    numb_ent1 = StringVar()
    numb_ent2 = StringVar()
    numb_ent3 = StringVar()

    gen_numbs = StringVar()

    same_ans1 = StringVar()
    same_ans2 = StringVar()
    same_ans3 = StringVar()

    first_numbs = []
    second_numbs = []
    third_numbs = []

    gene_numb = []

    same_numb1 = []
    same_numb2 = []
    same_numb3 = []

    def __init__(self, master):
        self.lotto_logo = PhotoImage(file="images/logo small.PNG")
        self.ithuba_logo = PhotoImage(file="images/ithuba small.PNG")

        self.canvas = Canvas(root, width=89, height=60, highlightthickness="0")
        self.canvas.create_image(0, 0, anchor=NW, image=self.lotto_logo,)
        self.canvas.place(x=10, y=10)

        self.canvas = Canvas(root, width=90, height=28, highlightthickness="0")
        self.canvas.create_image(0, 0, anchor=NW, image=self.ithuba_logo,)
        self.canvas.place(x=500, y=565)

        self.number_1 = PhotoImage(file="images/buttons/1.png")
        self.number_2 = PhotoImage(file="images/buttons/2.png")
        self.number_3 = PhotoImage(file="images/buttons/3.png")
        self.number_4 = PhotoImage(file="images/buttons/4.png")
        self.number_5 = PhotoImage(file="images/buttons/5.png")
        self.number_6 = PhotoImage(file="images/buttons/6.png")
        self.number_7 = PhotoImage(file="images/buttons/7.png")
        self.number_8 = PhotoImage(file="images/buttons/8.png")
        self.number_9 = PhotoImage(file="images/buttons/9.png")
        self.number_10 = PhotoImage(file="images/buttons/10.png")
        self.number_11 = PhotoImage(file="images/buttons/11.png")
        self.number_12 = PhotoImage(file="images/buttons/12.png")
        self.number_13 = PhotoImage(file="images/buttons/13.png")
        self.number_14 = PhotoImage(file="images/buttons/14.png")
        self.number_15 = PhotoImage(file="images/buttons/15.png")
        self.number_16 = PhotoImage(file="images/buttons/16.png")
        self.number_17 = PhotoImage(file="images/buttons/17.png")
        self.number_18 = PhotoImage(file="images/buttons/18.png")
        self.number_19 = PhotoImage(file="images/buttons/19.png")
        self.number_20 = PhotoImage(file="images/buttons/20.png")
        self.number_21 = PhotoImage(file="images/buttons/21.png")
        self.number_22 = PhotoImage(file="images/buttons/22.png")
        self.number_23 = PhotoImage(file="images/buttons/23.png")
        self.number_24 = PhotoImage(file="images/buttons/24.png")
        self.number_25 = PhotoImage(file="images/buttons/25.png")
        self.number_26 = PhotoImage(file="images/buttons/26.png")
        self.number_27 = PhotoImage(file="images/buttons/27.png")
        self.number_28 = PhotoImage(file="images/buttons/28.png")
        self.number_29 = PhotoImage(file="images/buttons/29.png")
        self.number_30 = PhotoImage(file="images/buttons/30.png")
        self.number_31 = PhotoImage(file="images/buttons/31.png")
        self.number_32 = PhotoImage(file="images/buttons/32.png")
        self.number_33 = PhotoImage(file="images/buttons/33.png")
        self.number_34 = PhotoImage(file="images/buttons/34.png")
        self.number_35 = PhotoImage(file="images/buttons/35.png")
        self.number_36 = PhotoImage(file="images/buttons/36.png")
        self.number_37 = PhotoImage(file="images/buttons/37.png")
        self.number_38 = PhotoImage(file="images/buttons/38.png")
        self.number_39 = PhotoImage(file="images/buttons/39.png")
        self.number_40 = PhotoImage(file="images/buttons/40.png")
        self.number_41 = PhotoImage(file="images/buttons/41.png")
        self.number_42 = PhotoImage(file="images/buttons/42.png")
        self.number_43 = PhotoImage(file="images/buttons/43.png")
        self.number_44 = PhotoImage(file="images/buttons/44.png")
        self.number_45 = PhotoImage(file="images/buttons/45.png")
        self.number_46 = PhotoImage(file="images/buttons/46.png")
        self.number_47 = PhotoImage(file="images/buttons/47.png")
        self.number_48 = PhotoImage(file="images/buttons/48.png")
        self.number_49 = PhotoImage(file="images/buttons/49.png")

        self.numb_label = Label(image=self.number_1)

        self.btn_1 = Button(root, image=self.number_1, command=lambda: self.choose_number(1), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_1.place(x=130, y=10)
        self.btn_2 = Button(root, image=self.number_2, command=lambda: self.choose_number(2), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_2.place(x=180, y=10)
        self.btn_3 = Button(root, image=self.number_3, command=lambda: self.choose_number(3), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_3.place(x=230, y=10)
        self.btn_4 = Button(root, image=self.number_4, command=lambda: self.choose_number(4), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_4.place(x=280, y=10)
        self.btn_5 = Button(root, image=self.number_5, command=lambda: self.choose_number(5), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_5.place(x=330, y=10)
        self.btn_6 = Button(root, image=self.number_6, command=lambda: self.choose_number(6), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_6.place(x=380, y=10)
        self.btn_7 = Button(root, image=self.number_7, command=lambda: self.choose_number(7), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_7.place(x=430, y=10)
        self.btn_8 = Button(root, image=self.number_8, command=lambda: self.choose_number(8), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_8.place(x=130, y=60)
        self.btn_9 = Button(root, image=self.number_9, command=lambda: self.choose_number(9), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_9.place(x=180, y=60)
        self.btn_10 = Button(root, image=self.number_10, command=lambda: self.choose_number(10), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_10.place(x=230, y=60)
        self.btn_11 = Button(root, image=self.number_11, command=lambda: self.choose_number(11), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_11.place(x=280, y=60)
        self.btn_12 = Button(root, image=self.number_12, command=lambda: self.choose_number(12), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_12.place(x=330, y=60)
        self.btn_13 = Button(root, image=self.number_13, command=lambda: self.choose_number(13), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_13.place(x=380, y=60)
        self.btn_14 = Button(root, image=self.number_14, command=lambda: self.choose_number(14), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_14.place(x=430, y=60)
        self.btn_15 = Button(root, image=self.number_15, command=lambda: self.choose_number(15), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_15.place(x=130, y=110)
        self.btn_16 = Button(root, image=self.number_16, command=lambda: self.choose_number(16), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_16.place(x=180, y=110)
        self.btn_17 = Button(root, image=self.number_17, command=lambda: self.choose_number(17), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_17.place(x=230, y=110)
        self.btn_18 = Button(root, image=self.number_18, command=lambda: self.choose_number(18), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_18.place(x=280, y=110)
        self.btn_19 = Button(root, image=self.number_19, command=lambda: self.choose_number(19), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_19.place(x=330, y=110)
        self.btn_20 = Button(root, image=self.number_20, command=lambda: self.choose_number(20), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_20.place(x=380, y=110)
        self.btn_21 = Button(root, image=self.number_21, command=lambda: self.choose_number(21), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_21.place(x=430, y=110)
        self.btn_22 = Button(root, image=self.number_22, command=lambda: self.choose_number(22), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_22.place(x=130, y=160)
        self.btn_23 = Button(root, image=self.number_23, command=lambda: self.choose_number(23), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_23.place(x=180, y=160)
        self.btn_24 = Button(root, image=self.number_24, command=lambda: self.choose_number(24), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_24.place(x=230, y=160)
        self.btn_25 = Button(root, image=self.number_25, command=lambda: self.choose_number(25), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_25.place(x=280, y=160)
        self.btn_26 = Button(root, image=self.number_26, command=lambda: self.choose_number(26), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_26.place(x=330, y=160)
        self.btn_27 = Button(root, image=self.number_27, command=lambda: self.choose_number(27), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_27.place(x=380, y=160)
        self.btn_28 = Button(root, image=self.number_28, command=lambda: self.choose_number(28), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_28.place(x=430, y=160)
        self.btn_29 = Button(root, image=self.number_29, command=lambda: self.choose_number(29), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_29.place(x=130, y=210)
        self.btn_30 = Button(root, image=self.number_30, command=lambda: self.choose_number(30), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_30.place(x=180, y=210)
        self.btn_31 = Button(root, image=self.number_31, command=lambda: self.choose_number(31), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_31.place(x=230, y=210)
        self.btn_32 = Button(root, image=self.number_32, command=lambda: self.choose_number(32), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_32.place(x=280, y=210)
        self.btn_33 = Button(root, image=self.number_33, command=lambda: self.choose_number(33), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_33.place(x=330, y=210)
        self.btn_34 = Button(root, image=self.number_34, command=lambda: self.choose_number(34), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_34.place(x=380, y=210)
        self.btn_35 = Button(root, image=self.number_35, command=lambda: self.choose_number(35), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_35.place(x=430, y=210)
        self.btn_36 = Button(root, image=self.number_36, command=lambda: self.choose_number(36), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_36.place(x=130, y=260)
        self.btn_37 = Button(root, image=self.number_37, command=lambda: self.choose_number(37), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_37.place(x=180, y=260)
        self.btn_38 = Button(root, image=self.number_38, command=lambda: self.choose_number(38), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_38.place(x=230, y=260)
        self.btn_39 = Button(root, image=self.number_39, command=lambda: self.choose_number(39), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_39.place(x=280, y=260)
        self.btn_40 = Button(root, image=self.number_40, command=lambda: self.choose_number(40), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_40.place(x=330, y=260)
        self.btn_41 = Button(root, image=self.number_41, command=lambda: self.choose_number(41), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_41.place(x=380, y=260)
        self.btn_42 = Button(root, image=self.number_42, command=lambda: self.choose_number(42), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_42.place(x=430, y=260)
        self.btn_43 = Button(root, image=self.number_43, command=lambda: self.choose_number(43), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_43.place(x=130, y=310)
        self.btn_44 = Button(root, image=self.number_44, command=lambda: self.choose_number(44), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_44.place(x=180, y=310)
        self.btn_45 = Button(root, image=self.number_45, command=lambda: self.choose_number(45), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_45.place(x=230, y=310)
        self.btn_46 = Button(root, image=self.number_46, command=lambda: self.choose_number(46), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_46.place(x=280, y=310)
        self.btn_47 = Button(root, image=self.number_47, command=lambda: self.choose_number(47), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_47.place(x=330, y=310)
        self.btn_48 = Button(root, image=self.number_48, command=lambda: self.choose_number(48), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_48.place(x=380, y=310)
        self.btn_49 = Button(root, image=self.number_49, command=lambda: self.choose_number(49), borderwidth=0, highlightthickness=0, highlightbackground="#FFC107", bd=0, bg="#FFC107")
        self.btn_49.place(x=430, y=310)

        self.lotto_frame = LabelFrame(root, padx=10, pady=30, width=500, height=190, bg="#EED313")
        self.lotto_frame.place(x=50, y=370)

        self.ent1_label = Label(self.lotto_frame, text="Your Lucky List 1", width=13, bg="#EED313")
        self.ent1_label.grid(column=1, row=1)
        self.ent2_label = Label(self.lotto_frame, text="Your Lucky List 2", width=13, bg="#EED313")
        self.ent2_label.grid(column=3, row=1)
        self.ent3_label = Label(self.lotto_frame, text="Your Lucky List 3", width=13, bg="#EED313")
        self.ent3_label.grid(column=5, row=1)

        self.ent1 = Label(self.lotto_frame, text="", textvariable=self.numb_ent1, width=13, bg="#FFC107")
        self.ent1.grid(column=1, row=2)
        self.ent2 = Label(self.lotto_frame, text="", textvariable=self.numb_ent2, width=13, bg="#FFC107")
        self.ent2.grid(column=3, row=2)
        self.ent3 = Label(self.lotto_frame, text="", textvariable=self.numb_ent3, width=13, bg="#FFC107")
        self.ent3.grid(column=5, row=2)

        self.generated_lab = Label(self.lotto_frame, textvariable=self.gen_numbs, width=13, bg="#FFC107")
        self.generated_lab.grid(column=3, row=3)

        self.gen_btn = Button(root, text="Generate", command=self.generate)
        self.gen_btn.place(x=300, y=530)

        self.same_lab1 = Label(root, textvariable=self.same_ans1, bg="sky blue").place(x=50, y=470)
        self.same_lab2 = Label(root, textvariable=self.same_ans2, bg="sky blue").place(x=50, y=490)
        self.same_lab3 = Label(root, textvariable=self.same_ans3, bg="sky blue").place(x=50, y=510)

        self.check_btn1 = Button(root, text="check same1", command=self.same_number1)
        self.check_btn1.place(x=350, y=500)
        self.check_btn2 = Button(root, text="check same2", command=self.same_number2)
        self.check_btn2.place(x=370, y=530)
        self.check_btn3 = Button(root, text="check same3", command=self.same_number3)
        self.check_btn3.place(x=390, y=560)

        self.clear_btn1 = Button(self.lotto_frame, text="Clear1", command=self.clear1)
        self.clear_btn1.grid(column=2, row=2)
        self.clear_btn2 = Button(self.lotto_frame, text="Clear2", command=self.clear2)
        self.clear_btn2.grid(column=4, row=2)
        self.clear_btn3 = Button(self.lotto_frame, text="Clear3", command=self.clear3)
        self.clear_btn3.grid(column=6, row=2)
        self.clear_btn = Button(self.lotto_frame, text="Clear All", command=self.clear)
        self.clear_btn.grid(column=6, row=3)

    def choose_number(self, number):
        if len(self.first_numbs) < 6 and number not in self.first_numbs:
            self.first_numbs.append(number)
            self.numb_ent1.set(self.first_numbs)
        elif len(self.first_numbs) == 6 and len(self.second_numbs) < 6 and number not in self.second_numbs:
            self.second_numbs.append(number)
            self.numb_ent2.set(self.second_numbs)
        elif len(self.second_numbs) == 6 and len(self.third_numbs) < 6 and number not in self.third_numbs:
            self.third_numbs.append(number)
            self.numb_ent3.set(self.third_numbs)
        elif len(self.third_numbs) == 6:
            messagebox.showerror("Entries full", "Play Game")
        else:
            messagebox.askretrycancel("Entry Invalid", "You can only choose one number per Entry")

    def generate(self):
        x = 0
        playsound("audio/here they come.mp3")
        while x < 6:
            number = random.randint(1, 49)
            if number not in self.gene_numb:
                self.gene_numb.append(number)
                x = x + 1

        else:
            x = x - 1
        self.gene_numb.sort()
        self.first_numbs.sort()
        self.second_numbs.sort()
        self.third_numbs.sort()
        self.gen_numbs.set(self.gene_numb)

    def same_number1(self):
        self.same_numb1 = set(self.gene_numb).intersection(set(self.first_numbs))
        self.same_ans1.set(self.same_numb1)
        if len(self.same_numb1) == 6:
            print("6")
        elif len(self.same_numb1) == 5:
            print("5")
        elif len(self.same_numb1) == 4:
            print("4")
        elif len(self.same_numb1) == 3:
            print("3")
        elif len(self.same_numb1) == 2:
            print("2")
        elif len(self.same_numb1) == 1:
            print("0")
        elif len(self.same_numb1) == 0:
            print("0")

    def same_number2(self):
        self.same_numb2 = set(self.gene_numb).intersection(set(self.second_numbs))
        self.same_ans2.set(self.same_numb2)
        if len(self.same_numb2) == 6:
            print("6")
        elif len(self.same_numb2) == 5:
            print("5")
        elif len(self.same_numb2) == 4:
            print("4")
        elif len(self.same_numb2) == 3:
            print("3")
        elif len(self.same_numb2) == 2:
            print("2")
        elif len(self.same_numb2) == 1:
            print("0")
        elif len(self.same_numb2) == 0:
            print("0")

    def same_number3(self):
        self.same_numb3 = set(self.gene_numb).intersection(set(self.third_numbs))
        self.same_ans3.set(self.same_numb3)
        if len(self.same_numb3) == 6:
            print("6")
        elif len(self.same_numb3) == 5:
            print("5")
        elif len(self.same_numb3) == 4:
            print("4")
        elif len(self.same_numb3) == 3:
            print("3")
        elif len(self.same_numb3) == 2:
            print("2")
        elif len(self.same_numb3) == 1:
            print("0")
        elif len(self.same_numb3) == 0:
            print("0")

    def clear1(self):
        if len(self.first_numbs) > 0:
            self.numb_ent1.set("")
            self.first_numbs = []

    def clear2(self):
        if len(self.second_numbs) > 0:
            self.numb_ent2.set("")
            self.second_numbs = []

    def clear3(self):
        if len(self.third_numbs) > 0:
            self.numb_ent3.set("")
            self.third_numbs = []

    def clear(self):
        if len(self.first_numbs) > 0:
            self.numb_ent1.set("")
            self.first_numbs = []
        if len(self.second_numbs) > 0:
            self.numb_ent2.set("")
            self.second_numbs = []
        if len(self.third_numbs) > 0:
            self.numb_ent3.set("")
            self.third_numbs = []
        self.gen_numbs.set("")
        self.same_ans1.set("")
        self.same_ans2.set("")
        self.same_ans3.set("")


e = GameScreen(root)
root.mainloop()
