import urwid


# Created by orhantgrl
# created on 8/4/20

def on_key_press(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()
