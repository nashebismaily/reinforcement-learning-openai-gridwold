from grid import Grid

def create_standard_grid(rewards=0.0):
    M = 3  # number of rows
    N = 4  # number of columns
    gw = Grid(M, N)  # create grid object

    gw.init_rewards(rewards)  # initialize all rewards to default

    gw.set_barrier((1, 1))   # set the position of the barrier node
    gw.set_terminal((2, 3))  # set one of two terminal nodes
    gw.set_terminal((1, 3))  # set two of two terminal nodes

    # set the reward for moving right from (2,2) to (2,3) is one
    gw.set_reward((2, 2), 'right', 1.0)
    # set the reward for moving right from (1,2) to (1,3) is minus one
    gw.set_reward((1, 2), 'right', -1.0)
    # set the reward for moving up from (0,3) to (1,3) is minus one
    gw.set_reward((0, 3), 'up', -1.0)

    # initialize all values to zero
    for i in range(0, gw.M):
        for j in range(0, gw.N):
            gw.set_value((i, j), 0)
    return gw

def create_negative_grid(rewards=-0.1):
    M = 3  # number of rows
    N = 4  # number of columns
    gw = Grid(M, N)  # create grid object

    gw.init_rewards(rewards)  # initialize all rewards to default

    gw.set_barrier((1, 1))  # set the position of the barrier node
    gw.set_terminal((2, 3))  # set one of two terminal nodes
    gw.set_terminal((1, 3))  # set two of two terminal nodes

    # set the reward for moving right from (2,2) to (2,3) is one
    gw.set_reward((2, 2), 'right', 1.0)
    # set the reward for moving right from (1,2) to (1,3) is minus one
    gw.set_reward((1, 2), 'right', -1.0)
    # set the reward for moving up from (0,3) to (1,3) is minus one
    gw.set_reward((0, 3), 'up', -1.0)

    # initialize all values to zero
    for i in range(0, gw.M):
        for j in range(0, gw.N):
            gw.set_value((i, j), 0)
    return gw
 
def create_custom_grid_1(rewards=0.0):
    M = 4  # number of rows
    N = 4  # number of columns
    gw = Grid(M, N)  # create grid object

    gw.init_rewards(rewards)  # initialize all rewards to default

    gw.set_barrier((1, 1))   # set the position of the barrier node
    gw.set_terminal((1, 2))  # set  terminal nodes
    gw.set_terminal((1, 3))  # set  terminal nodes


    # set the reward for moving up from (0,2) to (1,2) is one
    gw.set_reward((0, 2), 'up', 1.0)
    # set the reward for moving down from (2,2) to (1,2) is one
    gw.set_reward((2, 2), 'down', 1.0)
    # set the reward for moving up from (0,3) to (1,3) is minus one
    gw.set_reward((0, 3), 'up', -1.0)
    # set the reward for moving down from (2,3) to (1,3) is minus one
    gw.set_reward((2, 3), 'down', -1.0)

    # initialize all values to zero
    for i in range(0, gw.M):
        for j in range(0, gw.N):
            gw.set_value((i, j), 0)
    return gw


def create_custom_grid_2(rewards=0.0):
    M = 3  # number of rows
    N = 4  # number of columns
    gw = Grid(M, N)  # create grid object

    gw.init_rewards(rewards)  # initialize all rewards to default

    gw.set_barrier((0, 1))   # set the position of the barrier node
    gw.set_terminal((0, 2))  # set  terminal nodes
    gw.set_terminal((0, 3))  # set  terminal nodes

    # set the reward for moving down from (1,2) to (0,2) is one
    gw.set_reward((1, 2), 'down', 1.0)
    # set the reward for moving down from (1,3) to (0,3) is minus one
    gw.set_reward((1, 3), 'down', -1.0)

    # initialize all values to zero
    for i in range(0, gw.M):
        for j in range(0, gw.N):
            gw.set_value((i, j), 0)
    return gw
 
    
    
 
 















 

 
 
 
 
 

 
 
 
 
 















 

 
 
 
 
 
