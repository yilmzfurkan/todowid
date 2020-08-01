import urwid
import peewee
from src.model import Todo
from src.model.Todo import Todo as TodoClass

if __name__ == "__main__":
    Todo.db.connect()
    Todo.db.create_tables([TodoClass])
