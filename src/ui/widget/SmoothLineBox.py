import urwid


# Created by orhantgrl
# created on 8/21/20

class SmoothLineBox(urwid.LineBox):
    def __init__(self, original_widget, title="", title_align=urwid.LEFT):
        super().__init__(
            original_widget=urwid.Padding(original_widget, left=1, right=1),
            title=title,
            title_align=title_align,
            tline="─",
            trcorner="╮",
            tlcorner="╭",
            bline="─",
            blcorner="╰",
            brcorner="╯",
            lline="│",
            rline="│",
        )
