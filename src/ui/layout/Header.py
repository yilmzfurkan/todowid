import urwid
from src.ui.layout.Layout import Layout


# Created by orhantgrl
# created on 8/6/20

class Header(Layout):
    def __init__(self, title, subtitle):
        """
        :type title str
        :type subtitle str
        """
        super().__init__()
        self.title = title
        self.subtitle = subtitle

    def __draw__(self):
        title = urwid.BigText(self.title, urwid.HalfBlock5x4Font())
        date = urwid.Text(self.subtitle, align=urwid.CENTER)

        columns = urwid.Pile([
            urwid.AttrMap(urwid.Padding(w=title, align=urwid.CENTER, width=urwid.CLIP), 'title'),
            urwid.AttrMap(urwid.Padding(date), 'sub_title'),
        ])

        filler = urwid.Filler(body=columns, top=4, bottom=2)
        return urwid.Padding(w=urwid.BoxAdapter(box_widget=filler, height=8), left=1, right=1)
