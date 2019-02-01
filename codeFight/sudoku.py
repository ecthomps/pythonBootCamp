sudoku=[[7, 5, 1,  8, 4, 3,  9, 2, 6],
        [8, 9, 3,  6, 2, 5,  1, 7, 4], 
        [6, 4, 2,  1, 7, 9,  5, 8, 3],
        [4, 2, 5,  3, 1, 6,  7, 9, 8],
        [1, 7, 6,  9, 8, 2,  3, 4, 5],
        [9, 3, 8,  7, 5, 4,  6, 1, 2],
        [3, 6, 4,  2, 9, 7,  8, 5, 1],
        [2, 8, 9,  5, 3, 1,  4, 6, 7],
        [5, 1, 7,  4, 6, 8,  2, 3, 9]]

def valid_sudoku2(grid):
    is_sudoku = True
    #check 3*3
    for row3x3 in range(0,9,3):
        for col3x3 in range(0,9,3):
            vals = [val for row in grid[row3x3:row3x3+3] for val in row[col3x3:col3x3+3]]
            if len(vals) != len(set(vals)):
                is_sudoku = False
    
    #check columns
    for row in range(9):
        vals = [val for val in grid[row]]
        if len(vals) != len(set(vals)):
            is_sudoku = False

    #check rows
    for col in range(9):
        vals = [val[col] for val in grid]
        if len(vals) != len(set(vals)):
            is_sudoku = False
    
    return is_sudoku

if valid_sudoku2(sudoku):
    print("Valid Sudoku")
else:
    print("Not Valid")

# def printSudoku(lst):
#     for i in range(len(lst)):
#         for j in range(len(lst[i])):
#             print(lst[i][j], end=' ')
#         print()

# printSudoku(sudoku)
