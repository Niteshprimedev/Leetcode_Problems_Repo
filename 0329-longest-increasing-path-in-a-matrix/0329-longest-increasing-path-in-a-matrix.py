class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        # Solution 1: Top Down Memoization Approach;
        m_rows = len(matrix)
        n_cols = len(matrix[0])

        memo_dp = [[-1 for _ in range(n_cols)] for _ in range(m_rows)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        max_inc_path = 0

        def all_inc_paths(row_idx, col_idx, memo_dp):
            if memo_dp[row_idx][col_idx] != -1:
                return memo_dp[row_idx][col_idx]

            max_inc_path = 1
            for direction in directions:
                new_row_idx = row_idx + direction[0]
                new_col_idx = col_idx + direction[1]

                if new_row_idx >= 0 and new_row_idx < m_rows and new_col_idx >= 0 and new_col_idx < n_cols:          
                    curr_inc_path = 0
                    if matrix[new_row_idx][new_col_idx] > matrix[row_idx][col_idx]:
                        curr_inc_path = 1 + all_inc_paths(new_row_idx, new_col_idx, memo_dp)
                    
                    max_inc_path = max(max_inc_path, curr_inc_path)
            
            memo_dp[row_idx][col_idx] = max_inc_path
            return memo_dp[row_idx][col_idx]
        
        for row_idx in range(m_rows):
            for col_idx in range(n_cols):
                new_max_inc_path = all_inc_paths(row_idx, col_idx, memo_dp)
                max_inc_path = max(max_inc_path, new_max_inc_path)
        
        return max_inc_path

        '''
        # Solution 2: Bottom Up Approach;
        m_rows = len(matrix)
        n_cols = len(matrix[0])

        memo_dp = [[0 for _ in range(n_cols)] for _ in range(m_rows)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        max_inc_path = 0

        def all_inc_paths(row_idx, col_idx, memo_dp):
            
            curr_rows = row_idx
            curr_cols = col_idx

            for row_idx in range(curr_rows, -1, -1):
                for col_idx in range(curr_cols, -1, -1):

                    max_inc_path = 0
                    for direction in directions:
                        new_row_idx = row_idx + direction[0]
                        new_col_idx = col_idx + direction[1]

                        if new_row_idx >= 0 and new_row_idx < m_rows and new_col_idx >= 0 and new_col_idx < n_cols:          
                            curr_inc_path = 0
                            if matrix[new_row_idx][new_col_idx] > matrix[row_idx][col_idx]:
                                curr_inc_path = 1 + memo_dp[new_row_idx][new_col_idx]
                            
                            max_inc_path = max(max_inc_path, curr_inc_path)
            
                    memo_dp[row_idx][col_idx] = max_inc_path
            
            return memo_dp[row_idx][col_idx]
        
        for row_idx in range(m_rows - 1, -1, -1):
            for col_idx in range(n_cols - 1, -1, -1):
                max_inc_path = 0
                for direction in directions:
                    new_row_idx = row_idx + direction[0]
                    new_col_idx = col_idx + direction[1]

                    if new_row_idx >= 0 and new_row_idx < m_rows and new_col_idx >= 0 and new_col_idx < n_cols:          
                        curr_inc_path = 0
                        if matrix[new_row_idx][new_col_idx] > matrix[row_idx][col_idx]:
                            curr_inc_path = 1 + memo_dp[new_row_idx][new_col_idx]
                        
                        max_inc_path = max(max_inc_path, curr_inc_path)
        
                memo_dp[row_idx][col_idx] = max_inc_path
                new_max_inc_path = 1 + max_inc_path
                max_inc_path = max(max_inc_path, new_max_inc_path)
        
        return max_inc_path
        '''
        
        '''
        if not matrix:
            return 0
    
        m, n = len(matrix), len(matrix[0])
        dp = [[1 for _ in range(n)] for _ in range(m)]  # Minimum path length is 1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Create a list of cells with their values for sorting
        cells = []
        for row_idx in range(m):
            for col_idx in range(n):
                cells.append((matrix[row_idx][col_idx], row_idx, col_idx))
        
        # Sort cells by their values (ascending)
        cells.sort()
        
        # Process cells in increasing order of values
        max_length = 1
        for val, i, j in cells:
            for di, dj in directions:
                ni, nj = i + di, j + dj
                
                # If neighbor exists and has a smaller value
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] < matrix[i][j]:
                    dp[i][j] = max(dp[i][j], dp[ni][nj] + 1)
            
            max_length = max(max_length, dp[i][j])
        
        return max_length
        '''
            

