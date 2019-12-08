import sqlite3
from sqlite3 import Error

CREATE_TABLE_SQL_COMMAND = "CREATE TABLE IF NOT EXISTS todo(" \
                           "todo_id INTEGER PRIMARY KEY AUTOINCREMENT, " \
                           "todo_title TEXT NOT NULL, " \
                           "todo_date TEXT)"

INSERT_DATA_SQL_COMMAND = "INSERT INTO todo (todo_title, todo_date) VALUES (?, ?)"

DELETE_DATA_SQL_COMMAND = "DELETE  FROM todo WHERE todo_id = ?"


def connect_db(db_path):
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except Error as e:
        print(e)


def create_table(conn):
    try:
        c = conn.cursor()
        c.execute(CREATE_TABLE_SQL_COMMAND)
    except Error as e:
        print(e)


def insert_data(conn, args):
    try:
        c = conn.cursor()
        c.execute(INSERT_DATA_SQL_COMMAND, args)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def delete_data(conn, args):
    try:
        c = conn.cursor()
        c.execute(DELETE_DATA_SQL_COMMAND, args)
        conn.commit()
    except Error as e:
        print(e)
