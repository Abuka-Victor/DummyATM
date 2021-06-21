from database import *
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

# Window and Login Definition
window = Tk()
window.title("The People's Bank of Nigeria")
window.geometry("1000x667")
window.resizable(False, False)
Login = Toplevel(window)
Login.title("The People's Bank of Nigeria")
Login.geometry("1000x667")
Login.resizable(False, False)

# Adding The Background Image
bgimg = ImageTk.PhotoImage(file="bankappbg.jpg")
label = Label(Login, image=bgimg)
label.pack()


# FUNCTION
# Check is for the submit button, this checks with the database whether the details are correct

def check():
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
            genacc.set(accno)
            accno_entry.delete(0, END)
            accpin_entry.delete(0, END)
    else:
        messagebox.showerror("Error", "ATM NUMBER OR PIN IS INCORRECT")


# To Quit The Program from The  DashBoard
def quit():
    Login.deiconify()
    window.withdraw()


# To check BVN
def bvn():
    global genacc
    window = Toplevel()
    window.geometry("400x300")
    window.title("BVN")
    window.resizable(False, False)
    bvntaglabel = Label(window, text="Your BVN is", font=("Helvetica", 15, "bold"))
    bvntaglabel.place(x='75', y='90')
    connect.execute(f"SELECT BVN FROM {table} WHERE Acc_No ='{genacc.get()}'")
    bvn = connect.fetchone()
    bvnlabel = Label(window, text=bvn, font=("Helvetica", 25, "bold"))
    bvnlabel.place(x='75', y='135')


# To Withdraw
def withdraw():
    global genacc
    window = Toplevel()
    window.geometry("500x500")
    window.title("Withdrawal Window")
    window.resizable(False, False)
    connect.execute(F"SELECT Acc_Bal FROM {table} WHERE Acc_No = '{genacc.get()}'")
    accballist = connect.fetchone()
    accbal = int(accballist[0])
    amountlabel = Label(window, text="Select Withdrawal Amount", font=("Helvetica", 15, "bold"))
    amountlabel.place(x='120', y='100')
    amtentry = Entry(window, font=("Times New Roman", 15))
    amtentry.place(x='120', y='150', width='250')
    amtbutton = Button(window, font=("Times New Roman", 15), text='Submit', bg='black', fg='white',
                       activebackground='white', activeforeground='black', command=lambda: amtbutton())
    amtbutton.place(x='120', y='200', width='250')
    def amtbutton():
        amt = int(amtentry.get())
        if amt > accbal:
            messagebox.showerror("Error", "Insufficient Funds")
        else:
            retbal = (accbal - amt)
            connect.execute(f"UPDATE {table} SET Acc_Bal = '{retbal}' WHERE Acc_No='{genacc.get()}'")
            conn.commit()
            messagebox.showinfo("Success", f"Take Your Cash: {amt}")
            connect.execute(f"INSERT INTO {table2} VALUES({genacc.get()}, 'Withdrawal', {amt})")
            conn.commit()
            connect.execute(f"SELECT Acc_Bal FROM {table} WHERE Acc_No='{genacc.get()}'")
            ballist = connect.fetchone()
            bal = f"Your Account Balance is: {ballist[0]} Naira"
            balance.set(bal)
            window.destroy()


# To Pay Bills
def bills():
    global genacc
    window = Toplevel()
    window.geometry("700x500")
    window.title("Bills")
    window.resizable(False, False)

    servicelabel = Label(window, text="Select Service", font=("Helvetica", 15, "bold"))
    servicelabel.place(x='50', y='50')

    radio1 = IntVar()
    electbutton = Radiobutton(window, text="PHCN", var=radio1, value=1, font=("Helvetica", 15, "bold"))
    electbutton.place(x='100', y='100')
    dstvbutton = Radiobutton(window, text="DSTV", var=radio1, value=2, font=("Helvetica", 15, "bold"))
    dstvbutton.place(x='200', y='100')
    gotvbutton = Radiobutton(window, text="GOTV", var=radio1, value=3, font=("Helvetica", 15, "bold"))
    gotvbutton.place(x='300', y='100')
    waterbutton = Radiobutton(window, text="WATER DISTRIBUTION\nSERVICE", var=radio1, value=4, font=("Helvetica", 15, "bold"))
    waterbutton.place(x='400', y='87')

    quitbutton = Button(window, text="Quit", font=("Helvetica", 15, "bold"), command=lambda: quitair(),
                        activeforeground='white', activebackground='black')
    quitbutton.place(x='200', y='50', height='30', width='100')

    def quitair():
        window.destroy()


# To Deposit Money
def deposit():
    global genacc
    window = Toplevel()
    window.geometry("500x500")
    window.title("Deposit Form")
    window.resizable(False, False)
    connect.execute(F"SELECT Acc_Bal FROM {table} WHERE Acc_No = '{genacc.get()}'")
    accballist = connect.fetchone()
    accbal = int(accballist[0])
    amountlabel = Label(window, text="Enter Deposit Amount", font=("Helvetica", 15, "bold"))
    amountlabel.place(x='120', y='100')

    amtentry = Entry(window, font=("Times New Roman", 15))
    amtentry.place(x='120', y='150', width='250')

    depbutton = Button(window, font=("Times New Roman", 15), text='Submit', bg='black', fg='white',
                       activebackground='white', activeforeground='black', command=lambda: defbutt())
    depbutton.place(x='120', y='200', width='250')

    def defbutt():
        amt = int(amtentry.get())
        retbal = (amt + accbal)
        connect.execute(f"UPDATE {table} SET Acc_Bal = '{retbal}' WHERE Acc_No='{genacc.get()}'")
        conn.commit()
        messagebox.showinfo("Success", f"You have deposited: {amt}")
        connect.execute(f"SELECT Acc_Bal FROM {table} WHERE Acc_No='{genacc.get()}'")
        ballist = connect.fetchone()
        bal = f"Your Account Balance is: {ballist[0]} Naira"
        balance.set(bal)
        window.destroy()


# To transfer money to diff accounts
def transfer():
    global genacc
    window = Toplevel()
    window.geometry("500x500")
    window.title("Transfer Window")
    window.resizable(False, False)

    amountlabel = Label(window, text="Enter Account Number", font=("Helvetica", 15, "bold"))
    amountlabel.place(x='120', y='100')

    actentry = Entry(window, font=("Times New Roman", 15))
    actentry.place(x='120', y='150', width='250')

    amountlabel = Label(window, text="Enter Amount", font=("Helvetica", 15, "bold"))
    amountlabel.place(x='120', y='200')

    amtentry = Entry(window, font=("Times New Roman", 15))
    amtentry.place(x='120', y='250', width='250')

    amtbutton = Button(window, font=("Times New Roman", 15), text='Submit', bg='black', fg='white',
                       activebackground='white', activeforeground='black', command=lambda: transferact())
    amtbutton.place(x='120', y='300', width='250')

    def transferact():
        global genacc
        aza = actentry.get()
        amt = int(amtentry.get())
        connect.execute(f"SELECT Acc_Bal FROM {table} WHERE Acc_No = '{genacc.get()}'")
        sndcurramt = int((connect.fetchone()[0]))
        connect.execute(f"SELECT Acc_Bal FROM {table} WHERE Acc_No = '{aza}'")
        rcpcurramt = int(connect.fetchone()[0])
        rcpnewamt = (rcpcurramt + amt)
        sndnewamt = (sndcurramt - amt)
        if sndcurramt < amt:
            messagebox.showerror("Error", "INSUFFICIENT FUNDS IN YOUR ACCOUNT\nTRANSFER TERMINATED")
        else:
            connect.execute(f"SELECT First_Name FROM {table} WHERE Acc_No = '{aza}'")
            accname = connect.fetchone()[0]
            connect.execute(f"UPDATE {table} SET Acc_Bal = '{rcpnewamt}' WHERE Acc_No='{aza}'")
            connect.execute(f"UPDATE {table} SET Acc_Bal = '{sndnewamt}' WHERE Acc_No='{genacc.get()}'")
            connect.execute(f"SELECT Acc_Bal FROM {table} WHERE Acc_No='{genacc.get()}'")
            ballist = connect.fetchone()
            bal = f"Your Account Balance is: {ballist[0]} Naira"
            balance.set(bal)
            messagebox.showinfo("Success", f"You have Successfully sent {amt} Naira to {accname}\nPeople's Bank, Nigeria")
            window.destroy()


def cngpin():
    global genacc
    window = Toplevel()
    window.geometry("500x500")
    window.title("Change Pin")
    window.resizable(False, False)

    currpinlabel = Label(window, text="Enter Current Pin", font=("Helvetica", 15, "bold"))
    currpinlabel.place(x='120', y='100')

    currpinentry = Entry(window, font=("Times New Roman", 15))
    currpinentry.place(x='120', y='150', width='250')

    newpinlabel = Label(window, text="Enter New Pin", font=("Helvetica", 15, "bold"))
    newpinlabel.place(x='120', y='200')

    newpinentry = Entry(window, font=("Times New Roman", 15))
    newpinentry.place(x='120', y='250', width='250')

    cfmnewpinlabel = Label(window, text="Confirm New Pin", font=("Helvetica", 15, "bold"))
    cfmnewpinlabel.place(x='120', y='300')

    cfmnewpinentry = Entry(window, font=("Times New Roman", 15))
    cfmnewpinentry.place(x='120', y='350', width='250')

    pinbutton = Button(window, font=("Times New Roman", 15), text='Submit', bg='black', fg='white',
                       activebackground='white', activeforeground='black', command=lambda: changepin())
    pinbutton.place(x='120', y='400', width='250')
    def changepin():
        currpin = currpinentry.get()
        newpin = newpinentry.get()
        cfmnewpin = cfmnewpinentry.get()
        connect.execute(f"SELECT Pin FROM {table} WHERE Acc_No = '{genacc.get()}'")
        dbcurrpin = str(connect.fetchone()[0])
        if dbcurrpin != currpin:
            messagebox.showerror("Error", "You Have Entered An Incorrect Pin")
        else:
            if cfmnewpin == newpin:
                connect.execute(f"UPDATE {table} SET Pin = '{int(newpin)}' WHERE Acc_No='{genacc.get()}'")
                messagebox.showinfo("Success", "You Have Successfully Changed Your Pin")
                window.destroy()
            else:
                messagebox.showerror("Error", "The new pins you have entered do not match!")
                window.destroy()


def airtime():
    global genacc
    window = Toplevel()
    window.geometry("600x400")
    window.title("Airtime Window")
    window.resizable(False, False)

    netlabel = Label(window, text="Select Network", font=("Helvetica", 15, "bold"))
    netlabel.place(x='50', y='50')

    radio = IntVar()
    Airtelbutton = Radiobutton(window, text="Airtel", var=radio, value=1, font=("Helvetica", 15, "bold"),
                               command=lambda: cred())
    Airtelbutton.place(x='100', y='100')
    globutton = Radiobutton(window, text="Glo", var=radio, value=2, font=("Helvetica", 15, "bold"), command=lambda: cred())
    globutton.place(x='200', y='100')
    mtnbutton = Radiobutton(window, text="Mtn", var=radio, value=3, font=("Helvetica", 15, "bold"), command=lambda: cred())
    mtnbutton.place(x='300', y='100')
    ninemobilebutton = Radiobutton(window, text="9Mobile", var=radio, value=4, font=("Helvetica", 15, "bold"),
                                   command=lambda: cred())
    ninemobilebutton.place(x='400', y='100')

    quitbutton = Button(window, text="Quit", font=("Helvetica", 15, "bold"), command=lambda: quitair(), activeforeground='white', activebackground='black')
    quitbutton.place(x='200', y='50', height='30', width='100')

    def quitair():
        window.destroy()

    def cred():
        import random
        value = radio.get()
        if value == 1:
            code = random.randint(000000000000, 999999999999)
            result = Label(window, text="Enter This Code:", font=("Helvetica", 15, "bold"))
            result.place(x='50', y='150')

            result1 = Label(window, text=f"{code}", font=("Helvetica", 15, "bold"))
            result1.place(x='250', y='150')
        elif value == 2:
            code = random.randint(000000000000, 999999999999)
            result = Label(window, text="Enter This Code:", font=("Helvetica", 15, "bold"))
            result.place(x='50', y='150')

            result1 = Label(window, text=f"{code}", font=("Helvetica", 15, "bold"))
            result1.place(x='250', y='150')
        elif value == 3:
            code = random.randint(000000000000, 999999999999)
            result = Label(window, text="Enter This Code:", font=("Helvetica", 15, "bold"))
            result.place(x='50', y='150')

            result1 = Label(window, text=f"{code}", font=("Helvetica", 15, "bold"))
            result1.place(x='250', y='150')
        elif value == 4:
            code = random.randint(000000000000, 999999999999)
            result = Label(window, text="Enter This Code:", font=("Helvetica", 15, "bold"))
            result.place(x='50', y='150')

            result1 = Label(window, text=f"{code}", font=("Helvetica", 15, "bold"))
            result1.place(x='250', y='150')


# Header Greeting on Login
grt = Label(Login, text="Welcome To The People's Bank Of Nigeria", font=("Times New Roman", 20, "bold"), bg="#1a1a1a",
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
withdrawalbutt = Button(side1, text="WITHDRAWAL", activebackground="black", activeforeground="white",
                        font=("Helvetica", 15, "bold"), command=lambda: withdraw())
withdrawalbutt.place(x="20", y="180", height="30", width="170")

depositbutt = Button(side1, text="DEPOSIT", activebackground="black", activeforeground="white",
                     font=("Helvetica", 15, "bold"), command=lambda: deposit())
depositbutt.place(x="20", y="280", height="30", width="170")

transferbutt = Button(side1, text="TRANSFER", activebackground="black", activeforeground="white",
                      font=("Helvetica", 15, "bold"), command=lambda: transfer())
transferbutt.place(x="20", y="380", height="30", width="170")

billsbutt = Button(side1, text="PAY BILLS", activebackground="black", activeforeground="white",
                   font=("Helvetica", 15, "bold"), command=lambda: bills())
billsbutt.place(x="20", y="480", height="30", width="170")

# Side 2 Buttons
airtimebutt = Button(side2, text="AIRTIME", activebackground="black", activeforeground="white",
                     font=("Helvetica", 15, "bold"), command=lambda: airtime())
airtimebutt.place(x="20", y="180", height="30", width="170")

checkbvnbutt = Button(side2, text="CHECK BVN", activebackground="black", activeforeground="white",
                      font=("Helvetica", 15, "bold"), command=lambda: bvn())
checkbvnbutt.place(x="20", y="280", height="30", width="170")
genacc = StringVar()

cpinbutt = Button(side2, text="CHANGE PIN", activebackground="black", activeforeground="white",
                     font=("Helvetica", 15, "bold"), command=lambda: cngpin())
cpinbutt.place(x="20", y="380", height="30", width="170")

billsbutt = Button(side2, text="QUIT", activebackground="black", activeforeground="white",
                   font=("Helvetica", 15, "bold"), command=lambda: quit())
billsbutt.place(x="20", y="480", height="30", width="170")

window.withdraw()
# So that the window does not close until we manually close it
window.mainloop()
