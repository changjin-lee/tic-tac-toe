# models.py includes several models to calculate the optimal action for AI.

# Import several models
from .monte_carlo import MonteCarlo
from .simple_random import SimpleRandom

class ModelRandom:
    """A class Model includes several models to calculate the optimal action for AI."""
    def __init__(self, board_state, user_agent):
        self.board_state = board_state # board is an instance of the Board class.
        self.user_agent = user_agent

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
        # ---------------------------------------
        # Model Random: Monte Carlo Strategy: 
        # ---------------------------------------
        #   - choose any empty tile at random:
        #       1. make a list of tuples: (i, j) for the coordinates of an empty tile, where i = 0, 1, 2 and j = 0, 1, 2.
        #          The top-left tile corresponds to (0, 0) while the bottom-right does to (2, 2).
        #       2. make a rondom choice of a tuple out of the list.
        #       3. For that place(or tile) chosen randomly in the step 2, perform a Monte Carlo Simulation up until the game is over.
        #       4. Repeat the Monte Carlo Simulation in the step 3 up to a certain number of times.
        #       5. Calculate the probability distribution for AI to win or to lose or to make a tie.
        #       6. Repeat the steps from 2 to 5 for another randomly chosen place in the list of empty tiles not taken.
        #       7. First of all, find all the cases in which AI can win, and then choose the place where AI is most probable to win. 
        #       8. If step #7 is not fulfilled, find all the cases in which AI can make a tie, and then choose the place where AI is most probable to make a tie.  #       9. If step $8 is not fulfilled, find all the case in which AI can lose, and then choose the place AI is least probable to lose.
        #       10. Return the result as the ai_move or the optimal action for AI.

        # -------------------------------
        # 1. Model Random: Monte Carlo
        # -------------------------------
        # Make an instance of the Model of Monte Carlo to find the optimal action for AI.
        # Transfer the board_state and user_agent to the MonteCarlo. For example, 
        # self.board_state = [[-1, 1, 0], [1, -1, 0], [1, 0, 0]] and self.user_agent = 1
        mc = MonteCarlo(self.board_state, self.user_agent)
        # MonteCarlo calculate how frequently a player to win or to make a tie for a certain number of random simulations: given as SAMPLE_SIZE = 10. 
        # The result of MC simulation data, mc.data, has the form of a dictionary: for each empty tile with (i, j) as a key and its value with {1: 3, 0: 2, -1: 5}.
        # For example: 
        # mc.data = {(0, 2): {1: 2, 0: 4, -1: 4}, (2, 2): {1: 0, 0: 0, -1: 10}, (2, 1): {1: 0, 0: 0, -1: 10}, (1, 2): {1: 0, 0: 0, -1: 10}}.     
       
        # To see the result of Monte Carlo simulation, print its result saved in self.ai_move.
        print(mc.ai_move)
        return mc.ai_move
        

        # -----------------------------    
        # 2. Model Random: Simple Random
        # -----------------------------
        # Makes an instance of the Model of Simple Random to find the optimal action for AI.
        # No sophistcated strategy is adopted but just a simple random choice.
        # sr = SimpleRandom(self.board_state, self.user_agent)
        
        # # To see the result of Monte Carlo simulation, print its result saved as self.ai_move.
        # print(sr.ai_move)
        # return sr.ai_move
        
 
def main():
    model = ModelRandom(board_state=[[-1, 1, 0], [1, -1, 0], [1, 0, 0]], user_agent=1)
    # Calculate the optimal action for AI
    model.minimax()
    
if __name__ == '__main__':
    # Import a Parent class from a higher folder.
    import sys, os
    from pathlib import Path
    
    os.chdir(os.path.dirname(__file__))
    
    current_dir = Path.cwd()
    # sys.path.append(current_dir)
    parent_dir = current_dir.parent
    models_path = parent_dir / 'models'
    sys.path.append(models_path)
    fonts_path = parent_dir / 'fonts'
    sys.path.append(fonts_path)
    
    # from models import *

    main()
