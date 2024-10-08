# 🐍 PythonProjects
Welcome to my Python Projects repository! This collection showcases a variety of Python projects that I have created to explore different aspects of programming, challenge my skills, and demonstrate my capabilities as a developer. Each project reflects my interests and passion for coding, as well as my commitment to continuous learning and improvement.

The primary purpose of this repository is to:

- Explore Interests: Dive into areas of programming that intrigue me, such as game development, data analysis, and algorithm design.
- Test Skills: Challenge myself with complex problems and projects to enhance my coding proficiency and problem-solving abilities.
- Showcase Abilities: Present my work to potential employers, collaborators, and the developer community to demonstrate my skills and dedication.
<hr>

### Multi-Output Classification on Modified MNIST
This Python project implements a deep learning model using TensorFlow/Keras to perform multi-output classification on a modified MNIST dataset, designed to identify overlapping digits in images.

1 - Dataset Preparation: The modified MNIST dataset contains images with overlapping digits. The data was preprocessed and formatted to suit multi-output classification, where each image corresponds to two labels, one for each digit.

2 - Model Architecture: A Convolutional Neural Network (CNN) was developed and fine-tuned for this task. The architecture was optimized through a custom grid search, focusing on hyperparameters like learning rate and dropout rates. K-fold cross-validation was employed to ensure robustness and prevent overfitting.

3 - Training and Optimization: The model was trained using categorical cross-entropy loss and the Adam optimizer. Hyperparameters were optimized to achieve maximum accuracy across both output categories, ensuring the model could effectively learn and differentiate between overlapping digits.

4 - Evaluation and Analysis: Performance was evaluated per digit, with detailed analysis of learning curves and accuracy metrics. The model’s results were visualized using Matplotlib, demonstrating advanced techniques in computer vision and deep learning.
<hr>

### Connect 4 AI
This Python script implements a Connect Four game using the minimax algorithm for the AI player. 

1 - Board Setup: The game board is represented as a NumPy array, with rows and columns defined by constants ROW_COUNT and COLUMN_COUNT. Pieces are represented as integers: EMPTY, PLAYER_PIECE, and AI_PIECE.

2 - Game Mechanics: The drop_piece() function allows players to place their pieces on the board, and the is_valid_location() function checks if a column is a valid move. The game tracks winning moves using the winning_move() function, which checks for four consecutive pieces in any direction.

3 - AI Implementation: The AI uses the minimax algorithm to determine the best move. The minimax() function recursively evaluates future board states to determine the optimal move, considering both maximizing (AI) and minimizing (player) scenarios. The AI evaluates potential moves using a scoring system based on the positions of pieces.

4 - User Interface: Pygame is used to create the game interface. The game window displays the board, and players can interact by clicking on columns to place their pieces. The game ends when a player wins or the board is full. After each game, players can restart by clicking on the screen.

This script combines game logic, AI decision-making, and user interface elements to create a playable Connect Four game with an AI opponent.
<hr>

### SudokuSolver
This Python script creates a Sudoku Solver application using Pygame.

1 - Initialising Pygame: Pygame is initialized using pygame.init(), which sets up the Pygame environment for use.

2 - Constants and Setup: The script defines several constants such as the window width and height (WIDTH and HEIGHT), colors (e.g., WHITE, BLACK, RED), and a font for rendering text. The display window is created using pygame.display.set_mode() with the specified dimensions, and the window title is set using pygame.display.set_caption().

3 - Sudoku Logic: The script implements functions for solving Sudoku puzzles. The find_next_empty() function finds the next empty cell in the puzzle. The is_valid() function checks if a given number is valid at a specified position according to Sudoku rules. The solve_sudoku() function recursively solves the puzzle using backtracking, trying different guesses until a solution is found.

4 - Drawing the Grid: The draw_grid() function visualises the Sudoku grid on the Pygame window. It fills the window with a white background and draws the grid lines, numbers, and original puzzle values in red.

5 - Main Function: The main() function initialises the Sudoku puzzle and its original state, draws the initial grid, and calls the solve_sudoku() function to solve the puzzle.

