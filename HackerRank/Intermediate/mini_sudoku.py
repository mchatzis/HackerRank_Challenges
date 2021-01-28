'''Solve mini sodoku using recursive backtracking'''

import helper_functs as helper
import copy

EMPTY = 0

def solve(board):
    row,col = len(board), len(board[0])
    
    if not helper.is_valid_board(board):
        return False
    if helper.is_full_board(board):
        return True

    for i in range(row):
        for j in range(col):
            if board[i][j] == EMPTY:
                for n in [1,2,3]:
                    board[i][j] = n
                    if solve(board) == True:
                        return True
                    board[i][j] = 0
            else:
                continue
    return False

if __name__ == "__main__":
    
    #Mini sudoku
    board = [ [ 0 , 0 , 0 ],
          [ 1 , 0 , 0 ],
          [ 0 , 3 , 1 ] ]
    
    print("Sudoku to be solved:")
    helper.print_board(board)

    expected = [ [3, 1, 2],
             [1, 2, 3],
             [2, 3, 1] ]
    
    assert solve(board),"Mini Sudoku could not be solved"
    assert board == expected, "Mini Sudoku solution is incorrect"
    print("\n Solved mini sudoku board:")
    helper.print_board(board)
    

    
    
    