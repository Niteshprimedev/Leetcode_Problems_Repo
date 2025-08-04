class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Solution: Find the transpose of the matrix
        # reverse the cols of the matrix;
        '''
        90 = transpose + reverse row
        180 = reverse row + reverse column
        270 = transpose + reverse col
        '''

        '''
        # simple way to transpose: to run the second loop from row_idx and not 0;

        # Brute Force: Using Extra Space of n*n
        # and loop through the given matrix & for each
        # mat[row_idx][col_idx]
        # new_mat[col_idx][m_rows - row_idx] = mat[row_idx][col_idx]
        
        # Solution2: Using the trick or formula:
        # Step1: Reverse the cols of the matrix
        # Step2 : Transpose the matrix first

        # Or Step1: Transpose the matrix first
        # Step2: Reverse the rows of the matrix
        
        m_rows = len(matrix)
        n_cols = len(matrix[0])
        
        # Step1: Reverse the cols of the matrix;
        for col_idx in range(n_cols):
            strt_row_idx = 0
            for row_idx in range(m_rows - 1, -1, -1):
                if row_idx <= strt_row_idx:
                    break
                    
                first_val = matrix[strt_row_idx][col_idx]
                last_val = matrix[row_idx][col_idx]
                
                matrix[row_idx][col_idx] = first_val
                matrix[strt_row_idx][col_idx] = last_val
                
                strt_row_idx += 1
                
        # Step2: Transpose the matrix: Simply run nested loops
        # but this time, your second col loop will run from row_idx
        # and not from col_idx 0;
        for row_idx in range(m_rows):
            for col_idx in range(row_idx, n_cols):
                cell_val = matrix[row_idx][col_idx]
                matrix[row_idx][col_idx] = matrix[col_idx][row_idx]
                matrix[col_idx][row_idx] = cell_val
            
        return matrix
        '''
        
        '''
        # Solution3: Using the trick or formula:
        # Step1: Reverse the cols of the matrix
        # Step2 : Transpose the matrix first
        # Note: Transpose only upper traingular matrix part;

        # Or Step1: Transpose the matrix first
        # Step2: Reverse the rows of the matrix
        
        m_rows = len(matrix)
        n_cols = len(matrix[0])
        
        # Step1: Reverse the cols of the matrix;
        for col_idx in range(n_cols):
            strt_row_idx = 0
            for end_row_idx in range(m_rows - 1, -1, -1):
                if end_row_idx <= strt_row_idx:
                    break
                    
                first_val = matrix[strt_row_idx][col_idx]
                last_val = matrix[end_row_idx][col_idx]
                
                matrix[end_row_idx][col_idx] = first_val
                matrix[strt_row_idx][col_idx] = last_val
                
                strt_row_idx += 1
                
        # Step2: Transpose the matrix: Simply run nested loops
        # but this time, your second col loop will run from row_idx
        # and not from col_idx 0;
        for row_idx in range(m_rows):
            for col_idx in range(row_idx + 1, n_cols):
                cell_val = matrix[row_idx][col_idx]
                matrix[row_idx][col_idx] = matrix[col_idx][row_idx]
                matrix[col_idx][row_idx] = cell_val
            
        return matrix
        '''

        # Solution4: Using the trick or formula:
        # Step1: Reverse the cols of the matrix
        # Step2 : Transpose the matrix first

        # Or Step1: Transpose the matrix first 
        # Step2: Reverse the rows of the matrix
        # Note: Transpose only upper traingular matrix part;
        
        m_rows = len(matrix)
        n_cols = len(matrix[0])

        # Step1: Transpose the matrix: Simply run nested loops
        # but this time, your second col loop will run from row_idx
        # and not from col_idx 0;
        for row_idx in range(m_rows):
            for col_idx in range(row_idx + 1, n_cols):
                cell_val = matrix[row_idx][col_idx]
                matrix[row_idx][col_idx] = matrix[col_idx][row_idx]
                matrix[col_idx][row_idx] = cell_val
        
        # Step2: Reverse the rows of the matrix;
        for row_idx in range(m_rows):
            strt_col_idx = 0
            for end_col_idx in range(n_cols - 1, -1, -1):
                if end_col_idx <= strt_col_idx:
                    break
                    
                first_val = matrix[row_idx][strt_col_idx]
                last_val = matrix[row_idx][end_col_idx]
                
                matrix[row_idx][end_col_idx] = first_val
                matrix[row_idx][strt_col_idx] = last_val
                
                strt_col_idx += 1
            
        return matrix
        