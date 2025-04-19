class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        # Bottom Up Approach:
        # Notes: Robot can move up, and left only
        # Base Case: when the robot is reached (0,0) cell
        # we found a unique path

        m_rows = m
        n_cols = n

        memo_dp = [[0 for _ in range(n_cols)] for _ in range(m_rows)]

        # base case:
        memo_dp[0][0] = 1

        for row_idx in range(m_rows):
            for col_idx in range(n_cols):
                if row_idx == 0 and col_idx == 0:
                    # Base case when robot is at cell(0,0)
                    memo_dp[0][0] = 1
                else:
                    moving_up_paths_count = 0
                    moving_left_paths_count = 0

                    # Robot can move only up if there are any paths
                    if row_idx > 0:
                        moving_up_paths_count = memo_dp[row_idx - 1][col_idx]
                    
                    # Robot can move only left if there are any paths
                    if col_idx > 0:
                        moving_left_paths_count = memo_dp[row_idx][col_idx - 1]
                    
                    # Total paths explored by robot from this particular cell
                    memo_dp[row_idx][col_idx] = moving_up_paths_count + moving_left_paths_count
        
        return memo_dp[m_rows - 1][n_cols - 1]
        '''

        # Space Optimized Bottom Up Approach:
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