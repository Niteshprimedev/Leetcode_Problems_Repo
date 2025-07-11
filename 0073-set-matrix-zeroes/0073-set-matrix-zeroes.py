class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        '''
        # Brainstorming:
        # Logic: First Traverse the matrix and mark the rows and cols
        # with -1 indicating that this row and col needs to be set zero

        # And then loop through the rows first, mark the rows zero
        # Then loop through the cols, mark the cols zero

        m_rows = len(matrix)
        n_cols = len(matrix[0])
        is_zero = False

        for row_idx in range(m_rows):
            for col_idx in range(n_cols):
                if (row_idx == 0 or col_idx == 0) and matrix[row_idx][col_idx] == 0:
                    is_zero = True

                if row_idx == 0 and col_idx == 0 and matrix[row_idx][col_idx] == 0:
                    matrix[row_idx][col_idx] = -2
                elif matrix[row_idx][col_idx] == 0:
                    if row_idx != 0:
                        matrix[row_idx][0] = -1
                    matrix[0][col_idx] = -1
        
        print(matrix)
        for row_idx in range(1, m_rows):
            if matrix[0][col_idx] == -1 and n_cols == 1:
                for row_idx in range(m_rows):
                    matrix[row_idx][0] = 0
            elif matrix[row_idx][0] == -1:
                for col_idx in range(n_cols):
                    matrix[row_idx][col_idx] = 0

        for col_idx in range(1, n_cols):
            if matrix[0][col_idx] == -1 and m_rows == 1:
                for col_idx in range(n_cols):
                    matrix[0][col_idx] = 0
            elif matrix[0][col_idx] == -1:
                for row_idx in range(m_rows):
                    matrix[row_idx][col_idx] = 0

        
        for col_idx in range(1):
            if matrix[0][0] == -2:
                for row_idx in range(m_rows):
                    matrix[row_idx][0] = 0
                for col_idx in range(n_cols):
                    matrix[0][col_idx] = 0

        if is_zero:
            matrix[0][0] = 0

        return matrix
        '''

        m_rows = len(matrix)
        n_cols = len(matrix[0])
        first_col = matrix[0][0]
        
        for row_idx in range(m_rows):
            for col_idx in range(n_cols):
                if col_idx == 0 and matrix[row_idx][col_idx] == 0:
                    # print(row_idx, 0)
                    first_col = 0
                elif matrix[row_idx][col_idx] == 0:
                    matrix[row_idx][0] = 0
                    matrix[0][col_idx] = 0

        # print(matrix)    
        # setting all the rows cells and col cells to 1:
            
        # setting ith row cells:
        for row_idx in range(1, m_rows):
            for col_idx in range(1, n_cols):
                if matrix[row_idx][0] == 0 or matrix[0][col_idx] == 0:
                    matrix[row_idx][col_idx] = 0
        
        # setting the first row cells:
        for col_idx in range(1, n_cols):
            if matrix[0][0] == 0:
                matrix[0][col_idx] = 0
            
        # print(matrix, 'second', first_col)
        # setting the first col cells:
        for row_idx in range(m_rows):
            if first_col == 0:
                matrix[row_idx][0] = 0
            
        return matrix                
                

        