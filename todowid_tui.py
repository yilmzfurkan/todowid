import urwid


def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()
    txt.set_text(repr(key))


color_palette = [
    ('banner', 'black', 'light gray'),
    ('streak', 'black', 'dark red'),
    ('bg', 'black', 'dark blue')]

txt = urwid.Text(('banner', "Hello, World"), align=urwid.CENTER)
map = urwid.AttrMap(txt, 'streak')
fill = urwid.Filler(map)
map1 = urwid.AttrMap(fill, 'bg')
loop = urwid.MainLoop(map1, palette=color_palette, unhandled_input=exit_on_q)
loop.run()
