import urwid
import datetime
from src.util.key import on_key_press
from src.ui.layout.Header import Header
from src.ui.layout.Body import Body, Content
from src.ui.layout.Footer import Footer
from src.model.Todo import Todo


# Created by orhantgrl
# created on 8/4/20


def init_header():
    date = datetime.datetime.now().strftime('%A %d %B')
    return Header(
        title='Todowid',
        subtitle=date,
    ).__draw__()


def init_body():
    # Dummy Data
    contents = [
        Content(Todo(123, "First TODO", "2020-08-08")).draw_content_layout(),
        Content(Todo(456, "Second TODO", "2020-08-08")).draw_content_layout(),
        Content(Todo(789, "Third TODO", "2020-08-08")).draw_content_layout(),
    ]

    return Body(contents=contents).__draw__()


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
        ('frame', '', '', '', '#121212', '#121212'),
        ('focus', 'light gray', 'dark blue', 'standout'),
        ('body', '', '', '', 'light gray', '#121212'),
        ('foot', '', '', '', 'light gray', '#3D537F'),
        ('key', '', '', '', '#FF5722', '#3D537F'),
        ('title', '', '', '', '#FF5722', '#121212'),
        ('sub_title', '', '', '', 'white', '#121212'),
        ('flag', 'dark gray', 'light gray'),
        ('error', 'dark red', 'light gray'),
    ]

    frame = urwid.Frame(
        header=init_header(),
        body=init_body(),
        footer=init_footer())

    main = urwid.MainLoop(
        urwid.AttrMap(frame, 'frame'),
        color_palette,
        unhandled_input=on_key_press,
        handle_mouse=False
    )
    main.screen.set_terminal_properties(colors=256)
    main.run()
