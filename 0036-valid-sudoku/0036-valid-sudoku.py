class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        # Check Valid sudoku;
        def val_in_submatrix(row_idx, col_idx, curr_val):

            strt_row = (row_idx // 3) * 3
            strt_col = (col_idx // 3) * 3

            end_row = strt_row + 3
            end_col = strt_col + 3

            for r in range(strt_row, end_row):
                for c in range(strt_col, end_col):
                    if (r != row_idx and c != col_idx) and board[r][c] == curr_val:
                        return True
            
            return False
        
        def val_in_row(row_idx, col_idx, curr_val):
            for c in range(0, 9):
                if c != col_idx and board[row_idx][c] == curr_val:
                    return True
                
            return False
        
        def val_in_col(row_idx, col_idx, curr_val):
            for r in range(0, 9):
                if r != row_idx and board[r][col_idx] == curr_val:
                    return True
            
            return False
        
        def check_sudoku(row_idx, col_idx, board):
            # Base Case:
            if row_idx == 9 and col_idx == 9:
                return True
            elif row_idx >= 9:
                return False

            is_valid_sudoku = False

            new_col_idx = col_idx
            new_row_idx = row_idx

            if new_col_idx < 8:
                new_col_idx += 1
            else:
                if new_row_idx == 8:
                    new_col_idx += 1
                    new_row_idx += 1
                else:
                    new_col_idx = 0
                    new_row_idx += 1

            if board[row_idx][col_idx] != ".":
                curr_val = board[row_idx][col_idx]

                curr_val_in_submatrix = val_in_submatrix(row_idx, col_idx, curr_val)
                curr_val_in_row = val_in_row(row_idx, col_idx, curr_val)
                curr_val_in_col = val_in_col(row_idx, col_idx, curr_val)

                if not curr_val_in_submatrix and not curr_val_in_row and not curr_val_in_col:                   
                    is_valid_sudoku = check_sudoku(new_row_idx, new_col_idx, board)
            else:
                is_valid_sudoku = check_sudoku(new_row_idx, new_col_idx, board)
                
            return is_valid_sudoku
        
        return check_sudoku(0, 0, board)
        '''

        '''
        # Anothe rSOlution;

        def is_valid(board, row, col, num):
            # check row and column;
            for i in range(9):
                if i == row or i == col:
                    continue

                if board[row][i] == num or board[i][col] == num:
                    return False
            
            # check 3*3 subgrid
            strt_row = (row // 3) * 3
            strt_col = (col // 3) * 3

            for i in range(3):
                for j in range(3):
                    if (strt_row + i) == row and (strt_col + j) == col:
                        continue
                    if board[strt_row + i][strt_col + j] == num:
                        return False
            
            return True

        for row in range(9):
            for col in range(9):
                num = board[row][col]

                if num != ".":
                    if not is_valid(board, row, col, num):
                        # print(row, col, num)
                        return False
        
        return True
        '''

        # Great Solution and Logic Based:
        # CHeck each row
        # CHeck each col
        # CHeck each square

        def is_valid(arr):
            res = [i for i in arr if i != "."]

            return len(res) == len(set(res))
        
        def is_valid_row(board):
            for row in board:
                if not is_valid(row):
                    return False
            
            return True
        
        def is_valid_col(board):
            for col in zip(*board):
                if not is_valid(col):
                    return False
            
            return True
        
        def is_valid_square(board):
            for i in (0, 3, 6):
                for j in (0, 3, 6):
                    square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]

                    if not is_valid(square):
                        return False
            
            return True
        
        return is_valid_row(board) and is_valid_col(board) and is_valid_square(board)


