import sys
from db_helper import SqliteHelper
from datetime import datetime

if __name__ == '__main__':
    DATABASE_PATH = 'todo.db'
    SQLITE_HELPER = SqliteHelper(DATABASE_PATH)

if len(sys.argv) == 1:
    for temp in SQLITE_HELPER.fetch_all_data():
        print(*temp)
else:
    if sys.argv[1] == "--add":
        total_text = ' '.join(sys.argv[2:])
        args = (total_text, datetime.today().strftime('%Y-%m-%d'))
        SQLITE_HELPER.create_table()
        SQLITE_HELPER.insert_data(args)
    elif sys.argv[1] == "--remove":
        if SQLITE_HELPER.delete_data(sys.argv[2]):
            print("Item {} successfully deleted".format(sys.argv[2]))
    elif sys.argv[1] == "--edit":
        print("edit")
    else:
        print("invalid")
