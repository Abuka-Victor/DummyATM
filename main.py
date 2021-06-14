from database import *
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

# Window Definition
window = Tk()
window.title("Central Banque Of Nigeria")
window.geometry("1000x667")
window.resizable(False,False)


# Adding The Background Image
bgimg = ImageTk.PhotoImage(file="bankappbg.jpg")
label = Label(window, image=bgimg)
label.pack()


# FUNCTION
# Check is for the submit button, this checks with the database whether the details are correct
def check():
    accno = accno_entry.get()
    accpin = accpin_entry.get()
    connect.execute(f"SELECT * FROM {table} WHERE Acc_No ='{accno}' and Pin ='{accpin}'")
    row = connect.fetchone()
    if row==None:
        messagebox.showerror("Error", "User Not Found")
    else:
        messagebox.showinfo("Success", "Login Successful")




#Frame For Login
body = Frame(window)
body.place(x=290, y=170, width=400, height=450)

#Fields For Login containing the labels, entries and submit button
accno_label = Label(body, text='Account Number', font=("Andalusia", 15, 'bold'), fg='gray', bg='white')
accno_label.place(x='80', y='50')

accno_entry = Entry(body, font=("Times New Roman", 15))
accno_entry.place(x="80", y="100", width='250')

accpin_label = Label(body, text='PIN', font=("Andalusia", 15, 'bold'), fg='grey', bg='white')
accpin_label.place(x='80', y='150')

accpin_entry = Entry(body, show="*", font=("Times New Roman", 15))
accpin_entry.place(x="80", y="200", width='250')

submit_button = Button(body, text="Submit", activebackground="#00B8F8", activeforeground="white", fg='gray',
                       bg="#FBFBFF", font=("Arial", 15, "bold"), command=lambda: check())
submit_button.place(x="80", y="250", width="250")



#So that the window does not close until we manually close it
window.mainloop()