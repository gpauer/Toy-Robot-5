import unittest
from io import StringIO
import robot
from test_base import run_unittests
from test_base import captured_io
import maze.obstacles as obstacles
import sys

class MyTestCase(unittest.TestCase):
    def test_history(self):
        with captured_io(StringIO('HAL\nforward 5\nforward 5\nfaarward 5\nreplay\noff')) as (out, err):
            obstacles.random.randint = lambda a,b: 0
            robot.robot_start()
        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: Loaded obstacles.
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,5).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,10).
HAL: What must I do next? HAL: Sorry, I did not understand 'faarward 5'.
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,15).
 > HAL moved forward by 5 steps.
 > HAL now at position (0,20).
 > HAL replayed 2 commands.
 > HAL now at position (0,20).
HAL: What must I do next? HAL: Shutting down..""", output)


    def test_reverse(self):
        with captured_io(StringIO('HAL\nforward 5\nforward 3\nforward 2\nreplay reversed 2\noff')) as (out, err):
            obstacles.random.randint = lambda a,b: 0
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: Loaded obstacles.
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,5).
HAL: What must I do next?  > HAL moved forward by 3 steps.
 > HAL now at position (0,8).
HAL: What must I do next?  > HAL moved forward by 2 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 3 steps.
 > HAL now at position (0,13).
 > HAL moved forward by 5 steps.
 > HAL now at position (0,18).
 > HAL replayed 2 commands in reverse.
 > HAL now at position (0,18).
HAL: What must I do next? HAL: Shutting down..""", output)


    def test_silent_reverse(self):
        with captured_io(StringIO('HAL\nback 50\nforward 5\nforward 5\nforward 10\nreplay reversed silent\noff')) as (out, err):
            obstacles.random.randint = lambda a,b: 0
            robot.robot_start()

        output = out.getvalue().strip()
        print(output)
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: Loaded obstacles.
HAL: What must I do next?  > HAL moved back by 50 steps.
 > HAL now at position (0,-50).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,-45).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,-40).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,-30).
HAL: What must I do next?  > HAL replayed 4 commands in reverse silently.
 > HAL now at position (0,-60).
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_range(self):
        with captured_io(StringIO('HAL\nback 50\nforward 5\nforward 5\nright\nforward 10\nback 10\nleft\nreplay 5-2\noff')) as (out, err):
            obstacles.random.randint = lambda a,b: 0
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: Loaded obstacles.
HAL: What must I do next?  > HAL moved back by 50 steps.
 > HAL now at position (0,-50).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,-45).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,-40).
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,-40).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (10,-40).
HAL: What must I do next?  > HAL moved back by 10 steps.
 > HAL now at position (0,-40).
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,-40).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,-35).
 > HAL turned right.
 > HAL now at position (0,-35).
 > HAL moved forward by 10 steps.
 > HAL now at position (10,-35).
 > HAL replayed 3 commands.
 > HAL now at position (10,-35).
HAL: What must I do next? HAL: Shutting down..""", output)


if __name__ == '__main__':
    unittest.main()
        