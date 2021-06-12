import MySQLdb
conn = MySQLdb.connect(
    host='localhost',
    user='root',
    password='',
    database='dummyatm'
)

connect = conn.cursor()
