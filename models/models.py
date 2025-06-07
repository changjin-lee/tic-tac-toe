# models.py includes several models to calculate the optimal action for AI.

class Model:
    """A class Model includes several models to calculate the optimal action for AI."""
    def __init__(self):
        pass

    # AI model: minmax algorithm.
    def minimax(self):
        """
        Returns the optimal action for the current player, AI_Agent, on the board.
        """
        # We need know which is the ai.agent, X or O.
        # if ai.agent = 1, or if ai.agent_str = "X", we maximize the score as high as possible.
        # if ai.agent = -1, or if ai.agent_str = "O", the opposite: minimize the score.
        
        # Execute quantify_state(board) to get matrix, counter_filled, sum_list from quantify_state(board)
        # Find the number of tiles filled on board: counter_filled from quantify_state(board)
        #
        # -----------------
        # Random Strategy: 
        # -----------------
        #   choose any empty tile at random:
        #   make a list including the tuples of (i, j) for the empty tiles.
        #   make a rondom choice of a tuple out of the list.
        #   return it as the ai_move in runner.py
        import random
        
        matrix = self.board.state
        tiles_empty = []
        
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if col == 0:
                    tiles_empty.append((i, j))
        
        ai_move = random.choice(tiles_empty)
        return ai_move
        # return (2,2)