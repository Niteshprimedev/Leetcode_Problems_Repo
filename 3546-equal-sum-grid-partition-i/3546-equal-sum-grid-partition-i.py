class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows_sum = []
        cols_sum = []

        m_rows = len(grid)
        n_cols = len(grid[0])

        for row_idx in range(m_rows):
            curr_sum = 0
            for col_idx in range(n_cols):
                curr_sum += grid[row_idx][col_idx]

            rows_sum.append(curr_sum)

        for col_idx in range(n_cols):
            curr_sum = 0
            for row_idx in range(m_rows):
                curr_sum += grid[row_idx][col_idx]

            cols_sum.append(curr_sum)

        # print(rows_sum)
        # print(cols_sum)

        # calculate the equilibrium point:

        def eq_point(arr):
            suffix_sum = sum(arr) - arr[0]
            prefix_sum = arr[0]

            for num_idx in range(1, len(arr)):
                curr_num = arr[num_idx]

                if prefix_sum == suffix_sum:
                    return True

                prefix_sum += curr_num
                suffix_sum -= curr_num

            return False

        is_equal_row_cut = eq_point(rows_sum)
        is_equal_col_cut = eq_point(cols_sum)

        # print(is_equal_row_cut)
        # print(is_equal_col_cut)
        
        return is_equal_row_cut or is_equal_col_cut
        
                