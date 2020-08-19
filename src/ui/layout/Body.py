import urwid
from src.ui.layout.Layout import Layout
from src.model.Todo import Todo


# Created by orhantgrl
# created on 8/8/20

class Body(Layout):
    def __init__(self, contents):
        """
        :type contents list
        """
        super().__init__()
        self.contents = contents

    def __draw__(self):
        body_walker = urwid.SimpleListWalker(self.contents)
        body_list = urwid.ListBox(body_walker)
        body_padding = urwid.Padding(
            body_list,
            left=1,
            right=1,
        )
        return urwid.AttrMap(body_padding, attr_map='body')


class Content:
    def __init__(self, todo):
        """
        :type todo Todo
        """
        super().__init__()
        self.todo = todo

    def draw_content_layout(self):
        left_content = urwid.Pile(
            widget_list=[
                urwid.Text(str(self.todo.id)),
                urwid.Text(self.todo.subject)
            ]
        )

        right_content = urwid.Pile(
            widget_list=[
                urwid.Text(self.todo.date, align=urwid.RIGHT)
            ]
        )

        parent = urwid.Columns(
            widget_list=[
                left_content,
                right_content
            ]
        )

        return urwid.LineBox(parent)
