import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 540, 540  # Define the width and height of the window
WHITE = (255, 255, 255)    # Define colors using RGB values
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)

# Set up the display
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Create a window with defined width and height
pygame.display.set_caption("Sudoku Solver")     # Set the window title
FONT = pygame.font.Font(None, 40)               # Define a font for rendering text

def find_next_empty(puzzle):
    """Find the next empty cell in the puzzle."""
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:  # If the cell is empty (-1), return its coordinates
                return r, c
    return None, None  # If there are no empty cells, return None

def is_valid(puzzle, guess, row, col):
    """Check if the given guess is valid at the specified position."""
    # Check if the guess is already in the same row or column
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # Check if the guess is already in the same 3x3 grid
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve_sudoku(puzzle, original_puzzle):
    """Recursively solve the Sudoku puzzle using backtracking."""
    row, col = find_next_empty(puzzle)
    if row is None:  # If there are no empty cells, the puzzle is solved
        return True

    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess  # Try the guess
            # Print and visualize the guess
            print(f"Guess {guess} at ({row}, {col})")
            draw_grid(puzzle, original_puzzle)
            pygame.time.delay(100)  # Add a delay for visualization
            if solve_sudoku(puzzle, original_puzzle):  # Recursively solve the rest of the puzzle
                return True
            print(f"Backtrack at ({row}, {col})")  # If the guess leads to a dead end, backtrack
        puzzle[row][col] = -1  # Reset the guess

    return False

def draw_grid(puzzle, original_puzzle):
    """Draw the Sudoku grid with numbers."""
    WIN.fill(WHITE)  # Fill the window with a white background
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] != -1:  # If the cell is not empty
                color = RED if puzzle[r][c] == original_puzzle[r][c] else BLACK  # Check if it's an original number
                text_surface = FONT.render(str(puzzle[r][c]), True, color)  # Render the number as text
                text_rect = text_surface.get_rect(center=(c * (WIDTH // 9) + (WIDTH // 18),
                                                          r * (HEIGHT // 9) + (HEIGHT // 18)))  # Position the text
                WIN.blit(text_surface, text_rect)  # Draw the text on the window

    # Draw grid lines
    for x in range(0, WIDTH, WIDTH // 9):
        pygame.draw.line(WIN, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, HEIGHT // 9):
        pygame.draw.line(WIN, BLACK, (0, y), (WIDTH, y))
    for x in range(0, WIDTH, WIDTH // 3):
        for y in range(0, HEIGHT, HEIGHT // 3):
            pygame.draw.rect(WIN, GRAY, (x, y, WIDTH // 3, HEIGHT // 3), 3)

    pygame.display.update()  # Update the display

def main():
    # Define the Sudoku puzzle and its original state
    example_board = [
        [-1, 7, -1, -1, -1, 2, -1, 8, -1],
        [-1, -1, -1, 3, 5, -1, -1, -1, -1],
        [-1, -1, 2, 7, -1, -1, -1, 5, -1],
        [-1, 5, -1, -1, 6, -1, -1, -1, -1],
        [2, -1, 6, -1, -1, 3, -1, -1, -1],
        [-1, -1, -1, 8, -1, -1, -1, -1, -1],
        [5, -1, -1, -1, -1, -1, 4, -1, 1],
        [6, -1, -1, 1, -1, 5, -1, -1, -1],
        [1, -1, 7, -1, -1, -1, -1, 3, -1]
    ]
    original_board = [
        [-1, 7, -1, -1, -1, 2, -1, 8, -1],
        [-1, -1, -1, 3, 5, -1, -1, -1, -1],
        [-1, -1, 2, 7, -1, -1, -1, 5, -1],
        [-1, 5, -1, -1, 6, -1, -1, -1, -1],
        [2, -1, 6, -1, -1, 3, -1, -1, -1],
        [-1, -1, -1, 8, -1, -1, -1, -1, -1],
        [5, -1, -1, -1, -1, -1, 4, -1, 1],
        [6, -1, -1, 1, -1, 5, -1, -1, -1],
        [1, -1, 7, -1, -1, -1, -1, 3, -1]
    ]

    draw_grid(example_board, original_board)  # Draw the initial Sudoku grid
    solve_sudoku(example_board, original_board)

# Add an event loop to keep the window responsive
if __name__ == "__main__":
    main()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
