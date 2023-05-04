import mysql.connector


dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123'
)

cursorobject = dataBase.cursor()
cursorobject.execute('CREATE DATABASE starco1')
print('ALL DONE')