import sqlite3

connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Movies 
    (Title TEXT, Director TEXT, YEAR INT)''')

connection.commit()
connection.close
