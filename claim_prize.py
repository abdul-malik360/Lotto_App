from tkinter import *
from tkinter import ttk
import requests

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
    banks = ["ABSA", "Nedbank", "Standardbank", "FNB"]
    def __init__(self, master):
        self.lotto_logo = PhotoImage(file="images/nl flag.PNG")
        self.canvas = Canvas(root, width=570, height=180, highlightthickness="0")
        self.canvas.create_image(0, 0, anchor=NW, image=self.lotto_logo)
        self.canvas.place(x=70, y=10)

        with open("Game_Info.txt") as files:
            for line in files:
                file = line
            files.close()
            game = file

        self.currency_frame = LabelFrame(master, padx=50, pady=30, width=378, height=290, bg="#EED313")
        self.currency_frame.place(x=10, y=200)

        self.prize_lab = Label(self.currency_frame, text="Your Prize is R ")
        self.prize_lab.grid(column=1, row=1)

        self.amount = Label(self.currency_frame, textvariable=self.amount_won)
        self.amount.grid(column=2, row=1)
        self.amount_won.set(game)

        self.currency_box = ttk.Combobox(self.currency_frame)
        self.currency_box["values"] = currency
        self.currency_box.set("Choose Currency")
        self.currency_box.grid(column=1, row=2)

        self.converted_label = Label(self.currency_frame, text="Converted Amount is: ")
        self.converted_label.grid(column=1, row=3, padx=10, pady=10)

        self.converted = Label(self.currency_frame, text='', textvariable=converted)
        self.converted.grid(column=2, row=3, padx=10, pady=10)

        self.convert_btn = Button(self.currency_frame, text='Convert', command=self.swap_currencies)
        self.convert_btn.grid(column=2, row=4)

        self.bank_frame = LabelFrame(master, padx=50, pady=30, width=378, height=290, bg="#EED313")
        self.bank_frame.place(x=400, y=200)

        self.bank_name = StringVar(self.bank_frame)
        self.bank_name.set("Choose Your Bank")
        self.bank_options = OptionMenu(self.bank_frame,self.bank_name, *self.banks)
        self.bank_options.config(width=15)
        self.bank_options.grid(column=2, row=1, padx=10, pady=10)

        self.account_lab = Label(self.bank_frame, text="Account holder: ")
        self.account_lab.grid(column=1, row=2)
        self.account_numb_lab = Label(self.bank_frame, text="Account number: ")
        self.account_numb_lab.grid(column=1, row=3)

        self.account_name = Entry(self.bank_frame)
        self.account_name.grid(column=2, row=2, padx=10, pady=10)
        self.account_number = Entry(self.bank_frame)
        self.account_number.grid(column=2, row=3, padx=10, pady=10)
        self.email_ent = Label(self.bank_frame, width=20)
        self.email_ent.grid(column=2, row=4, padx=10, pady=10)
        self.send_btn = Button(self.bank_frame, text="send")
        self.send_btn.grid(column=2, row=5, padx=10, pady=10)

    def convert(self, zar, convert_currency, prize):
        prize = round(prize * currencies[convert_currency], 2)
        return prize

    def swap_currencies(self):
        prize = float(self.amount_won.get())
        from_zar = currencies
        to_converted = self.currency_box.get()

        converted_prize = self.convert(from_zar, to_converted, prize)
        converted.set(converted_prize)


f = CurrencyConverter(root)
root.mainloop()
