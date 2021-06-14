from database import *
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

# Window and Login Definition
window = Tk()
window.title("Central Banque Of Nigeria")
window.geometry("1000x667")
window.resizable(False,False)
global Login
Login = Toplevel()
Login.title("Central Banque Of Nigeria")
Login.geometry("1000x667")
Login.resizable(False,False)


# Adding The Background Image
bgimg = ImageTk.PhotoImage(file="bankappbg.jpg")
label = Label(Login, image=bgimg)
label.pack()


# FUNCTION
# Check is for the submit button, this checks with the database whether the details are correct
global var
var = ""
def check():
    global var
    accno = accno_entry.get()
    accpin = accpin_entry.get()
    connect.execute(f"SELECT * FROM {table} WHERE Acc_No ='{accno}' and Pin ='{accpin}'")
    row = connect.fetchone()
    var = connect.execute(f"SELECT First_Name FROM {table} WHERE Acc_No ='{accno}'")
    connect.fetchall()
    for x in connect:
        print(x[0])
    if row==None:
        messagebox.showerror("Error", "User Not Found")
    else:
        messagebox.showinfo("Success", "Login Successful")
        Login.withdraw()
        window.deiconify()

#Header Greeting on Login
grt = Label(Login, text="Welcome To The Central Banque Of Nigeria", font=("Times New Roman", 20, "bold"), bg="#1a1a1a", fg="white")
grt.place(x="0", y="10", width="1000", height="100")


#Frame For Login
body = Frame(Login)
body.place(x=290, y=170, width=400, height=450)

#Fields For Login containing the labels, entries and submit button
accno_label = Label(body, text='Account Number', font=("Andalusia", 15, 'bold'), fg='gray', bg='white')
accno_label.place(x='80', y='50')

global accno_entry
accno_entry = Entry(body, font=("Times New Roman", 15))
accno_entry.place(x="80", y="100", width='250')

accpin_label = Label(body, text='PIN', font=("Andalusia", 15, 'bold'), fg='grey', bg='white')
accpin_label.place(x='80', y='150')

accpin_entry = Entry(body, show="*", font=("Times New Roman", 15))
accpin_entry.place(x="80", y="200", width='250')

submit_button = Button(body, text="Submit", activebackground="#00B8F8", activeforeground="white", fg='gray',
                       bg="#FBFBFF", font=("Arial", 15, "bold"), command=lambda: check())
submit_button.place(x="80", y="250", width="250")

"STARTING CODE FOR MAIN WINDOW AFTER LOGIN"
#Side Panels
side1 = Frame(window, bg="#1a1a1a")
side1.place(x="0", y="0", height="1000", width="200")
side2 = Frame(window, bg="#1a1a1a")
side2.place(x="800", y="0", height="1000", width="200")
#Greeting Panel
topframe = Frame(window)
topframe.place(x="200", y="40", height="100", width="600")
tfimg = ImageTk.PhotoImage(file="cardbg.jpg")
tflabel = Label(topframe, image=tfimg)
tflabel.pack()

#Greeting
# name = connect.execute(f"SELECT First_Name FROM {table} WHERE Acc_No = '{accno_entry.get()}'")
# connect.fetchone()
# for i in connect:
#     print("tetet",i)
# print(accno_entry.get())
maingrt = Label(topframe, text=f"Welcome {var}", font=("Monospace", 15, "bold"))
maingrt.place(x="20", y="20")


window.withdraw()
#So that the window does not close until we manually close it
window.mainloop()