# DummyATM
A dummy ATM software with python.
Created By NIIT student team:
- Abuka Victor (abukavictoro@gmail.com)
- Ayoyemi Hamzat (ayoyemihamzat4@gmail.com)
- Udoakpan
- Emmanuel

# Program Algorithm
N.B This is a dummy ATM software so the Account Number input serves as the Card input.
1. Insert The Card(Your Account Number) 
2. Check if the account exists.
3. If the account does not exist:
   1. Prompt the user to Create an account:
        1. If the user accepts, Collect user bio
        2. If the user rejects, Print Thank you message.
4. If the account does exist, Ask the user what services the user wants to use:
    1. Withdraw
    2. Deposit
    3. Transfer
    4. Bill Payment
    5. Airtime
    6. Check Account Balance
    7. Check BVN and Account Number
5. Perform the service
6. Update the Database
7. Ask if the user wants to perform another function:
    1. If the user wants to perform another function, display the list of services again
    2. If not print a thank you message and prompt the user to take card(Print User Name)
