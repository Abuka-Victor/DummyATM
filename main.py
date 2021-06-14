import database
from tkinter import *
from PIL import ImageTk

window = Tk()
window.title("Central Banque Of Nigeria")
window.geometry("1000x667")
window.resizable(False,False)

bgimg = ImageTk.PhotoImage(file="bankappbg.jpg")
label = Label(window, image=bgimg)
label.pack()

body = Frame(window)
body.place(x=290, y=170, width=400, height=450)

accno_label = Label(body, text='Account Number', font=("Andalusia", 15, 'bold'))
accno_label.place(x='100', y='120')

accno_entry = Entry(body, font=("Times New Roman", 15))
accno_entry.place(x="100", y="150", width='190')

accpin_label = Label(body, text='PIN', font=("Andalusia", 15, 'bold'))
accpin_label.place(x='100', y='200')

accpin_entry = Entry(body, show="*", font=("Times New Roman", 15))
accpin_entry.place(x="100", y="230", width='190')

submit_button = Button(body, text="Submit")
submit_button.place(x="165", y="280")




window.mainloop()