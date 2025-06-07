# board.py for Tic-Tac-Toe Game!
from settings import Settings

# Create class Board.
class Board:
    # Class for Tic-Tac-Toe Board

    def __init__(self):
        self.settings = Settings()
        # Set initial values for class variables
        self.initialize()
        
    # Create the initial state of the board
    def initialize(self):
        # Returns starting state of the board.
        self.state = [[0, 0, 0],[0, 0, 0],[0, 0, 0]] # initial_state is [[0,0,0],[0,0,0],[0,0,0]]
        self.state_str = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]] # This is 3X3 matrix in strings.
        self.count_filled = 0 # Create instance variables # integers in range(10)
        self.sum_list = [] # sum_list: includes sums of each row, column and diagonal.
        self.game_over = False 

    def convert_to_str(self, state_num):
        # Converts the elements of the state from integers to strings. 
        # Define a tabular chart for the conversion.
        tabular_chart = {
            1 : "X",
            0 : " ",
            -1 : "O"
        }
        # Convert state_num into state_str.
        for i in range(len(state_num)):
            for j in range(len(state_num)):
                self.state_str[i][j] = tabular_chart[state_num[i][j]]
                    
        return self.state_str     
 
    def update(self, state_num):
        # Extracts some information out of the state of the board, and save them as integers.  
        # Update self.count_filled.
        new_count_filled = 0
        for i, row in enumerate(state_num):
            for j, element in enumerate(row):
                self.state[i][j] = element # Update the value at (i, j) on board
                if element in (self.settings.O, self.settings.X):
                    new_count_filled += 1
        self.count_filled = new_count_filled
        
        # Update the state_str
        self.state_str = self.convert_to_str(state_num) 
        
        # Define a list whose entities represents the sum of each row or column or diagonal of the 3x3 matrix defined above.
        # as like [ sum(row[1]), sum(row[2]), sum(row[3]), col[1], col[2], col[3], diagonal[1], diagonal[2]].
        # If there can be found 3 or -3 in the list, the game is over.
        # If there is not either 3 nor -3, no one wins the game so that the game continues.
        # If there is no room to fill, the game is over with no winner.
        new_sum = []
        # Add sums of three rows into sum_list.
        row_sums = [sum(row) for row in self.state]
        new_sum.extend(row_sums)
        # Add sums of three columns into sum_list.
        column_sums = [sum(col) for col in zip(*self.state)]
        new_sum.extend(column_sums)
        # Add the sum of the diagonal into sum_list.    
        new_sum.append(sum(self.state[i][i] for i in range(3)))
        # Add the sum of the second diagonal into sum_list.
        new_sum.append(sum(self.state[i][2-i] for i in range(3)))              
        
        self.sum_list = list(new_sum)

        # Check if the game is over
        # from self.count_filled that stands for the number of tiles filled.
        if self.count_filled in {0, 1, 2, 3, 4}:
            self.game_over = False
        elif self.count_filled == 9:
            self.game_over = True
        elif self.count_filled >= 5:
            if -3 in self.sum_list or 3 in self.sum_list:
                self.game_over = True
            else:
                self.game_over = False