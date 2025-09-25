class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Top Down Approach:
        m_rows = len(triangle)

        memo_dp = [[-1 for _ in range(m_rows)] for _ in range(m_rows)]

        def all_path_sum(curr_idx, curr_row_len):
            # print(curr_idx, curr_row_len)
            # Base Case:
            if curr_idx == 0 and curr_row_len == 0:
                return triangle[curr_idx][curr_row_len]
            elif curr_idx < 0 or curr_row_len < 0 or curr_idx > curr_row_len:
                return float('inf')
            
            if memo_dp[curr_idx][curr_row_len] != -1:
                return memo_dp[curr_idx][curr_row_len]
            
            # pick the current_idx;
            chose_curr_idx = triangle[curr_row_len][curr_idx] + all_path_sum(curr_idx, curr_row_len - 1)

            chose_next_idx = triangle[curr_row_len][curr_idx] + all_path_sum(curr_idx - 1, curr_row_len - 1)

            memo_dp[curr_idx][curr_row_len] = min(chose_curr_idx, chose_next_idx)
            return memo_dp[curr_idx][curr_row_len]
        
        min_path_sum = float('inf')
        for idx_i in range(m_rows):
           new_min_path_sum = all_path_sum(idx_i, m_rows - 1)
           min_path_sum = min(min_path_sum, new_min_path_sum)

        return min_path_sum
        