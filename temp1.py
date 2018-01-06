
emptyR = 0
emptyC = 0
def findEmpty(row, col):
    for row in range(len(matrix)):
        temp = matrix[row]
        for col in range(len(matrix)): 
            if(temp[col] == "."):
            	return row, col
    return -1,-1 #No more empty cells


def solveSudoku(row, col):
            row,col = findNextCellToFill(row, col)
            if i == -1:
                    return True #Sudoku is solved
            for e in range(1,10): #Possibilities for the empty cell
                    if isValid(grid,i,j,e): #If valie is valid, then assign the value to the empty cell
                            grid[i][j] = e
                            if solveSudoku(grid, i, j): #If this function had returned false earlier ("i == -1")
                                    return True
                            # Undo the current cell for backtracking
                            grid[i][j] = 0
            return False