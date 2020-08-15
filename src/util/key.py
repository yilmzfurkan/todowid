import urwid


# Created by orhantgrl
# created on 8/4/20

def on_key_press(key):
    if key in 'esc':
        raise urwid.ExitMainLoop()
    elif key in 'f1':
        pass
    elif key in 'f11':
        pass
