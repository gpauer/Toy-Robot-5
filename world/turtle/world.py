import turtle, sys, importlib

valid_maze = ['buff_boy', 'next_maze', 'obstacles', 'procedural_maze', 'simple_maze']

temp = list(set(sys.argv) & set(valid_maze))
if len(temp) > 0:
    is_position_blocked = getattr(importlib.import_module('maze.'+temp[0]),\
    "is_position_blocked")
    is_path_blocked = getattr(importlib.import_module('maze.'+temp[0]),\
    "is_path_blocked")
    get_obstacles = getattr(importlib.import_module('maze.'+temp[0]),\
    "get_obstacles")
else:
    from maze.obstacles import is_position_blocked, is_path_blocked, get_obstacles

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

t = turtle.Turtle()


def draw_rectangle(size_x, size_y, x, y):
    """
    Draws a rectangle on the turtle interface.
    :param size_x: the horizontal size of the rectangle
    :param size_y: the vertical size of the rectangle
    :param x: the x coordinate of the bottom left corner of the rectangle
    :param y: the y coordinate of the bottom left corner of the rectangle
    """
    current_pos = t.position()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.forward(size_y)
    t.right(90)
    t.forward(size_x)
    t.right(90)
    t.forward(size_y)
    t.right(90)
    t.forward(size_x)
    t.right(90)
    t.penup()
    t.goto(current_pos[0], current_pos[1])

def turtle_start():
    """
    Draws the border and all the obstacles and returns refresh settings to
    normal when done.
    """
    global t
    t._tracer(0,0)
    t.color('red')
    t.speed(0)
    t.left(90)
    t.penup()
    t.goto(0, 0)
    draw_rectangle(max_x*2, max_y*2, min_x, min_y)
    t.fillcolor('red')
    t.begin_fill()
    for x in get_obstacles():
        draw_rectangle(4, 4, x[0], x[1])
    t.end_fill()
    t.color('black')
    t._tracer(1,0)


def show_position(robot_name):
    """
    Prints the current position of the robot.
    :param robot_name: the name of the robot
    """
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps, current_direction_index):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    and shows the movements on the turtle interface
    :param steps:
    :return:    (False, False) if the path is not blocked and its out of bounds
                (False, True) if the the path is blocked
                (True, False) if the path is not blocked and it's not out of bounds
    """

    global position_x, position_y, directions
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if (is_position_blocked(new_x, new_y)) or (is_path_blocked(position_x,\
        position_y, new_x, new_y)):
        return False, True    

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        t.forward(steps)
        return True, False
    return False, False


def return_xy():
    """
    Returns the global variables position_x and position_y.
    :return: (x, y)
    """
    global position_x, position_y
    return (position_x, position_y)


def turn_right():
    """
    Turns the turtle (robot) right by 90 degrees.
    """
    t.right(90)


def turn_left():
    """
    Turns the turtle (robot) left by 90 degrees.
    """
    t.left(90)

def clean():
    """
    Resets the global positional variables of x and y.
    """
    global position_x, position_y
    position_x = 0
    position_y = 0
