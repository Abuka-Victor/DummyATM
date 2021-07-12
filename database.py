import MySQLdb
table = 'atm'
table2 = 'history'
conn = MySQLdb.connect(
    host='localhost',
    user='root',
    password='',
    database='dummyatm'
)

connect = conn.cursor()

# import pyodbc
# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=VICTOR-PC;'
#                       'Database=DummyATM;'
#                       'Trusted_Connection=yes;')
#
# cursor = conn.cursor()
