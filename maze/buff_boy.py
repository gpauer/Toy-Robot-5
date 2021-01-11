#imports the random module
import random

#this is my obstacle list
obstacles = []

def is_position_blocked(x,y):
    """ This function checks if the position of the robot falls into a obstacle in the obstacle list
    params = x,y
    return = False or True
    globals = obstacle list"""
    global obstacles

    robot_position = (x,y)

    for item in obstacles:
        if robot_position == item:
            return True
    for obstacle in obstacles:
        for counter in range(5):
            if (x == obstacle[0]+counter and y == obstacle[1]) or (y == obstacle[1]+counter and x == obstacle[0]):
                return True
            elif x == obstacle[0]+counter and y == obstacle[1]+counter:
                return True
            elif (x == obstacle[0]+1 and y == obstacle[1]+counter) or (x == obstacle[0]+2 and y == obstacle[1]+counter):
                return True
            elif (x == obstacle[0]+3 and y == obstacle[1]+counter) or (x == obstacle[0]+4 and y == obstacle[1]+counter):
                return True
            elif (x == obstacle[0]+counter and y == obstacle[1]+1) or (x == obstacle[0]+counter and y == obstacle[1]+2):
                return True
            elif (x == obstacle[0]+counter and y == obstacle[1]+3) or (x == obstacle[0]+counter and y == obstacle[1]+4):
                return True    
    else:
        return False


def is_path_blocked(x1,y1, x2, y2):
    """ This function checks if there is an obstacle that falls with the robots path
    params = x1,y1,x2,y2
    return = True or False
    globals = obstacle list"""
    global obstacles    
    
    if x1 == x2:
        start = y1
        end = y2
        other = x1
        index = (1,0)
    else:
        start = x1
        end = x2
        other = y1
        index = (0,1)
    for obst in obstacles:
        for counter in range(0,5):
            if start <= obst[index[0]]+counter  <= end and obst[index[1]] <= other <= obst[index[1]]+4:
                return True
            elif start >= obst[index[0]] + counter >= end and obst[index[1]] >= other >= obst[index[1]]+4:
                return True
            elif start >= obst[index[0]] + counter >= end and obst[index[1]] <= other <= obst[index[1]]+4:
                return True
            elif start <= obst[index[0]] + counter <= end and obst[index[1]] >= other >= obst[index[1]]+4:
                return True
    return False

    
def get_obstacles():
    """ This function generates the obstacle list at random to be used throughout the running program
    params = None
    return = obstacle list
    globals = obstacle list"""
    global obstacles
    
    obstacle_exit_pos  =  []

    for x in range(-100,96):
        if ('5' in str(x)) or ('0' in str(x))  :
            if -10 <= x < 10:
                continue
            else:
                obstacle_exit_pos.append((x,196))
    for x in range(-100,96):
        if ('5' in str(x)) or ('0' in str(x))  :
            if -10 <= x < 10:
                continue
            else:
                obstacle_exit_pos.append((x,-200))
    for y in range(-200,196):
        if ('5' in str(y)) or ('0' in str(y)):
            if -10 <= y < 10:
                continue
            else:
                obstacle_exit_pos.append((-100,y))
    for y in range(-200,196):
        if ('5' in str(y)) or ('0' in str(y)):
            if -10 <= y < 10:
                continue
            else:
                obstacle_exit_pos.append((95,y))

    maze_list = []
    counter = 0
    y_value = 5
    num_5_restrict_list = [51,52,53,54,56,57,58,59,-51,-52,-53,-54,-56,-57,-58,-59]
    while counter != 13:
        for i in range(-100,96):
            if (('5' in str(i)) or ('0' in str(i))) and (i not in num_5_restrict_list) : 
                maze_list.append((i,y_value))
        counter += 1
        y_value += 15
    counter = 0
    y_value = 10
    
    while counter != 13:
        for i in range(-100,96):
            if (('5' in str(i)) or ('0' in str(i))) and (i not in num_5_restrict_list) : 
                maze_list.append((i,-y_value))
        counter += 1
        y_value += 15

    #adds obstacles to the list
    obstacles = [(5,195),(5,190),(-85,175),(-85,180),(-10,160),(-10,165),(80,145),(80,150),(-65,145),(-65,150),(-15,130),(-15,135),
    (-30,115),(-30,120),(-75,100),(-75,105),(-90,100),(-90,105),(-30,85),(-30,90),(85,10),(85,15),(90,10),(90,15),
    (-70,40),(-70,45),(0,40),(0,45),(10,55),(10,60),
    #bottom list
    (5,-200),(5,-195),(-85,-185),(-85,-180),(-10,-170),(-10,-165),(80,-155),(80,-150),(-65,-155),(-65,-150),(-15,-140),(-15,-135),
    (-30,-125),(-30,-120),(-75,-110),(-75,-105),(-90,-110),(-90,-105),(-30,-95),(-30,-90),(65,-50),(65,-45),(65,-65),(65,-60),
    (-60,55),(-60,60),
    #middle list
    (-20,-5),(-20,0),(15,-5),(15,0),(-85,-5),(-85,0),(80,-5),(80,0),(-5,25),(-5,30),(0,25),(0,30),(80,10),(80,15),
    (65,40),(65,45),(80,25),(80,30),(30,25),(30,30),(-20,-35),(-20,-30),(15,-35),(15,-30),(-5,-50),(-5,-45),(0,-50),(0,-45),(-75,-65),(-75,-60),(35,-65),(35,-60),(-35,-65),(-35,-60),
    (25,-20),(25,-15),(-45,-20),(-45,-15),(-40,-20),(-40,-15),(-75,10),(-75,15)]

    #removes obstacles in the list
    maze_restrict_list = [(45,185),(40,185),(-95,185),(-90,185),(-95,170),(-90,170),(-5,170),(0,170),(-15,155),(-20,155),(85,155),(90,155),
    (85,140),(90,140),(-95,140),(-90,140),(40,140),(45,140),(-95,125),(-90,125),(85,125),(90,125),(0,125),(5,125),(-85,110),(-80,110),(20,110),(25,110),
    (-85,95),(-80,95),(-25,95),(-20,95),(-40,80),(-35,80),(75,80),(80,80),(-5,65),(0,65),(35,50),(40,50),(51,65),(52,65),(53,65),(54,65),(55,65),(56,65),(57,65),(58,65),(59,65),(60,65)]
    
    maze_restrict_list_2 =[(45,-190),(40,-190),(-95,-190),(-90,-190),(-95,-175),(-90,-175),(-5,-175),(0,-175),(-15,-160),(-20,-160),(85,-160),(90,-160),
    (85,-145),(90,-145),(-95,-145),(-90,-145),(40,-145),(45,-145),(-95,-130),(-90,-130),(85,-130),(90,-130),(0,-130),(5,-130),(-85,-115),(-80,-115),(20,-115),(25,-115),
    (-85,-100),(-80,-100),(-25,-100),(-20,-100),(-40,-85),(-35,-85),(75,-85),(80,-85),(-5,-70),(0,-70),(-70,-55),(-65,-55),(-70,-70),(-65,-70),(20,35),(25,35),
    (40,20),(45,20),(-80,35),(-75,35),(-15,35),(-10,35)]
    
    maze_restrict_list_3 = [(-95,5),(-90,5),(-15,5),(-10,5),(-5,5),(0,5),(5,5),(10,5),(85,5),(90,5),(5,20),(10,20),(85,20),(90,20),(85,35),(90,35),(70,35),(75,35),(85,-40),(90,-40),
    (40,-25),(45,-25),(40,-55),(45,-55),(-85,20),(-80,20),(85,-70),(90,-70),(-70,-25),(-65,-25),(-35,50),(-30,50),(-85,50),(-80,50)]

    maze_restrict_list_4 = [(-95,-10),(-90,-10),(-15,-10),(-10,-10),(-5,-10),(0,-10),(5,-10),(10,-10),(85,-10),(90,-10),(-15,-25),(-10,-25),(5,-40),(10,-40)
    ,(40,-70),(45,-70),(85,-55),(90,-55)]

    for i in obstacle_exit_pos:
        obstacles.append(i)
    for o in maze_list:
        obstacles.append(o)
    for i in maze_restrict_list:
        if i in obstacles:
            obstacles.remove(i)
        else:
            continue
    for i in maze_restrict_list_2:
        if i in obstacles:
            obstacles.remove(i)
        else:
            continue
    for i in maze_restrict_list_3:
        if i in obstacles:
            obstacles.remove(i)
        else:
            continue
    for i in maze_restrict_list_4:
        if i in obstacles:
            obstacles.remove(i)
        else:
            continue        


    return list(reversed(sorted(obstacles)))


def clear_globals():
    """ This function clears all globals within the current module
    params = None
    return = None
    globals = obstacle list
    """
    global obstacles
    obstacles = []
