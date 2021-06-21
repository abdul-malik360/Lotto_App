from tkinter import *
import requests

root = Tk()
root.geometry("700x700")
root.title("Claim Your Prize")
root.config(bg="#FFC107")

converted = StringVar()
currency = []

response = requests.get("https://v6.exchangerate-api.com/v6/5ad18b7d2e7ba4449612b2a8/latest/ZAR")
result = response.json()

currencies = result["conversion_rates"]

for i in currencies.keys():
    currency.append(i)

class ConvertCurrency:
    def __init__(self, master):




root.mainloop()
