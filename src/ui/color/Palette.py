from enum import Enum


# Created by orhantgrl
# created on 8/17/20

class Schema(Enum):
    DARK = "dark"
    LIGHT = "light"


class Palette:
    def __init__(self, schema=Schema.DARK):
        """
        :type schema Schema
        """
        super().__init__()
        self.schema = schema

    def __getpalette__(self):
        if self.schema == Schema.LIGHT:
            return self.__light_palette()
        return self.__dark_palette()

    @staticmethod
    def __dark_palette():
        return [
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

    @staticmethod
    def __light_palette():
        return [
            ('frame', '', '', '', '#f1faee', '#f1faee'),
            ('focus', 'light gray', 'dark blue', 'standout'),
            ('body', '', '', '', '#03071e', '#ffffff'),
            ('foot', '', '', '', '#ffffff', '#0077b6'),
            ('key', '', '', '', '#f5871f', '#0077b6'),
            ('title', '', '', '', '#e63946', '#f1faee'),
            ('sub_title', '', '', '', '#1d3557', '#ffffff'),
            ('flag', 'dark gray', 'light gray'),
            ('error', 'dark red', 'light gray'),
        ]
