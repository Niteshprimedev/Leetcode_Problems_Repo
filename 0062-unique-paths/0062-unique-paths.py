class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        # Top Down Approach:

        m_rows = m
        n_cols = n

        memo_dp = [[-1 for _ in range(n_cols)] for _ in range(m_rows)]

        def all_possible_paths(row_idx, col_idx):
            # Base Case:
            if row_idx == 0 and col_idx == 0:
                memo_dp[row_idx][col_idx] = 1
                return 1 #found a unique path
            elif row_idx < 0 or col_idx < 0:
                return 0
            
            if memo_dp[row_idx][col_idx] != -1:
                return memo_dp[row_idx][col_idx]
            
            up_paths_count = all_possible_paths(row_idx - 1, col_idx)
            left_paths_count = all_possible_paths(row_idx, col_idx - 1)

            memo_dp[row_idx][col_idx] = up_paths_count + left_paths_count
            return memo_dp[row_idx][col_idx]

        all_possible_paths(m_rows - 1, n_cols - 1)

        return memo_dp[m_rows - 1][n_cols - 1]
        '''

        '''
        # Bottom Up Approach Solution:
        # Notes: Robot can move up, and left only
        # Base Case: when the robot is reached (0,0) cell
        # we found a unique path

        m_rows = m
        n_cols = n
        
        memo_dp = [[0 for _ in range(n_cols)] for _ in range(m_rows)]
        
        for row_idx in range(m_rows):
            for col_idx in range(n_cols):
                # Base Case:
                if row_idx == 0 and col_idx == 0:
                    memo_dp[row_idx][col_idx] = 1
                else:
                    up_paths_count = 0
                    
                    left_paths_count = 0 
        
                    if row_idx > 0:
                        up_paths_count = memo_dp[row_idx - 1][col_idx]
                        
                    if col_idx > 0:
                        left_paths_count = memo_dp[row_idx][col_idx - 1]
                    
                    memo_dp[row_idx][col_idx] = up_paths_count + left_paths_count
        
        return memo_dp[m_rows - 1][n_cols - 1]
        '''

        # Bottom Up Approach: Optimized Solution 
        # Notes: Robot can move up, and left only
        # Base Case: when the robot is reached (0,0) cell
        # we found a unique path

        m_rows = m
        n_cols = n

        prev_dp = [0 for _ in range(n_cols)]

        # base case:
        prev_dp[0] = 1

        for row_idx in range(m_rows):
            curr_dp = [0 for _ in range(n_cols)]
            
            for col_idx in range(n_cols):
                if row_idx == 0 and col_idx == 0:
                    curr_dp[0] = 1
                else:
                    moving_up_paths_count = 0
                    moving_left_paths_count = 0

                    if row_idx > 0:
                        moving_up_paths_count = prev_dp[col_idx]
                    
                    if col_idx > 0:
                        moving_left_paths_count = curr_dp[col_idx - 1]
                    
                    curr_dp[col_idx] = moving_up_paths_count + moving_left_paths_count
        
            prev_dp = curr_dp
            
        return prev_dp[n_cols - 1]