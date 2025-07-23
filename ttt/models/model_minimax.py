# model_minimax.py
# Implement the well-known algorithm to find the optimal action for AI.

# Import model minimax from the package minimax.
from minimax import *

class ModelMinimax:
    """Returns the optimal action for AI obtained by the well-known minimax algorithm in game thoery, 
    which not only maximize the probability for AI to win but also to minimize the opponent's probability to win.
    In fact, this model chooses the move which gives the maximum score for AI
    among the minima offered by the opponent for all possible moves."""
    
    def __init__(self, board_state, user_agent):
        self.board_state = board_state
        self.user_agent = user_agent
    
    # AI model: minimax algorithm.
    def runs(self):
        """
        Returns the optimal action for the current player, AI_Agent, on the board.
        """
        pass
    
        # We need know which is the ai.agent, X or O.
        # if ai.agent = 1, or if ai.agent_str = "X", we maximize the score as high as possible.
        # if ai.agent = -1, or if ai.agent_str = "O", the opposite: minimize the score.
        
        # Execute board.update(board.state) to get matrix, count_filled, sum_list from board.update(board.state)
        # Find the number of tiles filled on board: count_filled from board.update(board.state)
        
        # ----------------------------------
        # Model Strategy: Minimax Algorithm
        # ---------------------------------- 
        # - Minimax Algorithm explores all possible outcomes in a game tree,
        #   and evaluates them according to the rules implemented. 
        # - Therefore, it is not a model that depends on the randomness such as a Monte Carlo Simulation Model.
        # - Key components of minimax algorithm: Maximizer, Minimizer, Evaluation function.
        #   1. Maximizer: player 1
        #   2. Minimizer: player -1
        #   3. Evaluation function(or winner function(or score function) or utility function): 
        #     {player 1 wins: 1, player -1 wins: -1, game tie: 0}.
        # - Steps of Minimax: 1. Root node/Base node/Leaf node, 2. Recursive Exploration, 3. Backtracking.
        
        # The source codes of minimax algorithm below comes from the course of CS50: AI at Havard university.
        # I kept its logic but modified some lines of the codes: variable's names and evaluation function and so on.
        # ----------------------------------------------------
        # - Pseudo Code for Minimax Algorithm: With Pruning
        # ----------------------------------------------------
        # def minimax(self, state, alpha, beta, maximizer):
        #   """
        #   Returns the optimal action for the current player on the board 
        #   using the minimax algorithm with alpha-beta pruning.
        #   """
        # 
        #   actions = self.find_possible_actions(state)
        #   if state is game_over:
        #       return None

        #   if maximizer:
        #       v = -math.inf
        #       optimal_action = None
        #       for action in actions:
        #           child_state = self.find_child_state(state, action, maximizer=True)
        #           new_value = self.min_value(child_state, -math.inf, math.inf)
        #           if new_value > v:
        #               v = new_value
        #               optimal_action = action
        #       return optimal_action
        
        #   else:
        #       v = math.inf
        #       optimal_action = None
        #       for action in actions:
        #           child_state = self.find_child_state(state, action, maximizer=False)
        #           new_value = self.max_value(child_state, -math.inf, math.inf)
        #           if new_value < v:
        #               v = new_value
        #               optimal_action = action
        #       return optimal_action
        # ---------------------------------------------
        # Code Ref.: 
        # - Source codes from CS50AI at Havard Univ.
        
        # Make an instance of the Model of Minimax to find the optimal action for AI.
        # Transfer the board_state and user_agent to the Minimax. For example, 
        # self.board_state = [[-1, 1, 0], [1, -1, 0], [1, 0, 0]] and self.user_agent = 1
        mm = Minimax(self.board_state, self.user_agent)
        mm.perform_minimax()
        
        #-----------------------
        # Model Minimax: Result
        # ----------------------
        # To see the result of Minimax algorithm, print its result saved in self.ai_move.
        print(mm.ai_move)
        return mm.ai_move     
        # [[0, 0, -1], [0, 1, 1], [0, 0, 0]]
        
def main():
    model = ModelMinimax(board_state=[[-1, -1, 1], [0, 1, 0], [0, 0, 1]], user_agent=1)
    # Calculate the optimal action for AI
    model.runs()
    
if __name__ == '__main__':
    # Import a Parent class from a higher folder.
    import sys, os
    from pathlib import Path
    
    current_dir = os.path.dirname(__file__)
    sys.path.append(current_dir)
    parent_dir = os.path.dirname(current_dir)
    sys.path.append(parent_dir)
    models_path = os.path.join(parent_dir, 'models')
    sys.path.append(models_path)
    fonts_path = os.path.join(parent_dir, 'fonts')
    sys.path.append(fonts_path)
    minimax_path = os.path.join(models_path, 'minimax')
    sys.path.append(minimax_path)
    
    # from models import *

    # main()