import urwid
from src.util.key import on_key_press


# Created by orhantgrl
# created on 8/4/20


def init_header():
    return urwid.Text(('head', "Todowid | Todo List"), align=urwid.CENTER)


def init_body(content):
    body_walker = urwid.SimpleListWalker(content)
    body_list = urwid.ListBox(body_walker)
    body_padding = urwid.Padding(
        body_list,
        left=1,
        right=1,
    )
    return urwid.LineBox(body_padding)


def init_footer():
    footer_text = [
        ('key', "UP"), ", ", ('key', "DOWN"), ", ",
        ('key', "PAGE UP"), " and ", ('key', "PAGE DOWN"),
        " move view | ",
        ('key', "Q"), " exit",
    ]

    return urwid.Padding(urwid.AttrMap(urwid.Text(footer_text), 'foot'),
                         left=1,
                         right=1)


def init_window():
    color_palette = [
        ('body', 'light gray', 'black'),
        ('focus', 'light gray', 'dark blue', 'standout'),
        ('head', 'light cyan', 'black', 'standout'),
        ('foot', 'light gray', 'black'),
        ('key', 'light cyan', 'black', 'underline'),
        ('title', 'white', 'black', 'bold'),
        ('flag', 'dark gray', 'light gray'),
        ('error', 'dark red', 'light gray'),
    ]

    frame = urwid.Frame(
        init_body(
            [
                urwid.Text("First"),
                urwid.Text("Second")
            ]
        ),
        header=init_header(), footer=init_footer())

    main = urwid.MainLoop(
        urwid.AttrMap(frame, 'body'),
        color_palette,
        unhandled_input=on_key_press,
        handle_mouse=False
    )

    main.run()
