import sys
import db_helper as dbh
from datetime import datetime

if len(sys.argv) == 1:
    print("list")
else:
    if sys.argv[1] == "--add":
        total_text = ' '.join(sys.argv[2:])
        args = (total_text, datetime.today().strftime('%Y-%m-%d'))
        conn = dbh.connect_db('todo.db')
        dbh.create_table(conn)
        dbh.insert_data(conn, args)
    elif sys.argv[1] == "--remove":
        print("remove")
    elif sys.argv[1] == "--edit":
        print("edit")
    else:
        print("invalid")
