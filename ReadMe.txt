# readme.txt 
# Tic-Tac-Toe Game!
# written by Chang-Jin Lee in 2025

- This project is to make a simple tic-tac-toe game set out by Chang-Jin Lee in 2025 on the purpose of just a self-study. 
- There may be some bugs in the codes especially in Monte Carlo Simulation, so that this codes should be used on the user's risk.
- Reference:
    1. The main source codes comes from the Tic-Tac-Toe Project given by Harvard on-line Machine Learning course CS50 AI.
       I modified the source codes into a class-based object-oriented-style codes.
    2. The main structure of the modified codes comes from the booK "Python Crash Course, by Eric Mathes, 2nd Ed. no stark press (2019)".

Tasks for some improvements.
A. Develop some strategies for AI to find the optimal action.
    1. Random Choices: At present, the strategy of AI minimax algorithm is just a simple random choice. 
        This stragedy can be pursued a little more into the deeper layers in depth taking the user's random response once more into account and the AI's too to the end of the game. This strategy may be called a Monte Carlo Simulation. Combine it with the Bayesian theorem to correct the probability with a new evidence. 
    2. Axiomatic Rules: Develop axiomatic rules for AI to judge what to do or not.
    3. Mathematical Calculation: Perform a specific mathematical calculation to get the probability for AI to win for an AI's specific action or a move.
       Take into account of some possible user's responses in series into the deeper layers.
    4. Machine Learning: Make AI learn from experiences or data.
    
B. Construct db with sqlite.
    - Open, Public Data Policy: No Ownership.
    - data contents: 
        1. game log/arxiv: game time, game id, game record, game score.
        2. game user: user id, user name, game log/arxiv.

C. Implement logging

D. Add more game modes.
    1. AI moves first mode.
    2. AI model selection mode.

E. Add new features.
    1. Pre-calculate the probability for USER to win for each tile and offer it when requested.

F. Prepare packaging this python project.
    1. pyproject.toml, setup.py
    2. README.md, LICENSE
    3. pytest
    4. building and distribution: CI/CD
    