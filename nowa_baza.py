import sqlite3
from sqlite3 import Error

def connection():
    try:
        connect = sqlite3.connect('base.db')
        return connect

    except Error:
        print(Error)


def table(connect):
    cursorObj = connect.cursor()
    cursorObj.execute(
        "CREATE TABLE IF NOT Exists users(id integer PRIMARY KEY AUTOINCREMENT, name varchar(20) not null"
        ", password varchar(20) not null)")
    connect.commit()

def insert(connect):
    cursorObj = connect.cursor()
    cursorObj.execute("INSERT INTO users(name, password) VALUES (?,?)")
    connect.commit()


connect = connection()
table(connect)