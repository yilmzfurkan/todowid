import sys
from db_helper import SqliteHelper
from datetime import datetime

if __name__ == '__main__':
    DATABASE_PATH = 'todo.db'
    SQLITE_HELPER = SqliteHelper(DATABASE_PATH)

if len(sys.argv) == 1:
    print("list")
else:
    if sys.argv[1] == "--add":
        total_text = ' '.join(sys.argv[2:])
        args = (total_text, datetime.today().strftime('%Y-%m-%d'))
        SQLITE_HELPER.create_table()
        SQLITE_HELPER.insert_data(args)
    elif sys.argv[1] == "--remove":
        SQLITE_HELPER.delete_data(sys.argv[2])
        print("--Removed--")
    elif sys.argv[1] == "--edit":
        print("edit")
    else:
        print("invalid")
