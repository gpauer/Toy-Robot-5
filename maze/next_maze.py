import random

# the list of obstacles createt by the get_obstacles command
obstacle_list = []
                                     
def is_position_blocked(x, y):
    """
    Summary: Checks if the position (x,y) falls inside an obstacle.
    Params:
    x(int): The x-coordinate of the destination of the robot
    y(int): The y-coordinate of the destination of the robot
    Returns:
    True/False(bool): Returns True or False based on wether the position falls
    inside an obstacle or not
    """

    for i in obstacle_list:
        if ((x >= i[0] and x <= i[0] + 4) and (y >= i[1] and y <= i[1] + 4)):
            return True
    return False


def is_path_blocked(x1, y1, x2, y2):
    """
    Summary: Checks if the is an obstacle in the path between the current location
    of the robot to the destination.
    Params:
    x1(int): The current x coordinate of the robot
    y1(int): The current y coordinate of the robot
    x2(int): The destination x coordinate of the robot
    y2(int): The desination y coordinate of the robot
    Returns:
    True/False(bool): Returns True or False based on wether or not there's an obstacle
    in the path between the robot and its destination
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


def make_obstacles():
    """
    Summary: Generates a list of a random number (up to 10) of randomly positioned obstacles
    Returns:
    obstacle_list(list): The list of tuples as coordinates of the obtacles
    """

    global obstacle_list

    x_list = [x for x in range(-100, 100, 8)]
    y_list = [y for y in range(-200, 200, 8)]

    temp_list = []

    for y in y_list:
        for x in x_list:
            temp_list.append((x, y))
            temp_list.append((x + 5, y))
            temp_list.append((x + 5, y + 5))
            temp_list.append((x, y + 5))

            horizontal = random.randint(0, 5)
            if horizontal == 0:
                temp_list.pop(1)
                temp_list.pop(0)
            elif horizontal == 1:
                temp_list.pop(3)
                temp_list.pop(0)
            elif horizontal == 2:
                temp_list.pop(1)
                temp_list.pop(0)
            elif horizontal == 3:
                temp_list.pop(3)
                temp_list.pop(0)
            else:
                temp_list.clear()
                temp_list.append((x + 5, y + 5))

            obstacle_list.extend(temp_list)
            temp_list = []

    for pos in obstacle_list:
        x = pos[0]
        y = pos[1]
        if (x < 10 and x > -10) and (y < 10 and y > -10):
            obstacle_list.remove(pos)
    return obstacle_list


def get_obstacles():
    if len(obstacle_list) == 0:
        make_obstacles()
    return(obstacle_list)