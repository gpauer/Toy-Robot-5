import operator

s = 4

class Node():
    """
    Node object which is used for in the A* algo for selecting optimal
    positions and backtracking.
    """
    def __init__(self, parent=None, position=None, f=0, g=0):
        """
        Init function for the node object assigning parent, position, g and f
        attributes.
        """
        self.parent = parent
        self.position = position
        self.f = f
        self.g = g


def f_calc(position, goal):
    """
    Calculate the f heuristic which is a combination of movement cost from
    goal and movement cost from start. (combo of g and h)
    :param position: the position from which to calculate.
    :param goal:     the goal which affects the f value.
    :return:         the f value and the g value.
    (g is movement cost from start)
    """
    h = 0
    g = 0
    if goal == 'up':
        h = 200 - position[1]
        g = abs(position[1])
    elif goal == 'down':
        h = 200 + position[1]
        g = abs(position[1])
    elif goal == 'right':
        h = 100 - position[0]
        g = abs(position[0])
    elif goal == 'left':
        h = 100 + position[0]
        g = abs(position[0])
    return (h+g, g)


def astar_algo(goal, current_position, cells):
    """
    A* algorithm to find the shortest possible path based on heuristics and the 
    current goal to reach.
    :param: goal
    :param: current_position
    :param: cells which is the maze
    :return: A list of coordinates representing a path through the maze.
    """
    open_list = []
    closed_list = []
    temp_list = []
    successors = []
    path = []
    path_node = None
    open_list.append(Node(None, current_position))
    skip = False
    q = None

    while len(open_list) > 0:
        temp_list = sorted(open_list, key=operator.attrgetter("f"))
        open_list = temp_list
        q = open_list[0]
        open_list.pop(0)
        successors = neigbor_check(cells, q, goal)

        for x in successors:
            if goal == 'top' and x.position[1] == 200:
                path_node = x
                while path_node != None:
                    path.append(path_node.position)
                    path_node = path_node.parent
                return(path[::-1])
            elif goal == 'bottom' and x.position[1] == -200:
                path_node = x
                while path_node != None:
                    path.append(path_node.position)
                    path_node = path_node.parent
                return(path[::-1])
            elif goal == 'right' and x.position[0] == 100:
                path_node = x
                while path_node != None:
                    path.append(path_node.position)
                    path_node = path_node.parent
                return(path[::-1])
            elif goal == 'left' and x.position[0] == -100:
                path_node = x
                while path_node != None:
                    path.append(path_node.position)
                    path_node = path_node.parent
                return(path[::-1])

            for j in closed_list:
                if (x.position == j.position) and (j.f <= x.f):
                    skip = True

            for i in open_list:
                if (x.position == i.position) and (i.f <= x.f):
                    skip = True

            if skip == False:
                open_list.append(x)
            skip = False

        closed_list.append(q)


def neigbor_check(cells, parent_node, goal):
    """
    Checks for unvisited neighbours in the maze grid and returns them.
    :param: cells (the maze)
    :param: parent_node (the node object the neighbours originate from)
    :param: goal
    :return: list of unvisited neighbour coordinates.
    """
    global s
    current_cell = parent_node.position
    x = current_cell[0]
    y = current_cell[1]
    neigbors = []
    if (x+s, y) in cells:
        neigbors.append(Node(parent_node, (x+s, y), f_calc((x+s, y), goal)[0],\
        f_calc((x+s, y), goal)[1]))
    if (x-s, y) in cells:
        neigbors.append(Node(parent_node, (x-s, y), f_calc((x-s, y), goal)[0],\
        f_calc((x-s, y), goal)[1]))
    if (x, y+s) in cells:
        neigbors.append(Node(parent_node, (x, y+s), f_calc((x, y+s), goal)[0],\
        f_calc((x, y+s), goal)[1]))
    if (x, y-s) in cells:
        neigbors.append(Node(parent_node, (x, y-s), f_calc((x, y-s), goal)[0],\
        f_calc((x, y-s), goal)[1]))
    return(neigbors)