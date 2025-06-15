# axiomatic.py

class ModelAxiomatic:
    """A class Model includes several models to calculate the optimal action for AI."""
    def __init__(self):
        pass

    # AI model: Axiomatic rule-based algorithm
    def minimax(self):
        """
        Returns the optimal action for the current player, AI_Agent, on the board.
        """
        # We need know which is the ai.agent, X or O.
        # if ai.agent = 1, or if ai.agent_str = "X", we maximize the score as high as possible.
        # if ai.agent = -1, or if ai.agent_str = "O", the opposite: minimize the score.
        
        # Execute board.update(board.state) to get matrix, count_filled, sum_list from board.update(board.state)
        # Find the number of tiles filled on board: count_filled from quantify_state(board)
        #
        # --------------------
        # Axiomatic Strategy: 
        # --------------------
        #   - Set up Axiomatic Rules:
        #   1. The top priority rule is to check if AI could win. If possible, occupy that place.
        #   2. If rule #1 is not fulfilled, check if the user could win for the next move. If possible, occupy that place.
        #   3. If rule #2 is not fulfilled, check if there is a place where AI could make multiple chances to win in several directions at its next turn. 
        #      If there are many, occupy a place from random.choice. 
        #   4. If rule #3 is not fulfilled, check if there is a place where AI could make multiple chances to win in the several direction at user's next turn.
        #      If there are many, occupy a place from random.choice.
        #   5. If rule #4 is not fulfilled, check if there is a place from where the empty tiles can be filled to make a win. 
        #      Count how many ways to win can be constructed from that place. Occupy the place which has the biggest number of ways to win.
        #   6. If rule #5 is not fulfilled, check if there is a place from where AI can fill the empty tiles to make a win.
        #      Count how many ways for AI to win can be constructed from that place. Occupy the place which has the biggest number of ways to win. 
        #      This is the strategy to make a Tie or not to lose.
        #
        #   - Make a list of empty tiles:
        #       1. make a list including the tuples of (i, j) for the empty tiles, where i = 0, 1, 2 and j = 0, 1, 2.
        #          The top-left tile corresponds to (0, 0) while the bottom-right does to (2, 2).
        #   - Apply the axiomatic rules:
        #       1. Any rule is fulfilled, return the result as the ai_move.
        #   - In case no rule fulfilled:
        #       1. make a random choice of a tuple out of the list of empty tiles.
        #       2. return the result as the ai_move.
        import random
        
        matrix = self.board.state
        tiles_empty = []
        
        for i, row in enumerate(matrix):
            for j, element in enumerate(row):
                if element == 0:
                    tiles_empty.append((i, j))
        
        ai_move = random.choice(tiles_empty)
        return ai_move
        # return (2,2)