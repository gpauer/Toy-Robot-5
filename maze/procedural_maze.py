import random

obstacle_list = []
x_s = 10
y_s = 10


def generate_cells():
    """
    Generate a list of cells on a 100*200 grid to generate the maze on.
    :return: A list of coordinates
    """
    global x_s, y_s
    return([(x, y) for x in range(-100, 101, x_s) for y in range(-200, 201, y_s)])
        

def neigbor_check(cells, current_cell):
    """
    Checks for unvisited neighbour cells on the grid.
    :param: cells (the grid)
    :param: current_cell (current position)
    :return: True if there is unvisited neighbours else False
    """
    global x_s, y_s
    x = current_cell[0]
    y = current_cell[1]
    if (x+x_s, y) in cells:
        return(True)
    if (x-x_s, y) in cells:
        return(True)
    if (x, y+y_s) in cells:
        return(True)
    if (x, y-y_s) in cells:
        return(True)
    return(False)


def neigbor_select(cells, current_cell):
    """
    Checks for unvisited neighbour cells on the grid.
    :param: cells (the grid)
    :param: current_cell (current position)
    :return: The unvisited neighbour cells.
    """
    neigbors = []
    x = current_cell[0]
    y = current_cell[1]
    if (x+x_s, y) in cells:
        neigbors.append((x+x_s,y))
    if (x-x_s, y) in cells:
        neigbors.append((x-x_s,y))
    if (x, y+y_s) in cells:
        neigbors.append((x,y+y_s))
    if (x, y-y_s) in cells:
        neigbors.append((x,y-y_s))
    return(neigbors[random.randint(0, len(neigbors) - 1)])


def generate_maze(current_cell, cells, old_cell):
    """
    A recursive implementation of depth first search to generate obstacles for
    the maze.
    :param: current_cell
    :param: cells
    :param: old_cell
    """
    global obstacle_list
    cells.remove(current_cell)
    while neigbor_check(cells, current_cell):
        old_cell = current_cell
        current_cell = neigbor_select(cells, current_cell)
        if (current_cell != (0,0)) and (old_cell != (0,0)):
            if current_cell[0] == old_cell[0]:
                if current_cell[1] > old_cell[1]:
                    for x in range(old_cell[1], current_cell[1] + 1, 5):
                        obstacle_list.append((current_cell[0], x))
                else:
                    for x in range(current_cell[1], old_cell[1] + 1, 5):
                        obstacle_list.append((current_cell[0], x))
            else:
                if current_cell[0] > old_cell[0]:
                    for x in range(old_cell[0], current_cell[0] + 1, 5):
                        obstacle_list.append((x, current_cell[1]))
                else:
                    for x in range(current_cell[0], old_cell[0] + 1, 5):
                        obstacle_list.append((x, current_cell[1]))
        generate_maze(current_cell, cells, old_cell)


def create_obs():
    """
    Creates a random amount of obstacles (up to 10) in the minimum area.
    """
    global obstacle_list
    generate_maze((0, 0), generate_cells(), (0, 0))
    obstacle_list = obstacle_refine(obstacle_list)
    


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
        for i in range(min_y, max_y + 1):
            if (is_position_blocked(x1, i) == True):
                return True
    return False


def obstacle_refine(obstacles):
    """
    Filters out obstacles at the edge of the grid to avoid unsolvable mazes
    being generated.
    :param: obstacles
    :return: new_obstacles
    """
    new_obs = []
    for x in obstacles:
        if (x[0] > -95 and x[0] < 95 and x[1] > -195 and x[1] < 195):
            new_obs.append(x)
    for x in range(0, 20, 5):
        new_obs.append((-100 + x, 0))
        new_obs. append((100 - x, 0))
        new_obs.append((0, 200 - x))
        new_obs. append((0, -200 + x))

    return(new_obs)


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
