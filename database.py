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
