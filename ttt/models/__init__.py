# __init__py 
# determines which strategy to use for obtaining the optimal action for AI.

# Strategies
# 1. Random choices
# 2. Axiomatic Rules
# 3. Mathematical calculation of the probability for AI to win.
# 4. Machine Learning

__all__ = ["ModelRandom", "SimpleRandom", "MonteCarlo", "MCBoard", "MCData", "ModelMinimax", "ModelAxiomatic"]

# import modules
# from .monte_carlo.simple_random import *
from .model_random import *
# from .monte_carlo.mc_board import *
from .axiomatic import *
# from .monte_carlo.mc_stats import *
from .model_minimax import *
#
# import packages
from .monte_carlo import *
from .minimax import *