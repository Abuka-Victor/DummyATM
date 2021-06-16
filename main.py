from database import *
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

# Window and Login Definition
window = Tk()
window.title("Central Banque Of Nigeria")
window.geometry("1000x667")
window.resizable(False, False)
Login = Toplevel(window)
Login.title("Central Banque Of Nigeria")
Login.geometry("1000x667")
Login.resizable(False, False)

# Adding The Background Image
bgimg = ImageTk.PhotoImage(file="bankappbg.jpg")
label = Label(Login, image=bgimg)
label.pack()


# FUNCTION
# Check is for the submit button, this checks with the database whether the details are correct

def check():
    global var
    accno = accno_entry.get()
    accpin = accpin_entry.get()
    if len(accno) == 10 and len(accpin) == 4:
        connect.execute(f"SELECT * FROM {table} WHERE Acc_No ='{accno}' and Pin ='{accpin}'")
        row = connect.fetchone()
        if row == None:
            messagebox.showerror("Error", "Incorrect Credientials")
        else:
            messagebox.showinfo("Success", "Login Successful")
            Login.withdraw()
            window.deiconify()
            connect.execute(f"SELECT First_Name FROM {table} WHERE Acc_No='{accno}'")
            namelist = connect.fetchone()
            name = f"Welcome {namelist[0]}"
            var.set(name)
            connect.execute(f"SELECT Acc_Bal FROM {table} WHERE Acc_No='{accno}'")
            ballist = connect.fetchone()
            bal = f"Your Account Balance is: {ballist[0]} Naira"
            balance.set(bal)
            accno_entry.delete(0, END)
            accpin_entry.delete(0, END)
    else:
        messagebox.showerror("Error", "ATM NUMBER OR PIN IS INCORRECT")
# To Quit The Program from The  DashBoard
def quit():
    Login.deiconify()
    window.withdraw()


# Header Greeting on Login
grt = Label(Login, text="Welcome To The Central Banque Of Nigeria", font=("Times New Roman", 20, "bold"), bg="#1a1a1a",
            fg="white")
grt.place(x="0", y="10", width="1000", height="100")

# Frame For Login
body = Frame(Login)
body.place(x=290, y=170, width=400, height=450)

# Fields For Login containing the labels, entries and submit button
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

"STARTING CODE FOR MAIN WINDOW AFTER LOGIN"
# Side Panels
side1 = Frame(window, bg="#391313")
side1.place(x="0", y="0", height="1000", width="200")
side2 = Frame(window, bg="#391313")
side2.place(x="800", y="0", height="1000", width="200")
# History Frame
bottomframe = Frame(window, bg="grey")
bottomframe.place(x="225", y="220", height="450", width="550")
# Greeting Panel
topframe = Frame(window)
topframe.place(x="200", y="40", height="100", width="600")
tfimg = ImageTk.PhotoImage(file="cardbg.jpg")
tflabel = Label(topframe, image=tfimg, width='600', height="100")
tflabel.pack()

# Greeting
var = StringVar()
maingrt = Label(topframe, textvariable=var, font=("Monospace", 15, "bold"))
maingrt.place(x="20", y="20")

# display acc balance
balance = StringVar()
accbal = Label(window, textvariable=balance, font=("monospace", 15, "bold"))
accbal.place(x="200", y="180")

# Side 1 Buttons
airtimebutt = Button(side1, text="WITHDRAWAL", activebackground="black", activeforeground="white",
                     font=("Helvetica", 15, "bold"))
airtimebutt.place(x="20", y="180", height="30", width="170")

depositbutt = Button(side1, text="DEPOSIT", activebackground="black", activeforeground="white",
                 font=("Helvetica", 15, "bold"))
depositbutt.place(x="20", y="280", height="30", width="170")

transferbutt = Button(side1, text="TRANSFER", activebackground="black", activeforeground="white",
                     font=("Helvetica", 15, "bold"))
transferbutt.place(x="20", y="380", height="30", width="170")

billsbutt = Button(side1, text="PAY BILLS", activebackground="black", activeforeground="white",
                   font=("Helvetica", 15, "bold"))
billsbutt.place(x="20", y="480", height="30", width="170")

# Side 2 Buttons
airtimebutt = Button(side2, text="AIRTIME", activebackground="black", activeforeground="white",
                     font=("Helvetica", 15, "bold"))
airtimebutt.place(x="20", y="180", height="30", width="170")

checkbvnbutt = Button(side2, text="CHECK BVN", activebackground="black", activeforeground="white",
                 font=("Helvetica", 15, "bold"))
checkbvnbutt.place(x="20", y="280", height="30", width="170")

airtimebutt = Button(side2, text="AIRTIME", activebackground="black", activeforeground="white",
                     font=("Helvetica", 15, "bold"))
airtimebutt.place(x="20", y="380", height="30", width="170")

billsbutt = Button(side2, text="QUIT", activebackground="black", activeforeground="white",
                   font=("Helvetica", 15, "bold"), command=lambda: quit())
billsbutt.place(x="20", y="480", height="30", width="170")

window.withdraw()
# So that the window does not close until we manually close it
window.mainloop()
