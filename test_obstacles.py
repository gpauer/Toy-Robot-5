import unittest
import unittest.mock
from world.text.world import *
from io import StringIO
import maze.obstacles as obstacles
import sys

class MyTestCase(unittest.TestCase):
    def test_get_obstacle(self):
        obstacles.random.randint = lambda a,b: 1
        obstacles.create_obs()
        self.assertEqual(obstacles.get_obstacles(), [(1, 1)])


    def test_is_position_blocked(self):
        self.assertEqual(obstacles.is_position_blocked(1, 1), True)
        self.assertEqual(obstacles.is_position_blocked(0, 0), False)


    def test_is_path_blocked(self):
        self.assertEqual(obstacles.is_path_blocked(1, -10, 1, 10), True)
        self.assertEqual(obstacles.is_path_blocked(0, -10, 0, 10), False)
        

    def test_clean_obs(self):
        obstacles.clean_obs()
        self.assertEqual(obstacles.obstacle_list, [])


if __name__ == '__main__':
    unittest.main()