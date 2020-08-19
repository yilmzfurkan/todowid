import urwid
import datetime
from src.util.key import on_key_press
from src.ui.layout.Header import Header
from src.ui.layout.Body import Body, Content
from src.ui.layout.Footer import Footer
from src.model.Todo import Todo
from src.ui.color.Palette import Palette, Schema


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
        ('key', 'Help '), 'F1', ' | ',
        ('key', 'Exit '), 'ESC'
    ]

    version = [
        ('key', 'Version '), 'v0.0.1'
    ]

    return Footer(hint, version).__draw__()


def init_window():
    frame = urwid.Frame(
        header=init_header(),
        body=init_body(),
        footer=init_footer())

    color_palette = Palette(Schema.DARK).__getpalette__()

    main = urwid.MainLoop(
        urwid.AttrMap(frame, 'frame'),
        color_palette,
        unhandled_input=on_key_press,
        handle_mouse=False
    )
    main.screen.set_terminal_properties(colors=256)
    main.run()
