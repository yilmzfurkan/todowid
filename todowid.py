import sys

if len(sys.argv) == 1:
        print("list")
else:
    if sys.argv[1] == "--add":
        print("add")
    elif sys.argv[1] == "--remove":
        print("remove")
    elif sys.argv[1] == "--edit":
        print("edit")
    else:
        print("unvalid")
