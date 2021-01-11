import random

obstacle_list = []

def create_obs():
    """
    Creates a random amount of obstacles (up to 10) in the minimum area.
    """
    global obstacle_list
    len_obstacles = random.randint(0, 11)
    obstacle_list = [(random.randint(-100, 100), random.randint(-200, 200)) for x in range(0, len_obstacles)]

def is_position_blocked(x,y):
    """
    Checks if a certain position on the robot's grid is blocked.
    :param x: the x coordinate to be checked
    :param y: the y coordinate to be checked
    """ 
    global obstacle_list
    for i in obstacle_list:
        if ((x >= i[0] and x <= i[0] + 4) and (y >= i[1] and y <= i[1] + 4)):
            return True
    return False


def is_path_blocked(x1,y1, x2, y2):
    """
    Checks if the path between 2 coordinates are blockd (if x1 == x2 or y1 == y2)
    :param x1: the first x coordinate
    :param y1: the first y coordinate
    :param x2: the second x coordinate
    :param y2: the second y coordinate
    """
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)
    if y1 == y2:
        for i in range(min_x, max_x + 1):
            if (is_position_blocked(i, y1) == True):
                return True
    elif x1 == x2:
        for i in range(min_y, max_y):
            if (is_position_blocked(x1, i) == True):
                return True
    return False


def get_obstacles():
    """
    Returns the global obstacle list.
    """
    global obstacle_list
    if len(obstacle_list) == 0:
        create_obs()
    return(obstacle_list)


def clean_obs():
    """
    Clears the global obstacle list.
    """
    global obstacle_list
    obstacle_list = []