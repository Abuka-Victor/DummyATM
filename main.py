import database
from tkinter import *
from PIL import ImageTk

# Window Definition
window = Tk()
window.title("Central Banque Of Nigeria")
window.geometry("1000x667")
window.resizable(False,False)


# Adding The Background Image
bgimg = ImageTk.PhotoImage(file="bankappbg.jpg")
label = Label(window, image=bgimg)
label.pack()


# functions
def check():
    accno = accno_entry.get()
    accpin = accpin_entry.get()


#Frame For Login
body = Frame(window)
body.place(x=290, y=170, width=400, height=450)

#Fields For Login containing the labels, entries and submit button
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



#So that the window does not close until we manually close it
window.mainloop()