import unittest
from src.ui.color.Palette import Palette, Schema


# Created by orhantgrl
# created on 8/19/20

class TestPalette(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.palette = Palette(Schema.LIGHT)

    def test_schema(self):
        self.assertEqual(self.palette.schema.value, "light", "Color schema is not light")


if __name__ == '__main__':
    unittest.main()
