import sys
from src.window import init_window


# Created by orhantgrl
# created on 8/3/20

def check_argument(argument):
    help_message = 'usage: todowid [no-args]'
    switch = {
        '-help': help_message,
        '-version': "todowid 0.0.1"
    }

    return switch.get(argument, help_message)


def main():
    if len(sys.argv) > 1:
        print(check_argument(argument=sys.argv[1]))
        return
    init_window()


if __name__ == '__main__':
    main()
