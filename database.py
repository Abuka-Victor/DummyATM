import MySQLdb
table = "atm"
conn = MySQLdb.connect(
    host='localhost',
    user='root',
    password='',
    database='dummyatm'
)

connect = conn.cursor()
