import urwid
import datetime
from src.util.key import on_key_press
from src.ui.layout.Header import Header
from src.ui.layout.Footer import Footer


# Created by orhantgrl
# created on 8/4/20


def init_header():
    date = datetime.datetime.now().strftime('%A %d %B')
    return Header(
        title='Todowid',
        subtitle=date,
    ).__draw__()


def init_body(content):
    body_walker = urwid.SimpleListWalker(content)
    body_list = urwid.ListBox(body_walker)
    body_padding = urwid.Padding(
        body_list,
        left=1,
        right=1,
    )
    return body_padding


def init_footer():
    """
    footer_text = [
        ('key', "UP"), ", ", ('key', "DOWN"), ", ",
        ('key', "PAGE UP"), " and ", ('key', "PAGE DOWN"),
        " move view | ",
        ('key', "Q"), " exit",
    ]
    """

    hint = [
        ('key', 'Help '), 'H', ' | ',
        ('key', 'Exit '), 'Q'
    ]

    version = [
        ('key', 'Version '), 'v0.0.1'
    ]

    return Footer(hint, version).__draw__()


def init_window():
    color_palette = [
        ('body', 'light gray', 'black'),
        ('focus', 'light gray', 'dark blue', 'standout'),
        ('head', '', '', '', '#FF5722', ''),
        ('foot', '', '', '', 'light gray', '#3D537F'),
        ('key', '', '', '', '#FF5722', '#3D537F'),
        ('title', 'white', 'black', 'bold'),
        ('flag', 'dark gray', 'light gray'),
        ('error', 'dark red', 'light gray'),
    ]

    frame = urwid.Frame(
        body=init_body(
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
    main.screen.set_terminal_properties(colors=256)
    main.run()
