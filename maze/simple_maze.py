import random

obs_list = []

def create_grid():
    """
    Creates 10 by 10 cells within the given area
    """
    grid = []
    for x in range(-100, 101, 10):
        for y in range(-200, 201, 10):
            grid.append((x,y))

    return grid


def check_neigbour(current_cell, grid):
    """
    Determines whether a surrounding cell(s) is present
    : param current_cell: a tuple representing the current position
    : param grid: y represents the number of cells in the area
    : return: True if position is blocked, else False
    """
    if (current_cell[0] + 10, current_cell[1]) in grid:
        return True
    if (current_cell[0] - 10, current_cell[1]) in grid:
        return True
    if (current_cell[0], current_cell[1] + 10) in grid:
        return True
    if (current_cell[0], current_cell[1] - 10) in grid:
        return True
    return False


def select_neigbour(current_cell, grid):
    """
    Creates a list of surrounding cells and return a random cell
    : param current_cell: a tuple representing the current position
    : param grid: y represents the number of cells in the area
    : return: True if position is blocked, else False
    """
    neighbour_cell = []

    if (current_cell[0] + 10, current_cell[1]) in grid:
        neighbour_cell.append((current_cell[0] + 10, current_cell[1]))
    if (current_cell[0] - 10, current_cell[1]) in grid:
        neighbour_cell.append((current_cell[0] - 10, current_cell[1]))
    if (current_cell[0], current_cell[1] + 10) in grid:
        neighbour_cell.append((current_cell[0], current_cell[1] + 10))
    if (current_cell[0], current_cell[1] - 10) in grid:
        neighbour_cell.append((current_cell[0], current_cell[1] - 10))

    if len(neighbour_cell) != 0:
        ran_cell = random.choice(neighbour_cell)
    else:
        return check_neigbour(current_cell, grid)

    return ran_cell


def make_obstacles():
    """
    Algorithm to generate random pathways, consisting of cells,
    within the grid and returns the coordinates of these cells as a list of 
    obstacles, therefore generating a maze
    """
    global obs_list

    current_cell = (0, 0)
    visited_cell = ()
    stack = [] # used to keep track of past movements to allow backtracking
    grid = create_grid()
    step = 1
    
    current_cell = select_neigbour(current_cell, grid)
    grid.remove((0,0))

    while len(grid) > 0:
        """
        If a neighbouring cell does not exist, the current cell backtracks until
        a neigbouring cell is present
        """
        if check_neigbour(current_cell, grid) == False:
            current_cell = stack[-1]
            stack.pop()
        else:
            stack.append(current_cell)
            visited_cell = current_cell
            current_cell = select_neigbour(current_cell, grid)
            grid.remove(current_cell)

            """ Ensures cells remain within the given area """
            if (current_cell[0] < 100 and current_cell[0] >= -100 and
                    current_cell[1] < 200 and current_cell[1] >= -200 and
                    visited_cell[0] < 100 and visited_cell[0] > -100 and
                    visited_cell[1] < 200 and visited_cell[1] > -200):

                """ x values of both current and previous cell are the same """
                if current_cell[0] == visited_cell[0]: 
                    """ Determines movement of cells and appends to obstacle list """
                    if current_cell[1] < visited_cell[1]:
                        step = -1
                    for y in range(visited_cell[1], current_cell[1] + 1, 5*step):
                        obs_list.append((current_cell[0], y))
                else:
                    """ Determines movement of cells and appends to obstacle list """
                    if current_cell[0] < visited_cell[0]:
                        step = -1
                    for x in range(visited_cell[0], current_cell[0] + 1, 5*step):
                        obs_list.append((x, current_cell[1]))
                step = 1

    return obs_list


def is_position_blocked(x,y):
    """
    Determines whether position is blocked due to an obstacle
    : param x: x position of robot
    : param y: y position of robot
    : return: True if position is blocked, else False
    """
    for coordinate in obs_list:
        if  (
            (x in range(coordinate[0], coordinate[0] + 5)) and 
            (y in range(coordinate[1], coordinate[1] + 5))
            ):
            return True
    return False
  

def is_path_blocked(x1,y1,x2,y2):
    """
    Determines whether path is blocked due to an obstacle
    : param x1: x position of robot
    : param y1: y position of robot
    : param x2: updated x position of robot
    : param y2: updated y position of robot
    : return: True if position is blocked, else False
    """
    ''' Set used for intersection '''
    range_x = set() 
    range_y = set()

    ''' Adds range of movement to x,y sets '''
    if x2 < x1:
        for x in range(x2, x1):
            range_x.add(x)
    else:
        for x in range(x1, x2):
            range_x.add(x)
    if y2 < y1:
        for y in range(y2, y1):
            range_y.add(y)
    else:
        for y in range(y1, y2):
            range_y.add(y)

    for coordinate in obs_list: 
        if x1 in range(coordinate[0], coordinate[0] + 5): 
            if  (
                range_y.intersection(range(coordinate[1],
                coordinate[1] + 5)) # checks y pos intersects with ob y pos
                ):
                return True
        if y1 in range(coordinate[1], coordinate[1] + 5):
            if  (
                range_x.intersection(range(coordinate[0],
                coordinate[0] + 5)) # checks x pos intersects with ob x pos
                ):
                return True
    return False


def get_obstacles():
    if len(obs_list) == 0:
        make_obstacles()
    return(obs_list)