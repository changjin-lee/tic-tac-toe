# models.py includes several models to calculate the optimal action for AI.

class ModelRandom:
    """A class Model includes several models to calculate the optimal action for AI."""
    def __init__(self, board):
        self.board = board # board is an instance of the Board class.

    # AI model: minimax algorithm.
    def minimax(self):
        """
        Returns the optimal action for the current player, AI_Agent, on the board.
        """
        # We need know which is the ai.agent, X or O.
        # if ai.agent = 1, or if ai.agent_str = "X", we maximize the score as high as possible.
        # if ai.agent = -1, or if ai.agent_str = "O", the opposite: minimize the score.
        
        # Execute board.update(board.state) to get matrix, count_filled, sum_list from board.update(board.state)
        # Find the number of tiles filled on board: count_filled from board.update(board.state)
        # -----------------
        # Random Strategy: 
        # -----------------
        #   - choose any empty tile at random:
        #       1. make a list including the tuples of (i, j) for the empty tiles, where i = 0, 1, 2 and j = 0, 1, 2.
        #          The top-left tile corresponds to (0, 0) while the bottom-right does to (2, 2).
        #       2. make a rondom choice of a tuple out of the list.
        #       3. For that place(or tile) chosen randomly in the step 2, perform a Monte Carlo Simulation up until the game is over.
        #       4. Repeat the Monte Carlo Simulation in the step 3 up to a certain number of times.
        #       5. Calculate the probability distribution for AI to win or to lose or to be tie.
        #       6. Repeat the steps from 2 to 5 for another randomly chosen place.
        #       7. First of all, find all the cases in which AI can win, and then choose the place where AI is most probable to win. 
        #       8. If step #7 is not fulfilled, find all the cases in which AI can make a tie, and then choose the place where AI is most probable to make a tie.  #       9. If step $8 is not fulfilled, find all the case in which AI can lose, and then choose the place AI is leas probable to lose.
        #       6. Return the result as the ai_move ro the optimal action for AI.
        import random
        
        matrix = self.board.state
        tiles_empty = []
        
        for i, row in enumerate(matrix):
            for j, element in enumerate(row):
                if element == 0:
                    tiles_empty.append((i, j))
        
        ai_move = random.choice(tiles_empty)
        
        return ai_move
