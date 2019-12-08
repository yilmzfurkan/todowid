import sqlite3
from sqlite3 import Error

__author__ = "Orhan Tugrul && Furkan Yılmaz"
__version__ = "1.0.0"


class SqliteHelper:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)

    def create_table(self):
        cursor = None
        create_table_query = "CREATE TABLE IF NOT EXISTS todo(" \
                             "todo_id INTEGER PRIMARY KEY NOT NULL , " \
                             "todo_title TEXT NOT NULL, " \
                             "todo_date TEXT)"
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_query)
        except Error as e:
            print(e)

    def insert_data(self, args):
        cursor = None
        insert_data_query = "INSERT INTO todo (todo_title, todo_date) VALUES (?, ?)"
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_data_query, args)
            self.connection.commit()
        except Error as e:
            print(e)
        finally:
            try:
                if cursor:
                    cursor.close()

                if self.connection:
                    self.connection.close()
            except Error as e:
                print(e)

    def delete_data(self, args):
        delete_data_query = "DELETE  FROM todo WHERE todo_id = ?"
        try:
            cursor = self.connection.cursor()
            cursor.execute(delete_data_query, args)
            self.connection.commit()
        except Error as e:
            print(e)
