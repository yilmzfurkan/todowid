from peewee import *

# Created by orhantgrl
# created on 8/1/20

db = SqliteDatabase('todo.db')


class Todo(Model):
    id = AutoField()
    subject = CharField()
    date = DateTimeField()

    class Meta:
        database = db
