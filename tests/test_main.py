import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
import maze.obstacles as obstacles
import robot


class MyTestCase(unittest.TestCase):
    def test_step3_default_maze(self):

        with captured_io(StringIO('HAL\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 1
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: Loaded obstacles.
There are some obstacles:
- At position 1,1 (to 5,5)""", output[:130])

    def test_step4_mazerun_noarg(self):

        with captured_io(StringIO('HAL\nmazerun\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 1
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertTrue(output.find('starting maze run..') > -1)
        self.assertTrue(output.find('I am at the top edge') > -1)

    def test_step5_mazerun_top(self):

        with captured_io(StringIO('HAL\nmazerun top\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 1
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertTrue(output.find('starting maze run..') > -1)
        self.assertTrue(output.find('I am at the top edge') > -1)

    def test_step5_mazerun_bottom(self):

        with captured_io(StringIO('HAL\nmazerun bottom\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 1
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertTrue(output.find('starting maze run..') > -1)
        self.assertTrue(output.find('I am at the bottom edge') > -1)

    def test_step5_mazerun_left(self):

        with captured_io(StringIO('HAL\nmazerun left\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 1
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertTrue(output.find('starting maze run..') > -1)
        self.assertTrue(output.find('I am at the left edge') > -1)

    def test_step5_mazerun_right(self):

        with captured_io(StringIO('HAL\nmazerun right\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 1
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertTrue(output.find('starting maze run..') > -1)
        self.assertTrue(output.find('I am at the right edge') > -1)

    def test_unittest_robot_exist(self):
        import test_robot 
        self.assertTrue('test_robot' in sys.modules, "test_robot module should be found")

    def test_unittest_robot_succeeds(self):
        import test_robot
        test_result = run_unittests("test_robot")
        self.assertTrue(test_result.wasSuccessful(), "unit tests should succeed")

    def test_unittest_world_exist(self):
        import test_world 
        self.assertTrue('test_world' in sys.modules, "test_world module should be found")

    def test_unittest_world_succeeds(self):
        import test_world
        test_result = run_unittests("test_world")
        self.assertTrue(test_result.wasSuccessful(), "unit tests should succeed")

    def test_unittest_obstacles_exist(self):
        import test_obstacles 
        self.assertTrue('test_obstacles' in sys.modules, "test_obstacles module should be found")

    def test_unittest_succeeds(self):
        import test_obstacles
        test_result = run_unittests("test_obstacles")
        self.assertTrue(test_result.wasSuccessful(), "unit tests should succeed")


if __name__ == '__main__':
    unittest.main()
