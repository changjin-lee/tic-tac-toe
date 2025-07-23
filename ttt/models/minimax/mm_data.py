# mm_data.py
# defind a data class for the outcomes of the minimax algorithm.

import random

class MMData:
    """This class defines a data class for the outcome of the minimax algorithm,
    and several methods to extract information from the outcome."""
    
    def __init__(self, tiles_empty):
        self.outcome = {key: 0 for key in tiles_empty} # tiles_empty is a list of tuples: [(i, j), ...].
        self.outcome_sorted = {}
        self.ai_move = (None, None)
                
    def generate_outcome(self, maximizer=True):
        #
        if maximizer:
            # For maximizer, sorted in descending order. 
            self.outcome_sorted = dict(sorted(self.outcome.items(), key= lambda item: item[1] in self.outcome.items(), reverse=True)) 
        else:
            # For minimizer, sorted in ascending order.
            self.outcome_sorted = dict(sorted(self.outcome.items(), key= lambda item: item[1] in self.outcome.items())) 
        
        # Collect the keys that share the same value in self.outcome_sorted.
        sorted_by_value = {}

        for key, value in self.outcome_sorted.items():
            if value in sorted_by_value:
                sorted_by_value[value].append(key)
            else:
                sorted_by_value[value] = [key]

        self.ai_move = random.choice(list(sorted_by_value.values())[0])
    