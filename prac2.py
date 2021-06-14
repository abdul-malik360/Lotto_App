from tkinter import *
from datetime import date, timedelta
import rsaidnumber

root = Tk()
root.geometry("600x500")
root.title("Login Screen")

id_no = StringVar()
id_res = StringVar()


id_ent = Entry(root, textvariable=id_no)
id_ent.place(x=50, y=50)

id_ans = Entry(root, textvariable=id_res)
id_ans.place(x=50, y=100)


def dob():
    id_number = rsaidnumber.parse(id_ent.get())
    age = (date.today() - id_number.date_of_birth) // timedelta(days=365.245)
    id_res.set(age)


cal_btn = Button(root, command=dob)
cal_btn.place(x=50, y=200)

root.mainloop()