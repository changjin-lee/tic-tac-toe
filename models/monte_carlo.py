# monte_carlo.py
# performs some artificial experiments in a computer, or Monte Carlo Simulations, 
# to see what will happen if AI occupies a certain empty place(or tile).

# Import the MCBoard class that is just the same as the class Board.
# Inside a package, relative path is valid.
from .mc_board import MCBoard

import random, copy, collections, statistics
   
class MonteCarlo:
    """A class represents the Monte Carlo simulation, which generates a possible outcome based on randomness."""
    # def __init__(self, tiles_empty, board_state, user_agent):
    def __init__(self, board_state, user_agent):
        # Get information about the board and the user.
        self.board_state = board_state
        self.user_agent = user_agent
        # Find self.tiles_empty from self.board_state.
        self.tiles_empty = self.find_tiles_empty()
        # self.ai_agent = -1 if self.user_agent == 1 else 1 # user_agent is 1 or -1.
        self.ai_agent = - self.user_agent # user_agent is 1 or -1.
        # Initialize the ai_move: This is the goal for this Monte Carlo simulation to achieve.
        self.ai_move = (None, None) 
        
        # Initialize local variables
        self.initialize()         
        # Perform Monte Carlo simulation to find self.ai_move.
        self.perform_mc_simulation()
    
    def initialize(self):
        # Make an instance of the class of MCBoard, on which we perform a Monte Carlo simulation.
        self.mc_board = MCBoard() 
        # Update mc_board by self.board_state.
        self.mc_board.update(self.board_state)
        # Set the sampling size or the upper bound on how many sample to be collected for a round of MC simulation.
        self.SAMPLE_SIZE = 30 
        # Set the upper bound on how many MC-rounds to be run for the MC Simulation.
        self.ITERATION_SIZE = 10
        # Create vaiables to save the data obtained from many rounds of the Monte Carlo Simulations.
        # At an intermediate stage, it has the form of {(0, 0): {1: [ ... ], 0: [ ... ], -1: [ ... ]}, ... } 
        # where each [ ... ] has integers 1, 0, -1 as many as self.ITERATION_SIZE.
        # Finally, [ ... ] turns into a frequency number and then the probability for each player to win.
        self.data = { key: {1: {}, 0: {}, -1: {}} for key in self.tiles_empty} 
        self.data_sorted = {} # sorted self.data according to the probability.
        # self.game_record = [] # Each game record can be stored: [(1, 1), (0, 0), (2, 0), (0, 2), (0, 1), ...].

    def find_tiles_empty(self):
        # matrix = self.board_state
        matrix = self.board_state
        tiles_empty = []
        
        for i, row in enumerate(matrix):
            for j, element in enumerate(row):
                if element == 0:
                    tiles_empty.append((i, j))
        return tiles_empty
        
    # Roll a dice and put a possible ai_move on the board and check if the game is over with the move added. 
    # If yes, return the winner. If not, roll a dice once again to put a user_move and check if the game is over with the move added. 
    # If not, roll a dice once again to put a ai_move until the end of the game.
    def generate_mc_data(self):  
        """ Performs a single round of MC simulation to generate self.mc_data.
            in the from of self.mc_data: {(0,0): {1: 3, 0: 2, -1: 5}, (0, 1): {1: 4, 0: 2, -1: 4}, ... }."""     
        # Create a completely independent list from self.board_state using copy.deepcopy().
        self.mc_state = copy.deepcopy(self.board_state)
        # Create a local variable completely independent from self.tiles_empty using copy.deepcopy().  
        self.mc_tiles_empty = copy.deepcopy(self.tiles_empty)
        # Create a tuple of the coordinates of a tile chosen randomly for AI's move.
        self.mc_tile_chosen = () 
        # Make an empty list to save the winner for each game.
        self.mc_winners = [] # In this list, we save the winner from {1, o, -1} for each game as many as upto self.SAMPLE_SIZE.
        # From self.mc_winners = [1, 0, -1, -1, -1, 0, 1, 1, -1, -1], we count the frequencies for 1, 0, -1, 
        # and then save them into a dictionary below as corresponding values to the keys 1, 0, -1 as {1: 3, 0: 2, -1: 5}.
        # Save it as self.mc_winners_frequency below.
        self.mc_winners_frequency = {} # {1: 3, 0: 2, -1: 5} The keywords{1, 0, -1} stand for the winners of a game: X, Tie, O respectively.
        # Save self.mc_winners_frequencies in corresponding winner's list as below.
        # This is the final result of a single round of the MC simulation.
        self.mc_data = {} # {(0,0): {1: 3, 0: 2, -1: 5}, (0, 1): {1: 4, 0: 2, -1: 4}, ... } 
        
        while len(self.mc_tiles_empty) > 0 and self.ai_move == (None, None):
            # Pick up a tile for AI to occupy, and then, for that choice, calculate the probability for AI to win.
            self.mc_tile_chosen = random.choice(self.mc_tiles_empty)
            # Remove the tile chosen by AI.
            self.mc_tiles_empty.remove(self.mc_tile_chosen) 
            # Apply ai_move on the board at self.mc_tile_chosen: Mark ai_agent on the tile_chosen.
            (m, n) = self.mc_tile_chosen
            self.mc_state[m][n] = self.ai_agent
            # Update the mc_board to make it reflect the updated self.mc_state.
            self.mc_board.update(self.mc_state)
            # Set a flag for checking if self.mc_data has been determined or not.
            self.mc_data_found = False 
            
            # Fortunately, the tile_chosen can make AI be the winner, then take it as the optimal action for AI.
            # Just take it as ai_move and break the while loop. 
            # Of course, there could be more tiles to make AI win. Let consider such a case later. 
            if self.mc_board.game_over:
                # Since the tile_chosen make AI win, set the winner of each MC simulation be AI.
                self.mc_winners = [self.ai_agent for sample in range(self.SAMPLE_SIZE)]
                # Convert self.mc_winners into a dict in frequency.
                self.convert_into_freqency()
                # Save the self.mc_winners_frequency in the dictionary of self.mc_data.
                self.mc_data[self.mc_tile_chosen] = self.mc_winners_frequency 
                # Reset variables in this function and get ready to perform another MC simulation.
                self.reset()
                # Inform self.mc_data has been determined by setting the flag self.mc_data_found as True.
                self.mc_data_found = True
            
            elif self.user_win():
                # This is the second best choice for AI, which prevents the user from being the winner in the following user's turn.
                # Therefore, if I put AI in the self.mc_winners on purpose, which will increase the probability for AI to win at this position.
                # On the other hand, if I put USER in the self.winners, which will increase the probabiity for USER to win at this position.
                # Investgating the performances of the two cases above, putting AI in the self.winners performs better for AI.
                # In case that we have a chance to win at a position and also to lose at another position, 
                # we need to set up a rule which tells AI to choose the better postion to win first rather than to prevent USER from winning.
                self.mc_winners = [self.ai_agent for sample in range(self.SAMPLE_SIZE)]   
                # Set the last number of self.mc_winners as 0, which means game_tie and decreases the frequency for AI to win just by one. 
                # This make AI choose the position to win first rather thant to prevent USER from winning. 
                self.mc_winners[-1] = 0  
                # Convert self.mc_winners into a dict in frequency.
                self.convert_into_freqency()
                # Save the self.mc_winners_frequency in the data dictionary
                self.mc_data[self.mc_tile_chosen] = self.mc_winners_frequency     
                self.reset()
                self.mc_data_found = True     
                         
            # In case that the tile_chosen doesn't make AI immediately win the game, keep proceding MC simulation with the tiles remained.
            # Perform Monte Carlo simulation to generate a possible random state of the game with the tiles remained.
            # Since AI has already picked up one empty tile, now it is user's turn.
            elif self.ai_move == (None, None) and not self.mc_data_found:
                for sample in range(self.SAMPLE_SIZE):
                    # Create local variables using copy.deepcopy().
                    mc_matrix = copy.deepcopy(self.mc_state)
                    mc_tiles_empty = copy.deepcopy(self.mc_tiles_empty)
                    mc_board = self.mc_board # deepcopy makes an error here. I don't know why and what it means.
                    mc_board.update(mc_matrix)
                    mc_winner = None # This takes only one number in the while loop below.
                    while not mc_board.game_over:
                        for tile_count in range(len(mc_tiles_empty)):
                            if tile_count % 2 == 0: # Check if it is the user's turn.
                                mc_tile_occupied = random.choice(mc_tiles_empty)
                                mc_tiles_empty.remove(mc_tile_occupied)
                                # Apply user_move to the board: Mark user_agent on the mc_board.
                                i, j = mc_tile_occupied
                                mc_matrix[i][j] = self.user_agent
                                mc_board.update(mc_matrix)
                                if mc_board.count_filled == 9 and mc_board.game_tie:
                                    mc_winner = 0
                                    # Save the winner for each sample game into self.mc_winners.
                                    self.mc_winners.append(mc_winner) 
                                    break
                                elif mc_board.game_over:
                                    mc_winner = self.user_agent
                                    # Save the winner for each sample game into self.mc_winners.
                                    self.mc_winners.append(mc_winner)                             
                                    break
                            elif tile_count % 2 == 1: # Check if it is AI's turn.
                                mc_tile_occupied = random.choice(mc_tiles_empty)
                                mc_tiles_empty.remove(mc_tile_occupied)
                                # Apply ai_move to the board: Mark ai_agent on the board.
                                i, j = mc_tile_occupied
                                mc_matrix[i][j] = self.ai_agent
                                mc_board.update(mc_matrix)   
                                if mc_board.game_over:
                                    mc_winner = self.ai_agent
                                    # Save the winner for each sample game into self.mc_winners.
                                    self.mc_winners.append(mc_winner)
                                    break
                        
                # Convert self.mc_winners into the list of self.mc_winners_frequency.
                # For example, self.mc_winners: [1, 1, 0, 0, -1, 0, 0, 1, -1, -1]
                # self.convert_into_frequency() generates a dict of the form of {1: 3, 0: 4, -1: 3},
                # where the keys of 1, 0, -1 stand for the winners of a game: X, Tie, O respectively.
                # Convert self.mc_winners into a dict in frequency as given above.
                self.convert_into_freqency()
                # Save the self.mc_winners_frequency in the dict of self.mc_data: {(0, 1): {1: 3, 0: 4, -1: 3}, ... }
                self.mc_data[self.mc_tile_chosen] = self.mc_winners_frequency
                # Reset self.mc_winners, self.mc_winners_frequency.
                self.reset()
                
                # The size of self.mc_winners is as same as self.SAMPLE_SIZE.
                # The size of sample shouldn't be too big because of the limitation of the memory.
            # print(self.mc_data)
                
    def reset(self):
        self.mc_winners = []
        self.mc_winners_frequency = {}
        
    def convert_into_freqency(self):
        """Obtain the frequency of the same element in the list of self.mc_winners."""
        element_counts = collections.Counter(self.mc_winners)
        mc_winners_frequency = {}
        
        for key in [1, 0, -1]:
            mc_winners_frequency[key] = element_counts.get(key, 0)
        
        # print(mc_winners_frequency)
        self.mc_winners_frequency = mc_winners_frequency
        
    def user_win(self):
        """Check if mc_tile_chosen makes the user win."""
        (m, n) = self.mc_tile_chosen
        # Temporarily change the value of self.mc_state[m][n] just for a check from self.ai-agent to self.user_agent.
        self.mc_state[m][n] = self.user_agent
        # print(self.mc_state)
        # Update the mc_board to make it reflect the new self.mc_state.
        self.mc_board.update(self.mc_state)
        if 3 * self.user_agent in self.mc_board.sum_list:
            # print(f'mc_tile_chosen makes user win: {self.mc_board.sum_list}')
            # Recover the value of self.mc_state and self.mc_board before finishing this check.
            self.mc_state[m][n] = self.ai_agent
            self.mc_board.update(self.mc_state)
            return True 
    
    def perform_mc_simulation(self):
        """ performs several rounds of MC_simulations to get a set of self.mc_data, 
        and then analyze it using some modules such as statistics, scipy.stats, numpy, pandas."""
        # MonteCarlo calculates how frequently a player to win or to make a tie for a certain number of MC simulations: given as SAMPLE_SIZE = 10. 
        # The result of MC simulation data, mc.data, has the form of a dictionary: for each empty tile with (i, j) as a key and its value with {1: 3, 0: 2, -1: 5}.
        # For example, when the board_state is [[-1, 1, 0], [1, -1, 0], [1, 0, 0]], the result of MC simulation turns out to be: 
        # mc_data = {(0, 2): {1: 2, 0: 4, -1: 4}, (2, 2): {1: 0, 0: 0, -1: 10}, (2, 1): {1: 0, 0: 0, -1: 10}, (1, 2): {1: 0, 0: 0, -1: 10}}        
        # We need to collect more mc.data to make a set of data for each empty tile, which can be used for statistical analysis.
        # mc_data = {(0, 2): {1: 3, 0: 3, -1: 4}, (1, 2): {1: 0, 0: 0, -1: 10}, (2, 2): {1: 0, 0: 0, -1: 10}, (2, 1): {1: 0, 0: 0, -1: 10}}
        # mc_data = {(0, 2): {1: 5, 0: 3, -1: 2}, (1, 2): {1: 0, 0: 0, -1: 10}, (2, 2): {1: 0, 0: 0, -1: 10}, (2, 1): {1: 0, 0: 0, -1: 10}}
        # mc_data = {(2, 2): {1: 0, 0: 0, -1: 10}, (1, 2): {1: 0, 0: 0, -1: 10}, (2, 1): {1: 0, 0: 0, -1: 10}, (0, 2): {1: 0, 0: 0, -1: 10}}
        # mc_data = {(1, 2): {1: 3, 0: 3, -1: 4}, (2, 2): {1: 0, 0: 0, -1: 10}, (2, 1): {1: 0, 0: 0, -1: 10}, (0, 2): {1: 0, 0: 0, -1: 10}}
        # For example, collect data for (0, 2) empty tile, which tell us how probable for AI to win, for the user to win, or to be a tie.
        # Let us collect them: {(0, 2): {1: 2, 0: 4, -1: 4}, {1: 3, 0: 3, -1: 4}, {1: 5, 0: 3, -1: 2}, {1: 0, 0: 0, -1: 10}, {1: 0, 0: 0, -1: 10}}
        # where we can collect the frequencies for each key 1, 0, -1 as three corresponding lists as below:
        # self.data_temp: {(0, 2): {1: [2, 3, 5, 0, 0], 0: [4, 3, 3, 0, 0], -1: [4, 4, 2, 10, 10]}
        # Now we can use a tool for statistical analysis to find the probability for each result 1, 0, -1 to occur.
        # The built-in module statistics provides basic tools for statistics.
        # The third party modules, numpy, pandas, scipy.stats can be used for the analysis of such as the list [2, 3, 5, 0, 0] for 1 above.
        # sample_mean = np.mean(data), 
        # sample_standard deviation = np.std(data),
        # technical statistics : scipy.stats.describe(data),
        # and so on.          

        while self.ai_move == (None, None):
            # Temporarily, self.mc_winners_frequency goes into the values of self.data_temp below.
            self.data_temp = { key: {1: [], 0: [], -1: []} for key in self.tiles_empty} 
            
            # Set a flag to check if the self.ai_move is found.
            ai_move_found = False
            
            # Performs several rounds of MC simulations upto self.ITERATION_SIZE.
            for mc_round_index in range(self.ITERATION_SIZE):
                # Generate self.mc_data: {(0, 1): {1: 3, 0: 4, -1: 3}, ... }
                self.generate_mc_data()
                # Check if self.ai_move has been determined axiomatically before performing Monte Carlo simulations.
                # If positive, break this for loop
                if self.ai_move != (None, None):
                    ai_move_found = True
                    break
                # print(self.mc_data)
                # print(self.tiles_empty)
                # print(self.ai_move)

                for tile in self.tiles_empty:
                    for i in [1, 0, -1]:
                        temp = self.mc_data[tile][i] if tile in self.tiles_empty else 0
                        self.data_temp[tile][i].append(temp)
            # Display the result of self.data.
            # print(self.data_temp)
            
            # Check if self.ai_move has been found. If positive, break this while loop.
            if ai_move_found:
                break
            
            # Perform statistical analysis on self.data_sorted.            
            for tile in self.tiles_empty:
                for i in [1, 0, -1]:
                    mean = statistics.mean(self.data_temp[tile][i])/self.SAMPLE_SIZE
                    # stdev = statistics.stdev(self.data_temp[tile][i])/self.SAMPLE_SIZE
                    self.data[tile][i] = round(mean, 3)
                    # self.data[tile][i] = (round(mean, 2), round(stdev, 2))
            # Display the result of mean values.
            # print(self.data)
            
            # Find the optimal actions for AI
            self.find_optimal_action()

        
    def find_optimal_action(self):
        """Determines which place is the optimal action for AI."""
        while self.ai_move == (None, None):
            data_ai_sorted = dict(sorted(self.data.items(), key = lambda item: item[1][self.ai_agent], reverse=True))
            data_user_sorted = dict(sorted(self.data.items(), key = lambda item: item[1][self.user_agent], reverse=True))
            data_tie_sorted = dict(sorted(self.data.items(), key = lambda item: item[1][0], reverse=True))
            # print(data_ai_sorted)
            # print(data_user_sorted)
            # print(data_tie_sorted)
            
            key_ai = list(data_ai_sorted.keys())[0]
            mean_ai = data_ai_sorted[key_ai][self.ai_agent]
            key_user = list(data_user_sorted.keys())[0]
            mean_user = data_user_sorted[key_user][self.user_agent]
            key_tie = list(data_tie_sorted.keys())[0]
            mean_tie = data_tie_sorted[key_tie][0] # 0 stands for game_tie.
            
            # Select which rule or strategy to use to determine the optimal action for AI.
            # The simple one is to choose the most probable position for any player or a game_tie.
            # Find more strategies for the better performance.
            mean_max = max(mean_ai, mean_user, mean_tie)
            
            if mean_max == mean_ai:
                self.mc_ai_move = key_ai
            elif mean_max == mean_user:
                self.mc_ai_move = key_user
            elif mean_max == mean_tie:
                self.mc_ai_move = key_user
            else:
                break
                    
            self.ai_move = self.mc_ai_move
            
            # return self.ai_move
            # print(f'sorted: {self.data_sorted}')
            # print(list(self.data_sorted.keys())[0])
    
        
def main():
    mc = MonteCarlo(board_state=[[-1, 1, 0], [1, -1, 0], [1, 0, 0]], user_agent=1)
    # mc.generate_mc_data()
    
    # Check if the game is over and who is the winner.
    print(mc.data)       
    
    mc.perform_mc_simulation()
    
    print(mc.ai_move)

if __name__ == '__main__':
    # Import a Parent class from a higher folder
    
    import sys, os
    
    current_dir = os.path.dirname(__file__)
    sys.path.append(current_dir)
    main_dir = os.path.dirname(current_dir)
    sys.path.append(main_dir)
    models_path = os.path.join(main_dir, 'models')
    sys.path.append(models_path)
    fonts_path = os.path.join(main_dir, 'fonts')
    sys.path.append(fonts_path)
    
    main()
        