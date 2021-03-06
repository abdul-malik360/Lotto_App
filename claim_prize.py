from tkinter import *
from tkinter import ttk
import requests
from tkinter import messagebox
import os
import smtplib
from email.message import EmailMessage
from playsound import playsound


root = Tk()
root.geometry("700x700")
root.title("Claim Your Prize")
root.config(bg="#FDDA0F")

converted = StringVar()

response = requests.get("https://v6.exchangerate-api.com/v6/5ad18b7d2e7ba4449612b2a8/latest/ZAR")
result = response.json()

currencies = result["conversion_rates"]

currency = []
for i in currencies.keys():
    currency.append(i)


class CurrencyConverter:
    amount_won = StringVar()
    account_holder = StringVar()
    account_number = StringVar()
    player_email = StringVar()
    banks = ["ABSA", "Nedbank", "Standardbank", "FNB"]
    def __init__(self, master):
        self.lotto_logo = PhotoImage(file="images/nl flag.PNG")
        self.canvas = Canvas(root, width=570, height=180, highlightthickness="0")
        self.canvas.create_image(0, 0, anchor=NW, image=self.lotto_logo)
        self.canvas.place(x=70, y=10)

        with open("Game_Info.txt") as file:
            for line in file:
                winnings = line.split()
                prizes = winnings
            prize = prizes[3]

        f = open("Game_Info.txt")
        for x, lines in enumerate(f):
            if x == 1:
                email_line = lines.split()
                email_add = email_line[3]

        self.convert_pic = PhotoImage(file="images/Capture.PNG")
        self.canvas = Canvas(root, width=113, height=83, highlightthickness="0")
        self.canvas.create_image(0, 0, anchor=NW, image=self.convert_pic)
        self.canvas.place(x=30, y=250)

        self.currency_frame = LabelFrame(master, padx=50, pady=30, width=378, height=290, bg="#EED313")
        self.currency_frame.place(x=170, y=190)

        self.prize_lab = Label(self.currency_frame, text="Your Prize in rands (R)", bg="#EED313")
        self.prize_lab.grid(column=1, row=1)

        self.amount = Label(self.currency_frame, textvariable=self.amount_won, bg="#EED313")
        self.amount.grid(column=2, row=1)
        self.amount_won.set(prize)

        self.currency_box = ttk.Combobox(self.currency_frame)
        self.currency_box["values"] = currency
        self.currency_box.set("Choose Currency")
        self.currency_box.grid(column=1, row=2, padx=10, pady=10)

        self.converted_label = Label(self.currency_frame, text="Converted Amount is: ", bg="#EED313")
        self.converted_label.grid(column=1, row=3, padx=10, pady=10)

        self.converted_ans = Label(self.currency_frame, text='', textvariable=converted, bg="#EED313")
        self.converted_ans.grid(column=2, row=3, padx=10, pady=10)

        self.convert_btn = Button(self.currency_frame, text='Convert', command=self.swap_currencies, bg="#FDDA0F")
        self.convert_btn.grid(column=2, row=4)

        self.bank_frame = LabelFrame(master, padx=50, pady=30, width=378, height=290, bg="#EED313")
        self.bank_frame.place(x=100, y=400)

        self.bank_box = ttk.Combobox(self.bank_frame)
        self.bank_box["values"] = self.banks
        self.bank_box.set("Choose Your Bank")
        self.bank_box.grid(column=2, row=1, padx=10, pady=10)

        self.account_lab = Label(self.bank_frame, text="Account Holder: ", bg="#EED313")
        self.account_lab.grid(column=1, row=2)
        self.account_numb_lab = Label(self.bank_frame, text="Account Number: ", bg="#EED313")
        self.account_numb_lab.grid(column=1, row=3)
        self.account_numb_lab = Label(self.bank_frame, text="Your Email Address: ", bg="#EED313")
        self.account_numb_lab.grid(column=1, row=4)

        self.account_ent = Entry(self.bank_frame, textvariable=self.account_holder)
        self.account_ent.grid(column=2, row=2, padx=10, pady=10)
        self.account_number_ent = Entry(self.bank_frame, textvariable=self.account_number)
        self.account_number_ent.grid(column=2, row=3, padx=10, pady=10)
        self.email_ent = Label(self.bank_frame, width=30, bg="#EED313", textvariable=self.player_email)
        self.email_ent.grid(column=2, row=4, padx=10, pady=10)
        self.player_email.set(email_add)

        self.send_btn = Button(self.bank_frame, text="Claim Prize", bg="#FDDA0F", command=self.send_details)
        self.send_btn.grid(column=2, row=5, padx=10, pady=10)

    def convert(self, zar, convert_currency, prize):
        try:
            prize = round(prize * currencies[convert_currency], 2)
            return prize
        except KeyError:
            messagebox.showerror("No Entry", "Please choose a currency")

    def swap_currencies(self):
        playsound("audio/ching.mp3")
        prize = float(self.amount_won.get())
        from_zar = currencies
        to_converted = self.currency_box.get()

        converted_prize = self.convert(from_zar, to_converted, prize)
        converted.set(converted_prize)
        with open("Game_Info.txt", "a+") as written:
            written.write("Chosen Currency: " + self.currency_box.get())
            written.write("\n")
            written.write("Amount in new Currency: " + str(converted_prize))
            written.write("\n")

    def send_details(self):
        try:
            messagebox.showinfo("Check Your Email","An Email will be sent to you shortly")
            with open("Game_Info.txt", "a+") as written:
                written.write("Your Bank: " + self.bank_box.get())
                written.write("\n")
                written.write("Account Holder: " + self.account_holder.get())
                written.write("\n")
                written.write("Account Number: " + self.account_number_ent.get())
                written.write("\n")
            playsound("audio/money.mp3")
            # email_address = os.environ.get("email_add")
            # email_password = os.environ.get("email_pass")
            email_address = "abdulmalikmohamed360@gmail.com"
            email_password = "****"

            msg = EmailMessage()
            msg["Subject"] = "Results of Your Lotto Draw"
            msg["From"] = email_address
            msg["To"] = self.player_email.get()
            msg.set_content("Your Results attached...")

            files = ["Game_Info.txt"]
            for file in files:
                with open(file, "rb") as gif:
                    file_data = gif.read()
                    file_name = gif.name
                msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(email_address, email_password)

                smtp.send_message(msg)
            root.destroy()
            import main
        except KeyError:
            messagebox.showerror("No Entry", "Please choose a bank")
        except ValueError:
            if self.account_number_ent.get() != int:
                return messagebox.showerror("Entry Invalid", "Please Enter Numbers Only")


f = CurrencyConverter(root)
root.mainloop()
