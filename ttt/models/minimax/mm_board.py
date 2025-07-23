# mm_board.py
# defines a child class of Board with an additional property of self.score,
# which can be obtained by utility function when the node becomes a leaf node.

# The module board.py is in the parent folder.
from board import Board

class MMBoard(Board):
    def __init__(self, user_agent):
        super().__init__()
        self.user_agent = user_agent
        self.ai_agent = -1 if self.user_agent == 1 else 1
        self.score = None

    # Update the MMBoard with the new items added.
    def update(self, board_state):
        super().update(board_state)
        self.score = self.evaluation()
        
    # Check if a game is over, and determines who is the winner.
    def evaluation(self):
        # Evaluate the leaf state or the terminal state.
        if self.game_over:
            if 3 in self.sum_list:
                return 1
            elif -3 in self.sum_list:
                return -1
            else:
                return 0
        else:
            return None
       