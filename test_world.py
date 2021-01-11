import unittest
import unittest.mock
from world.text.world import *
from io import StringIO
import sys

class MyTestCase(unittest.TestCase):
    def test_show_position(self):
        clean()
        captured_output = StringIO()
        sys.stdout = captured_output
        show_position('HAL')
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), ' > HAL now at position (0,0).\n')


    def test_is_position_allowed(self):
        self.assertEqual(is_position_allowed(50, -80), True)
        self.assertEqual(is_position_allowed(100, -300), False)


    def test_update_position(self):
        global position_y, position_x
        clean()
        self.assertEqual(update_position(300, 0), (False, False))
        self.assertEqual(update_position(10, 0), (True, False))
        self.assertEqual(update_position(100, 0), (True, False))
        self.assertEqual(update_position(20, 0), (True, False))
        self.assertEqual(update_position(1000, 0), (False, False))


if __name__ == '__main__':
    unittest.main()
        