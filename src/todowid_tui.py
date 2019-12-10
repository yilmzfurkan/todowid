import urwid
from utils import attributes as atr
from db_helper import SqliteHelper


class TodowidListView:
    footer_text = [
        ('key', "UP"), ", ", ('key', "DOWN"), ", ",
        ('key', "PAGE UP"), " and ", ('key', "PAGE DOWN"),
        " move view | ",
        ('key', "Q"), " exit",
    ]

    palette = [
        ('body', 'light gray', 'black'),
        ('focus', 'light gray', 'dark blue', 'standout'),
        ('head', 'light cyan', 'black', 'standout'),
        ('foot', 'light gray', 'black'),
        ('key', 'light cyan', 'black', 'underline'),
        ('title', 'white', 'black', 'bold'),
        ('flag', 'dark gray', 'light gray'),
        ('error', 'dark red', 'light gray'),
    ]

    def __init__(self):
        self.content = self.init_main_content()

        # Main Header
        self.header = urwid.Text(('head', "Todo List"), align=urwid.CENTER)

        # Main Body
        self.body_walker = urwid.SimpleListWalker(self.content)
        self.body_list = urwid.ListBox(self.body_walker)
        self.body_padding = urwid.Padding(
            self.body_list,
            left=1,
            right=1,
        )
        self.body = urwid.LineBox(self.body_padding)

        # Main Footer
        self.footer = urwid.AttrMap(urwid.Text(self.footer_text), 'foot')

        # Main Frame
        self.frame = urwid.Frame(self.body, header=self.header, footer=self.footer)

        # Main Loop
        self.loop = urwid.MainLoop(
            urwid.AttrMap(self.frame, 'body'),
            self.palette,
            unhandled_input=self.handle_input,
            handle_mouse=False
        )

    def handle_input(self, key):
        if type(key) is str:
            if key in ('q', 'Q'):
                raise urwid.ExitMainLoop()
            elif key in ('h', 'H'):
                self.alert_dialog(
                    [
                        'Todo v0.1.0\n',
                        '\n',
                        'Press Q to quit\n',
                        'Press H for help'
                    ]
                )
        elif type(key) is tuple:
            pass

    def reset_layout(self):
        self.loop.widget = self.frame.body
        self.loop.draw_screen()

    def start_application(self):
        self.loop.run()

    def alert_dialog(self, text=None):
        if text is None:
            text = [""]

        # Dialog Header
        header_text = urwid.Text(('head', 'Todo List'), align=urwid.CENTER)
        header = urwid.AttrMap(header_text, 'body')

        # Dialog Body
        body_text = urwid.Text("Help", align=urwid.CENTER)
        body_filler = urwid.Filler(body_text, valign=urwid.TOP)
        body_padding = urwid.Padding(
            body_filler,
            left=1,
            right=1
        )
        body = urwid.LineBox(body_padding)

        # Dialog Footer
        footer = urwid.Button('Okay', self.reset_layout())
        footer = urwid.AttrWrap(footer, 'selectable', 'focus')
        footer = urwid.GridFlow([footer], 8, 1, 1, 'center')

        # Dialog Layout
        layout = urwid.Frame(
            body,
            header=header,
            footer=footer,
            focus_part='foot'
        )

        return layout

    def init_main_content(self):
        temp = []
        for chs in SqliteHelper('../todo.db').fetch_all_data():
            button = urwid.Button("{todo}".format(todo=chs))
            urwid.connect_signal(button, 'click', self.item_chosen, "{todo}".format(todo=chs))
            temp.append(urwid.AttrMap(button, None, focus_map='focus'))
        return temp

    def item_chosen(self, button, choice):
        response = urwid.Text([u"Selected to do list item ", choice, u'\n'])
        done = urwid.Button(u"Done")
        urwid.connect_signal(done, 'click', atr.exit_application)
        self.frame.body = urwid.Filler(urwid.Pile([response,
                                                   urwid.AttrMap(done, None, focus_map='focus')]))

def main():
    TodowidListView().start_application()


if __name__ == '__main__':
    main()
