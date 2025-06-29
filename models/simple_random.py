# simple_random.py
# makes a simple random choice for the optimal action for AI: No sophistcated strategy implemented at all.
    
import random

class SimpleRandom():
    """A class represents a simple random model for the optimal action for AI: 
    No sophistcated strategy implemented at all but just a simple random choice."""

    # def __init__(self, board_state, user_agent):
    def __init__(self, board_state, user_agent):
        # Get information about the board and the user.
        self.board_state = board_state
        # Find self.tiles_empty from self.board_state.
        self.tiles_empty = self.find_tiles_empty()
        # board_state includes the user's recent move.
        self.user_agent = user_agent
        self.tiles_empty = self.find_tiles_empty()
        self.ai_move = (None, None) # Initialize the ai_move.
        self.ai_move = random.choice(self.tiles_empty)

    def find_tiles_empty(self):
        # matrix = self.board.state
        matrix = self.board_state
        tiles_empty = []
        
        for i, row in enumerate(matrix):
            for j, element in enumerate(row):
                if element == 0:
                    tiles_empty.append((i, j))
        return tiles_empty