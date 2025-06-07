# Create Player class
from settings import Settings

class Player:
    """ A class to manage the status and actions of players, and set properties of them."""
    
    def __init__(self):
        self.settings = Settings()
        self.initialize()

    def initialize(self):
        self.agent = None # X or O or None
        self.agent_str = None # self.convert_agent_to_str() # X or 0 or None
        self.on_turn = False # True or False
        # Create instance variable
        self.win = False 
        self.actions_possible = [] # coordinates (i, j) of tiles possible to fill.
        self.action_optimal = (None, None) # coordinates (i, j) to fill
        self.archive = self.settings.initial_archive # Save all moves of a game in a dictionary.   

    def convert_agent_to_str(self):
        # Define a tabular chart for the conversion.
        tabular_chart = {
            1 : "X",
            None : None,
            -1 : "O"
        }
        # Convert self.agent into self.agent_str.
        self.agent_str = tabular_chart[self.agent]

    def update(self, board): # attr board is an instance of the Board class.
        # Determine which player is the next mover.                        
        # Total sum of all elements of the 3X3 matrix
        # amounts to the summation of the first three elements in sum_list 
            
        # Determine the winner of the game, if there is one.
        if 3 * self.agent in board.sum_list:
            self.win = True
        else:
            self.win = False
            
        # Find the set of all possible actions (i, j) available on the board.
        # Define a list of tuples of (i, j)-coordinates of (3 X 3) square board.
        actions_set = []
        for i, row in enumerate(board.state):
            for j, col in enumerate(row):
                if col == self.settings.EMPTY:
                    actions_set.append((i, j))
        
        self.actions_possible = actions_set


    def apply_action_optimal(self, board, user_action_optimal, user_agent):
        # Returns the board that results from making move (i, j) on the board.
        updated_state = board.state
        (i, j) = user_action_optimal
        updated_state[i][j] = user_agent
        
        return updated_state

