def find_next_empty(puzzle):
    # find next row, col on the puzzle that's not filled --> represented wuth -1 
    #  return row, col tuple (or(None,None) if there is none)
    
    for r in range(9):
        for c in range(9):   # range is 0 - 9
            if puzzle[r][c] == -1:  #returning item in r row and c cloumn 
                return r,c  #if it does = -1 return that r c 

    return None, None # if no spaces in the puzzle are empty (-1)

def is_valid(puzzle, guess, row,col):
    #fifures out if guess at that row & col is valid
    #returns True if valid, False otherwise

    # start with row 
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    # Checks the column 
 
    col_vals = [puzzle[i][col] for i in range(9)] # takes puzzle index into i within that row index to col and do that for  i in range 9 
    if guess in col_vals:
            return False # means that the number is in that column 

    # Then taking 3x3 grid into consideration 
    # Find where in grid - Starting index of row & starting column
    # iterate over the 3 values in row / column 

    row_start = (row//3) * 3 # 1//3 = 0, eg 5//3 = 1, ...
    col_start = (col//3) * 3

    for r in range(row_start, row_start +3):
        for c in range(col_start, col_start +3):
            if puzzle[r][c] == guess:
                return False

    #If arive here then checks have be passed 
    return True

def solve_sudoku(puzzle):
    # solve using backtracking technique 
    # puzzle is a list if lists, where each list is a row in puzzle 
    # return whether a solution exists 
    # mutates puzzle to be the solution 

    # step 1: choose somewhere on puzzle to start 
    row, col = find_next_empty(puzzle)

    #step 1.1: if nowhere left, then finished
    if row is None: # only need to check one as each space is individual 
        return True

    #step 2: If there is a place to put a number, make guess between 1 and 9 
    for guess in range(1,10): #range is 1 - 9 
        #step 3: check if valid guess 
        if is_valid(puzzle,guess,row,col):  #info needed to make sure the guess is valid
            # step 3.1: If this is valid, then place that guess on the puzzle !
            puzzle[row][col] = guess 
            # now recurse using this puzzle 
            # step 4: call function with new guess
            if solve_sudoku(puzzle):
                return True

        # step 5: if not valid or does not solve then backtarck and try ne number 
        puzzle[row][col] = -1 #reset the guess 


    #step 6: if none of the numbers attempted work then puzzle is unsolvable

    return False 

if __name__ == '__main__':
    example_board = [
        [-1,7,-1,   -1,-1,2,   -1,8,-1],
        [-1,-1,-1,  3,5,-1,  -1,-1,-1],
        [-1,-1,2,  7,-1,-1,    -1,5,-1],
        
        [-1,5,-1,  -1,6,-1,    -1,-1,-1],
        [2,-1,6,   -1,-1,3,   -1,-1,-1],
        [-1,-1,-1,  8,-1,-1,   -1,-1,-1],
        
        [5,-1,-1,  -1,-1,-1,  4,-1,1],
        [6,-1,-1,   1,-1,5,   -1,-1,-1],
        [1,-1,7,   -1,-1,-1,   -1,3,-1]
    ]
    
    print(solve_sudoku(example_board))
    print(example_board)
