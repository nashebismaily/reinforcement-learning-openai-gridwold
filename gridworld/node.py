class Node:
    """GridWorld Node"""
    
    def __init__(self):
        self.state = None           # (i,j) tuple of coordinates of node
        self.value = None           # value of the node
        self.is_terminal = False    # flag for terminal state
        self.is_barrier = False     # flag for barrier state
        self.left = None        # immediate reward for left, None if invalid
        self.right = None       # immediate reward for right, None if invalid    
        self.down = None        # immediate reward for down, None if invalid
        self.up = None          # immediate reward for up, None if invalid
        
    def set_state(self,state):
        self.state = state
    def get_state(self):
        return self.state
    def set_value(self,value):
        self.value = value
    def get_value(self):
        return self.value
    def set_is_terminal(self,terminal):
        self.is_terminal = terminal
    def get_is_terminal(self):
        return self.is_terminal
    def set_is_barrier(self,barrier):
        self.is_barrier = barrier
    def get_is_barrier(self):
        return self.is_barrier
    
    def set_left(self,reward):
        self.left = reward
    def get_left(self):
        return self.left
    def set_right(self,reward):
        self.right = reward
    def get_right(self):
        return self.right
    def set_down(self,reward):
        self.down = reward
    def get_down(self):
        return self.down
    def set_up(self,reward):
        self.up = reward
    def get_up(self):
        return self.up
