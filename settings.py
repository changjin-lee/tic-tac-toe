# settings.py for Tic-Tac-Toe Game!

import sys, os

# # Includes the fonts folder in the list of sys.path.
fonts_path = os.path.join(os.getcwd(), 'fonts')
sys.path.append(fonts_path)

import pygame

class Settings:
    """A class to stor all settings for Tic-Tac-Toe Game"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings.
        self.screen_width = 600
        self.screen_height = 400
        self.screen_size = (600, 400)
        self.bg_color = (0, 0, 0) # black
        self.obj_color = (255, 255, 255) # white
    
        # Fonts settings for images on the board.
        self.Font_Medium = pygame.font.Font('fonts/OpenSans-Regular.ttf', 28)
        self.Font_Large = pygame.font.Font('fonts/OpenSans-Regular.ttf', 40)
        self.Font_OX = pygame.font.Font('fonts/OpenSans-Regular.ttf', 60)
        
        # Tiles settings for OX images on the board.
        # square tile with the side's width of 80.
        self.tile_size = 80 
        # tile_origin: xy-coordinates of the left top corner of a tile
        self.tile_origin = (self.screen_width / 2 - (1.5 * self.tile_size),
                            self.screen_height / 2 - (1.5 * self.tile_size))
        
        # Define symbols that represent the agents.
        self.X = 1
        self.O = -1
        self.EMPTY = 0 
        # Create class variable to save all states of the board
        # self.initial_archive = {'user': ' '}
        self.initial_archive = dict.fromkeys(x for x in range(1,10))
        # self.initial_archive.extend(self.dict_items)
        # Create class variable below shared by all instances
        self.initial_state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] 
        self.initial_state_str = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.initial_state_rect = [[None, None, None], [None, None, None], [None, None, None]]
        
if __name__ == '__main__':
    test = Settings()
    print(test.initial_archive)
    print(test.dict_items)
    print(test.initial_archive)