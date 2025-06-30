# tiles.py for Tic-Tac-Toe Game!

from settings import Settings

import pygame

class Tiles:
    """A class to manage the tiles on board."""

    def __init__(self, game_screen):
        """Initialize the tiles and set their positions on board."""
        self.settings = Settings()
        self.screen = game_screen
        self.screen_rect = self.screen.get_rect()
        # Create the list of Rect objects or tiles to draw the lattice on the game board.
        self.lattice = self.construct_lattice() # list of pygame.Rect objects or tiles.  
              
        # Load the tile image and get its rect.
        # self.image = pygame.image.load('images/tile.png')
        # self.rect = self.image.get_rect()        
    
    def construct_lattice(self):
        tiles_list = []
        for i in range(3):
            row = []
            for j in range(3):
                # Syntax: pygame.Rect(x, y, width, height)
                rect = pygame.Rect(
                    self.settings.tile_origin[0] + j * self.settings.tile_size,
                    self.settings.tile_origin[1] + i * self.settings.tile_size,
                    self.settings.tile_size, self.settings.tile_size
                )
                # Save rect in the list row.
                row.append(rect)
            tiles_list.append(row)
        return tiles_list
       
    # Draw game board and display all moves made.
    def update(self, board): # attr board is an instance variable of the Board class: board = Board().
        """Draw OXs inside the tiles of the lattice board."""
        EMPTY_tile = " "
        for i in range(3):
            for j in range(3):
                # Syntax: pygame.draw.rect(Surface, color, Rect, Line Width)
                # Draw tiles to make a lattice.
                pygame.draw.rect(self.screen, self.settings.obj_color, self.lattice[i][j], 3) 
                # Draw pieces: OXs inside tiles on the lattice.
                if board.state_str[i][j] != EMPTY_tile:
                    piece = self.settings.Font_OX.render(str(board.state_str[i][j]), True, self.settings.obj_color)
                    piece_rect = piece.get_rect()
                    tile_rect = pygame.Rect(self.lattice[i][j])
                    piece_rect.center = tile_rect.center
                    self.screen.blit(piece, piece_rect)        
                    