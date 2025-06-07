# minimax.py for Tic-Tac-Toe Game!
# Returns the optimal action for the current player, AI_Agent, on the board.

# We need know which is the ai.agent, X or O.
# if ai.agent = 1, we need to choose the move that maximizes the score as high as possible.
# if ai.agent = -1, the opposite: minimize the score.

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


import sys, time, pygame, random

from player import Player
from board import Board
from tiles import Tiles
from mouse import Mouse
from settings import Settings

# 
pygame.init()

# Create a Settings class
settings = Settings()   

# Create a screen and caption on it.
screen = pygame.display.set_mode(settings.screen_size)
pygame.display.set_caption('Tic Tac Toe Game')   

# Create Player class instances. 
user = Player(agent=None, on_turn=False) # agent=None, on_turn=False
ai = Player(agent=None, on_turn=False) # agent=None, on_turn=False   
# user can choose an agent from "O" or "X": Set as ai.agent = None as default value
# ai.on_turn=False: user makes the first move, then AI takes the next.

# Create an instance of the Board class.
board = Board()
# Create an instance of the Tiles class.
tiles = Tiles(screen) # Here self.screen attr required!
# Create an instance of the Mouse class.
mouse = Mouse()

# Create a clss variable
buttons_intro = [None, None] # includes two pygame.Rect objects.


# Fill the screen with black-color.
screen.fill(settings.bg_color)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(f'exit button clicked')
            time.sleep(1)
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                print(f'Q key clicked')
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(f'mouse clicked') 

    pygame.display.flip()

pygame.quit()        

def who_plays(self):
    """
    Determins who is the winner
    """
    if self.user.on_turn and not self.ai.on_turn:
        return self.user.agent 
    elif self.ai.on_turn and not self.user.on_turn:
        return self.ai.agent
    else:
        return None

state = [[1, -1, 0],[1, -1,1],[-1, 0, 1]]

tiles_empty = []            

for i, row in enumerate(state):
    for j, col in enumerate(row):
        print(f' {col} ', end="")
        if col == 0:
            tiles_empty.append((i, j))
    print()
print(random.choice(tiles_empty))



 