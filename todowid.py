import urwid

txt = urwid.Text("Hello, World", align=urwid.CENTER)
fill = urwid.Filler(txt, 'top')
loop = urwid.MainLoop(fill)
loop.run()
