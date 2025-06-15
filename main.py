# main.py for Tic-Tac-Toe Game! 
# written by Changjin Lee in 2025.
# email: changjin.lee.phys@gmail.com

# reference: 
#   - Python Crash Course, Eric Matthes, 2nd Ed., no starch press (2019)
#   - Project source files from Havard on-line Machine Learning course of CS50 AI, 1st lecture.
#     Modified into an object-oriented style codes.

import sys, time, pygame

from settings import Settings
from player import Player
from board import Board
from tiles import Tiles
# Import Models package that includes various strategies for AI to find the optimal action.
from models import *

class TicTacToe:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """initialize the game, and create game resorces"""
        pygame.init()
        # Create a Settings class
        self.settings = Settings()
        
        # Create a screen and caption on it.
        self.screen = pygame.display.set_mode(self.settings.screen_size)
        pygame.display.set_caption('Tic Tac Toe Game')   
           
        # Create two instances of Player class: user and AI. 
        self.user = Player() # agent=None, on_turn=False
        self.ai = Player() # agent=None, on_turn=False   
        # user can choose an agent from "O" or "X": Set as ai.agent = None as default value
        # Set as user.on_turn = False and ai.on_turn = False: 
        # user makes the first move, then AI takes the second.
        
        # Create a game board: an instance of the Board class.
        self.board = Board()
        # Create a 3x3 lattice on the board: an instance of the Tiles class.
        self.tiles = Tiles(self.screen) # Here self.screen attr required!
        # Create a class variable: winner
        self.winner = None # "You" or "AI", otherwise None for Tie.
        
        # Create instance variables
        self.buttons_intro = [None, None] # includes two pygame.Rect objects.
        self.running = True
        
    def run_game(self):
        """Start the main loop for the game"""
        
        while self.running:
            # Start a game.
            # user.agent = 1 stands for "X" while -1 for "O", otherwise None.
            if self.user.agent == None and not self.board.game_over: 
                # Fill the screen with black-color.
                self.screen.fill(self.settings.bg_color)
                # # Show Agent Buttons for the user to choose.
                self.pop_up_screen()
                # Check events to set the user's agent and start a game, or quit.
                self.check_start()
                
            elif self.user.agent != None and not self.board.game_over: 
                # After the user starts playing a game!
                # Display a game board.
                self.screen.fill(self.settings.bg_color)
                self.board.update(self.board.state)
                self.tiles.update(self.board)
                 
                # Check if the game is over. 
                # if negative, check which place the user moves to, and apply user's move to the state of the board.
                self.check_winner()
                self.put_user_on_notice()
                self.check_user_move()
                
                # Check if the game is over, 
                # If negative, AI is the next mover. Then, calculate the best move for AI. 
                # Select a model for AI to find the optimal action for its move.     
                if self.ai.on_turn and not self.user.on_turn:
                    # Check the winner and display which player is going to move.
                    self.check_winner()
                    self.put_user_on_notice()
                    # AI moves when the game is not over.
                    # AI can select a model to find the optimal action: 1. Random, 2. Axiomatic, 3. Mathematical, 4. Machine Learning.
                    self.make_ai_move()
                            
            elif self.board.game_over:  
                # Check if the user want to replay.
                self.check_replay()
                
            # Make the most recently drawn screen visible.
            pygame.display.flip()
        

    def pop_up_screen(self):     
        # Draw title: Play Tic-Tac-Toe.
        title_text_intro = self.settings.Font_Large.render("Play Tic-Tac-Toe", True, self.settings.obj_color) # True activates anti-alias.
        title_text_rect = title_text_intro.get_rect()
        title_text_rect.center = ((self.settings.screen_width / 2), 50)
        self.screen.blit(title_text_intro, title_text_rect)
        # Draw X button
        button_X_rect = pygame.Rect((self.settings.screen_width / 8), (self.settings.screen_height / 2), self.settings.screen_width / 4, 50)
        notice_text_X = self.settings.Font_Medium.render("Play as X", True, self.settings.bg_color)
        notice_text_X_rect = notice_text_X.get_rect()
        notice_text_X_rect.center = button_X_rect.center
        pygame.draw.rect(self.screen, self.settings.obj_color, button_X_rect)
        self.screen.blit(notice_text_X, notice_text_X_rect)
        # Draw O button
        button_O_rect = pygame.Rect(5 * (self.settings.screen_width / 8), (self.settings.screen_height / 2), self.settings.screen_width/ 4, 50)
        notice_text_O = self.settings.Font_Medium.render("Play as O", True, self.settings.bg_color)
        notice_text_O_rect = notice_text_O.get_rect()
        notice_text_O_rect.center = button_O_rect.center
        pygame.draw.rect(self.screen, self.settings.obj_color, button_O_rect)
        self.screen.blit(notice_text_O, notice_text_O_rect)
        # Save the rect objects of the buttons in the intro screen.
        self.buttons_intro = [button_X_rect, button_O_rect]
                                   
    def check_start(self):
        # Respond the keyboard and mouse events.
        for event in pygame.event.get():
            # Terminate a game, and close the window pannel.
            if event.type == pygame.QUIT:
                self. running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.running = False
                    pygame.quit()
                    sys.exit()
            # Before agents have been assigned
            elif event.type == pygame.MOUSEBUTTONUP:
                # pygame.mouse.get_pressed() returns a tuple with three integers, for example, (1, 0, 0),
                # Check if mounse clicked, and which tile it clicked on
                mouse_location = pygame.mouse.get_pos()
                # Assign user's agent to user
                agent_assigned = self.assign_agent(mouse_location) # attr not required.
                # Make user be the first mover.
                if agent_assigned:
                    self.user.on_turn = True
                    self.ai.on_turn = False
                    # Update self.user.agent_str and self.ai.agent_str
                    self.user.convert_agent_to_str()
                    self.ai.convert_agent_to_str()
                    # Update the status of user and AI.
                    # self.user.update(self.board)
                    # self.ai.update(self.board)

    def assign_agent(self, mouse_location):
        # Check if button is clicked
        # pygame.mouse.get_pressed() returns a tuple with three integers, for example, (1, 0, 0),
        # where the first number 1 stands for left mouse button clicked whereas 0 for not yet clicked.
        if self.buttons_intro[0].collidepoint(mouse_location): # self.intro_buttons[0] : button_X
            time.sleep(0.2)
            self.user.agent = self.settings.X 
            self.ai.agent = self.settings.O 
            return True
        elif self.buttons_intro[1].collidepoint(mouse_location): # self.intro_buttons[1] : button_O
            time.sleep(0.2)
            self.user.agent = self.settings.O
            self.ai.agent = self.settings.X  
            return True
        else:
            return False
 
    # Check if a game is over, and determines who is the winner.
    def find_winner(self):
        # Determins who is the winner when the game is over.
        if self.board.game_over:
            if self.user.win and not self.ai.win:
                return "You"
            elif self.ai.win and not self.user.win:
                return "AI"
            else:
                return None 
        else:
            return None
        
    def check_winner(self):
        # Check whether the game is over or not.
        # by using self.board.game_over
        self.winner = self.find_winner() # Returns You or AI or None in str    

    def put_user_on_notice(self):
        # Show the status of the current game on the screen.
        # 3 status: on play as X or O, otherwise the game is over.      
        # put user on notice
        # Determine which sentence to be shown on the board.
        if self.board.game_over:
            if self.winner is None:
                title = f"Game Over: Tie."
            elif self.winner != None:
                title = f"Game Over: {self.winner} wins."
        elif self.user.on_turn:
            title = f"Play as {self.user.agent_str}"
        elif self.ai.on_turn:
            title = f"Computer thinking..."
        # Secondly, Show the title on the screen.    
        title_mid = self.settings.Font_Large.render(title, True, self.settings.obj_color)
        title_rect = title_mid.get_rect()
        title_rect.center = ((self.settings.screen_width / 2), 30)
        self.screen.fill(self.settings.bg_color)
        self.tiles.update(self.board) # attr board=Board() required.
        self.screen.blit(title_mid, title_rect) 
        
    def check_user_move(self):
        # Check if the user moved, and apply user's move to the state of the board.
        if self.user.on_turn:
            for event in pygame.event.get():
                # Terminate a game, and close the window pannel.
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.running = False
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse_location = pygame.mouse.get_pos()
                    # if event.button == 1:
                    for i in range(3):
                        for j in range(3):
                            if self.board.state[i][j] == self.settings.EMPTY and self.tiles.lattice[i][j].collidepoint(mouse_location):
                                # If mouse clicked on the tile (i, j),
                                self.user.action_optimal = (i, j)
                                # Update the state of the board with the user's move on the tile at (i, j).
                                self.board.state = self.user.apply_action_optimal(self.board, self.user.action_optimal, self.user.agent) 
                                # Update board with user'move.
                                self.board.update(self.board.state) # attr board.state required.
                                # Update user's status after the user's move.
                                self.user.update(self.board) # For user's update, attr class instance board required.
                                self.ai.update(self.board)
                                # Check the winner and Update the screen.
                                self.check_winner()
                                self.put_user_on_notice()
                                self.tiles.update(self.board)
                                # Write the user's move and save it in user's archive
                                self.user.archive[self.board.count_filled] = self.user.action_optimal 
                                # Make AI be the next mover.
                                self.user.on_turn = False
                                self.ai.on_turn = True                           

    def make_ai_move(self):
        # Check if AI moves next, and calculate the best move for AI. 
        # Use a minimax algorithm for the optimal action for AI.
        #
        # Check if the user want to stop.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.running = False
                    pygame.quit()
                    sys.exit()
        # Calculate the optimal action for AI
        if self.ai.on_turn and not self.user.on_turn and not self.board.game_over:
            # Determine which model is to be used for AI.
            model = ModelRandom(self.board)
            # Calculate the optimal action for AI
            self.ai.action_optimal = model.minimax() 
            # time.sleep(0.5)
            # ai.action_optimal is the optimal action for ai to take.
            self.board.state = self.ai.apply_action_optimal(self.board, self.ai.action_optimal, self.ai.agent) 
            # where self.board.state is the state written in terms of integers {-1, 0, 1}.
            # Get the updated state displayed on the board.
            self.board.update(self.board.state) # For board's update, attr state_num required.
            # Update the status of the players.
            self.ai.update(self.board) 
            self.user.update(self.board) # For user's update, the classe instance board required.
            # Update the screen.
            self.check_winner()
            self.put_user_on_notice()
            self.tiles.update(self.board)
            # Save AI's move in user's archive.
            self.user.archive[self.board.count_filled] = self.ai.action_optimal
            # Make the user be the next player. 
            self.user.on_turn = True
            self.ai.on_turn = False          
    
    def reset(self):
        # Initialize
        self.board.initialize()
        self.user.initialize()
        self.ai.initialize()
        # Initialize the status of board and tiles
        self.board.update(self.board.state)
        self.tiles.update(self.board)
        
    def check_replay(self):
        # Check for a new game
        again_button = pygame.Rect(self.settings.screen_width / 3, self.settings.screen_height - 65, self.settings.screen_width / 3, 50)
        again_text = self.settings.Font_Medium.render("Play Again", True, self.settings.bg_color)
        again_text_rect = again_text.get_rect()
        again_text_rect.center = again_button.center
        # Syntax: pygame.draw.rect(surface, color, rect, width=0) <-- draw a rectangle on the screen
        pygame.draw.rect(self.screen, self.settings.obj_color, again_button) 
        self.screen.blit(again_text, again_text_rect) # draw a text line on a rectangular box.
        # Check if user clicked on the Again Button.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.running = False
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_location = pygame.mouse.get_pos()
                if again_button.collidepoint(mouse_location):
                    time.sleep(0.2)
                    # print("Play Again button clicked!")
                    self.reset()

            
# Main starts here!            
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ttt = TicTacToe()
    ttt.run_game()