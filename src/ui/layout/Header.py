import datetime

import urwid

from src.ui.layout.Layout import Layout


# Created by orhantgrl
# created on 8/6/20

class Header(Layout):
    __date = datetime.datetime.now().strftime('%A %d %B')

    def __init__(self, title):
        """
        :type title str
        :type date str
        """
        super().__init__()
        self.title = title

    def __draw__(self):
        title = urwid.Text(self.title)
        date = urwid.Text(self.__date, align=urwid.RIGHT)

        columns = urwid.Columns([
            urwid.AttrMap(urwid.Padding(w=title, align=urwid.LEFT), 'app_name'),
            urwid.AttrMap(urwid.Padding(date), 'date'),
        ])

        padding = urwid.Padding(w=columns, left=1, right=1)
        filler = urwid.Filler(body=padding, top=2)
        return urwid.BoxAdapter(box_widget=filler, height=2)
