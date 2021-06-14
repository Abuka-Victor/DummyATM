import database
from tkinter import *

window = Tk()
window.title("Central Banque Of Nigeria")
window.geometry("1200x700")


body = Frame(window)
body.place(x=390, y=170, width=400, height=450)

accno_label = Label(body, text='Account Number', font=("Andalusia", 15, 'bold'))
accno_label.place(x='80', y='50')

accno_entry = Entry(body, font=("Times New Roman", 15))
accno_entry.place(x="80", y="80", width='190')

accpin_label = Label(body, text='PIN', font=("Andalusia", 15, 'bold'))
accpin_label.place(x='290', y='50')

accpin_entry = Entry(body, font=("Times New Roman", 15))
accpin_entry.place(x="290", y="80", width='190')




window.mainloop()