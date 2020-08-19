import urwid


# Created by orhantgrl
# created on 8/4/20

def on_key_press(key):
    if key == 'esc':
        raise urwid.ExitMainLoop()
    elif key == 'f1':
        pass
    elif key == 'f11':
        pass
