# main.py for Tic-Tac-Toe Game! 
# written by Changjin Lee in 2025.
# email: changjin.lee.phys@gmail.com

# reference: 
#   - Python Crash Course, Eric Matthes, 2nd Ed., no starch press (2019)
#   - Project source files from Havard on-line Machine Learning course of CS50 AI, 1st lecture.
#     Modified into an object-oriented style codes.

import sys, os

main_dir = os.path.abspath(os.path.dirname(__file__))
# src_dir = os.path.join(main_dir, 'ttt')
# sys.path.append(src_dir)
models_path = os.path.join(main_dir, 'models')
sys.path.append(models_path)
mc_path = os.path.join(models_path, 'monte_carlo')
sys.path.append(mc_path)
mm_path = os.path.join(models_path, 'minimax')
sys.path.append(mm_path)
fonts_path = os.path.join(main_dir, 'fonts')
sys.path.append(fonts_path)
images_path = os.path.join(main_dir, 'images')
sys.path.append(images_path)

from tictactoe import TicTacToe
            
# Main starts here!            
if __name__ == '__main__':
    # Make a game instance, and run a game.
    ttt = TicTacToe()
    ttt.run_game()