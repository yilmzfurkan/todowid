import sqlite3
from sqlite3 import Error
from error.CustomExceptions import TodoNotFoundException

__author__ = "Orhan Tugrul && Furkan Yılmaz"
__since__ = "0.1.0"


class SqliteHelper:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)

    def create_table(self):
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
        insert_data_query = "INSERT INTO todo (todo_title, todo_date) VALUES (?, ?)"
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_data_query, args)
            self.connection.commit()
            cursor.close()
        except Error as e:
            print(e)
        finally:
            try:
                if self.connection:
                    self.connection.close()
            except Error as e:
                print(e)

    def delete_data(self, args):
        delete_data_query = "DELETE FROM todo WHERE todo_id = (?)"
        try:
            if len(self.fetch_data(args)) == 0:
                raise TodoNotFoundException("We've searched enough for you, but we haven't found any data like this :(")
        except TodoNotFoundException as e:
            print(e)
            return False

        try:
            cursor = self.connection.cursor()
            cursor.execute(delete_data_query, (args,))
            self.connection.commit()
            cursor.close()
        except Error as e:
            print(e)
            return False
        finally:
            try:
                if self.connection:
                    self.connection.close()
            except Error as e:
                print(e)
        return True

    def fetch_all_data(self):
        todo_list = None
        select_data_query = "SELECT * FROM todo"
        try:
            cursor = self.connection.cursor()
            cursor.execute(select_data_query)
            todo_list = cursor.fetchall()
            cursor.close()
        except Error as e:
            print(e)
        finally:
            try:
                if self.connection:
                    self.connection.close()
            except Error as e:
                print(e)
        return todo_list

    def fetch_data(self, args):
        todo = None
        select_data_query = "SELECT todo_id FROM todo WHERE todo_id = ?"
        try:
            cursor = self.connection.cursor()
            cursor.execute(select_data_query, (args,))
            todo = cursor.fetchall()
            cursor.close()
        except Error as e:
            print(e)
        finally:
            try:
                if self.connection:
                    cursor.close()
            except Error as e:
                print(e)
        return todo
