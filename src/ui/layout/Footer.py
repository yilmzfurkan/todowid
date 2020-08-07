import urwid
from src.ui.layout.Layout import Layout


# Created by orhantgrl
# created on 8/7/20

class Footer(Layout):
    def __init__(self, hint, version):
        """
        :type hint List
        :type version List
        """
        super().__init__()
        self.hint = hint
        self.version = version

    def __draw__(self):
        contents = urwid.Columns([
            urwid.Text(self.hint, align=urwid.LEFT),
            urwid.Text(self.version, align=urwid.RIGHT)
        ])

        contents_padding = urwid.Padding(contents, left=1, right=1)
        attr_map = urwid.AttrMap(w=contents_padding, attr_map="foot")
        return urwid.Padding(w=attr_map, left=1, right=1)
